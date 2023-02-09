import sys, os
from .base import AppBase

from PySide2 import QtCore, QtGui, QtUiTools


class Pyside2Mixin(AppBase):
    """
    This will add Pyside2 based GUI controls for your application.
    By default, running the app via CLI is available with the --no_gui flag.
    pre() and post() will not be called when using a GUI so it's up to the
    developer to include them as needed in run_gui().
    """

    gui_file = None

    def __init__(self, ctx=None, argparser=None):
        super().__init__(ctx=ctx, argparser=argparser)

        # Check for a GUI file
        if not self.gui_file:
            self.gui_file = __name__ + ".ui"

    def add_arguments(self):
        """Args that need to be included in the app"""
        self.add_argument("-n", "--no_gui", action="store_true", help="Run Without GUI")
        super().add_arguments()

    def __call__(self, ctx=None):
        if self.arg_dict.get("no_gui", False):
            super.__call__(ctx=ctx)
        else:
            ctx.gui_mode = True
            if not ctx:
                ctx = self.ctx
            self.run_gui(self.ctx)

    def load_gui(self):
        """
        Load the GUI and run.

        Args:
            ctx (Context): Context to execute the tool with
        """
        self.app = QtGui.QApplication(sys.argv)

        # Load the UI file
        loader = QtUiTools.QUiLoader()
        gui_path = os.path.join(os.path.dirname(__file__), self.gui_file)
        uifile = QtCore.QFile(gui_path)
        uifile.open(QtCore.QFile.ReadOnly)

        # Attach the loaded results to the main_window variable
        self.main_window = loader.load(uifile, None)

        uifile.close()

        self.connect_signals_and_slots()

        self.main_window.show()
        sys.exit(self.app.exec_())

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
