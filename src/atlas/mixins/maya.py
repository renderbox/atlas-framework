class MayaAppMixin:
    """
    This mixin is meant to help run a project inside of Maya.  It will automatically
    detect if the current context is inside of Maya and if so, will set the host to
    "maya" and set the context to "maya".

    Mixins are only partially built classes and are meant to override existing with specific
    functionality.  They are not meant to be used directly.
    """

    # Figure out if Maya is the host interpreter
    def determine_host(self):
        if self.host is None:
            # if the host is not set, check to see if we are running in Maya
            try:
                import maya.cmds as cmds  # noqa: F401

                self.host = "maya"
            except ImportError:
                super().determine_host()  # If this does not work, call the superclass

    # def pre_load_ui(self):
    #     """Entry Point that will run before the UI is first loaded"""
    #     if self.host == "maya":
    #         if self.gui_lib == "PySide2":
    #             # PySide2 setup for running inside of Unreal
    #             print("Running PySide2 in Maya")
