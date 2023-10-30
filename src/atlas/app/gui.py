import sys, os

import inspect

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile, QCoreApplication
from PySide2 import QtCore


class Pyside2Base:
    """
    A base class that will load a UI file or auto-built class and connect signals and slots.  It should not be subclassed directly.
    """

    gui_file = None
    gui_class = None
    root = None  # The main window or loaded widget
    gui_lib = "PySide2"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Check for a GUI file and make it the same as the Widget Class if its empty
        if not self.gui_file:
            self.gui_file = self.get_gui_file_name()

    def setup_ui(self, parent=None):
        """
        Evaluated when in GUI mode.  By default just loads the GUI.
        Can be overridden to do other things when loading a GUI.

        Args:
            parent (QObject): Object that will be the parent of this Widget instance
        """
        self.pre_load_ui()
        self.load_gui(parent=parent)
        self.post_load_ui()
        self.connect_signals_and_slots()
        self.post_connect_signals_and_slots()

    def pre_load_ui(self):
        """Entry Point that will run before the UI is first loaded"""
        pass

    def post_load_ui(self):
        """Entry Point that will run after the UI is first loaded but before signals and slots are connected"""
        pass

    def post_connect_signals_and_slots(self):
        """Entry Point that will run after the signals and slots are connected"""
        pass

    def get_gui_file_name(self):
        return self.__class__.__name__ + ".ui"

    def load_gui(self, parent=None):
        """
        Load and create the root GUI with any children already included

        Args:
            ctx (Context): Context to execute the tool with
        """

        if self.gui_class:
            self.root = self.gui_class()
        else:
            # Get the path to the App Class Instance being evaluated
            gui_path = os.path.join(
                os.path.dirname(inspect.getfile(self.__class__)), self.gui_file
            )

            # Load the UI file
            uifile = QFile(gui_path)
            uifile.open(QFile.ReadOnly)
            loader = QUiLoader()

            try:
                # Attach the loaded results to the window variable
                self.root = loader.load(uifile)
            except RuntimeError as e:
                print(
                    "Could not load the file: {}\nOne is needed to use a PySide2 GUI based app.".format(
                        gui_path
                    )
                )
                print(e)

            uifile.close()

    def connect_signals_and_slots(self):
        """Step that will connect signals and slots from the UI file to code"""
        pass


class Pyside2Widget(Pyside2Base, QWidget):
    """
    Widget Class that will load a UI file or auto-built class and connect signals and slots
    """

    def __init__(self, ctx=None, parent=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Creating Widget: {}".format(self.__class__.__name__))
        self.setup_ui(parent=parent)


class Pyside2Mixin(Pyside2Base):
    """
    This will add Pyside2 based GUI controls for your application.
    By default, running the app via CLI is available with the --no_gui flag.
    pre() and post() will not be called when using a GUI so it's up to the
    developer to include them as needed in setup_ui().

    If you provide a GUI Class, that will be used first, followed by a provided name and
    finally by a .ui file named the same as the class at the same path level as the module file.

    Whatever GUI file is provided it assumes the path is relative to the file where your
    App is defined.

    On an app class, the main window will be available as self.root.
    """

    def add_arguments(self):
        """Args that need to be included in the app"""
        self.add_argument("-n", "--no_gui", action="store_true", help="Run Without GUI")
        super().add_arguments()

    def __call__(self, ctx=None):
        ctx = self.pre(ctx)
        if self.arg_dict.get("no_gui", False):
            self.run(ctx)
            self.post()
        else:
            if not ctx:
                ctx = self.ctx
            ctx.gui_mode = True
            self.setup_ui(self.ctx)

    def setup_ui(self, ctx):
        """
        Evaluated when in GUI mode.  By default just loads the GUI.
        Can be overridden to do other things when loading a GUI.

        Args:
            ctx (Context): Context to execute the tool with
        """
        # TODO: Should this be here?
        QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
        host_app = QApplication(sys.argv)

        super().setup_ui(ctx)
        self.root.show()
        # TODO: Add post() call after the app is closed to do any cleanup
        sys.exit(host_app.exec_())
