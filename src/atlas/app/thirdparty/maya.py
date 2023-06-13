from PySide2.QtWidgets import QWidget


def get_maya_main_window():
    """
    Get the Maya Main Window as a QWidget
    """
    import maya.OpenMayaUI as omui
    from shiboken2 import wrapInstance

    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QWidget)


class MayaMixin:
    """An Atlas Mixin to support running inside of Maya"""

    in_maya = False

    def __init__(self, ctx=None, argparser=None):
        super().__init__(ctx=ctx, argparser=argparser)
        try:
            import maya.cmds as cmds

            self.in_maya = True
        except ImportError:
            pass
