import sys
from PySide2.QtWidgets import QApplication

try:
    import unreal_engine as ue
except ImportError:
    pass


def get_unreal_main_window():
    """
    Get the Maya Main Window as a QWidget
    """
    app = QApplication(sys.argv)

    def ticker_loop(delta_time):
        app.processEvents()
        return True

    ticker = ue.add_ticker(ticker_loop)

    root_window = ue.get_editor_window()

    return root_window


class UnrealMixin:

    in_unreal = False

    def __init__(self, ctx=None, argparser=None):
        super().__init__(ctx=ctx, argparser=argparser)
        try:
            import unreal_engine as ue

            self.in_unreal = True
        except ImportError:
            pass
