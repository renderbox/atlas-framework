class UnrealAppMixin:
    """
    This mixin is meant to help run a project inside of Maya.  It will automatically
    detect if the current context is inside of Maya and if so, will set the host to
    "maya" and set the context to "maya".
    """

    # Figure out if Maya is the host interpreter
    def determine_host(self):
        if self.host is None:
            # if the host is not set, check to see if we are running in Maya
            try:
                import unreal  # noqa: F401

                self.host = "unreal"
            except ImportError:
                super().determine_host()  # If this does not work, call the superclass

    # def pre_load_ui(self):
    #     """Entry Point that will run before the UI is first loaded"""
    #     if self.host == "maya":
    #         if self.gui_lib == "PySide2":
    #             # PySide2 setup for running inside of Unreal
    #             unreal.log("Running PySide2 in Unreal")
