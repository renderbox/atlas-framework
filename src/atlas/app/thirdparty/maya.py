from PySide2.QtWidgets import QWidget


class MayaMixin:
    """An Atlas Mixin to support running inside of Maya"""

    in_maya = False

    def __init__(self, ctx=None, argparser=None):
        super().__init__(ctx=ctx, argparser=argparser)
        try:
            # if this library is available, we are in maya
            import maya.cmds as cmds

            self.in_maya = True
        except ImportError:
            pass

    def get_maya_main_window(self):
        """
        Get the Maya Main Window as a QWidget
        """
        import maya.OpenMayaUI as omui
        from shiboken2 import wrapInstance

        main_window_ptr = omui.MQtUtil.mainWindow()
        return wrapInstance(int(main_window_ptr), self.window)

    def run_gui(self, ctx):
        """
        Evaluated when in GUI mode.  By default just loads the GUI.
        Can be overridden to do other things when loading a GUI.

        Args:
            ctx (Context): Context to execute the tool with
        """
        if self.in_unreal:
            import maya.OpenMayaUI as omui
            from shiboken2 import wrapInstance

            main_window_ptr = omui.MQtUtil.mainWindow()
            app = wrapInstance(int(main_window_ptr), self.window)
            self.load_gui()
            self.connect_signals_and_slots()
            self.window.show()
        else:
            super().run_gui(ctx)
