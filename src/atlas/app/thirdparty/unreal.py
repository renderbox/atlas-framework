import sys
from PySide2.QtWidgets import QApplication

try:
    import unreal as ue
except ImportError:
    pass


class UnrealMixin:

    in_unreal = False

    def __init__(self, ctx=None, argparser=None):
        super().__init__(ctx=ctx, argparser=argparser)
        try:
            # if this library is available, we are in unreal
            import unreal as ue

            self.in_unreal = True
        except ImportError:
            pass

    def run_gui(self, ctx):
        """
        Evaluated when in GUI mode.  By default just loads the GUI.
        Can be overridden to do other things when loading a GUI.

        Note that this does not use app.exec_() as it will result in Qt taking control of the UE loop.

        For Unreal Hints, see:
        https://github.com/20tab/UnrealEnginePython

        Args:
            ctx (Context): Context to execute the tool with
        """

        # If this is running inside of Unreal Editor, we need to add a ticker to the main loop
        if self.in_unreal:

            host_app = QApplication(sys.argv)

            def ticker_loop(delta_time):
                host_app.processEvents()
                return True

            ticker = ue.add_ticker(ticker_loop)

            self.load_gui()
            self.connect_signals_and_slots()
            self.window.show()

            root_window = ue.get_editor_window()
            root_window.set_as_owner(self.window.winId())
        else:
            super().run_gui(ctx)
