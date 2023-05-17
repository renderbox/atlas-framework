import sys, os

import inspect

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile, QCoreApplication
from PySide2 import QtCore


class Pyside2Mixin:
    """
    This will add Pyside2 based GUI controls for your application.
    By default, running the app via CLI is available with the --no_gui flag.
    pre() and post() will not be called when using a GUI so it's up to the
    developer to include them as needed in run_gui().

    If you provide a GUI Class, that will be used first, followed by a provided name and
    finally by a .ui file named the same as the class at the same path level as the module file.

    Whatever GUI file is provided it assumes the path is relative to the file where your
    App is defined.
    """

    gui_file = None
    gui_class = None

    def __init__(self, ctx=None, argparser=None):
        super().__init__(ctx=ctx, argparser=argparser)

        # Check for a GUI file and make it the same as the App Class if its empty
        if not self.gui_file:
            self.gui_file = self.get_gui_file_name()

    def get_gui_file_name(self):
        return self.__class__.__name__ + ".ui"

    def add_arguments(self):
        """Args that need to be included in the app"""
        self.add_argument("-n", "--no_gui", action="store_true", help="Run Without GUI")
        super().add_arguments()

    def __call__(self, ctx=None):
        if self.arg_dict.get("no_gui", False):
            super.__call__(ctx=ctx)
        else:
            if not ctx:
                ctx = self.ctx
            ctx.gui_mode = True
            self.run_gui(self.ctx)

    def load_gui(self):
        """
        Load the GUI and run.

        Args:
            ctx (Context): Context to execute the tool with
        """
        QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

        self.app = QApplication(sys.argv)

        if self.gui_class:
            self.window = self.gui_class()
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
                self.window = loader.load(uifile)
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

    def run_gui(self, ctx):
        """
        Evaluated when in GUI mode.  By default just loads the GUI.
        Can be overridden to do other things when loading a GUI.

        Args:
            ctx (Context): Context to execute the tool with
        """
        self.load_gui()

        self.connect_signals_and_slots()

        self.window.show()
        sys.exit(self.app.exec_())
