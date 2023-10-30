import argparse
from atlas.context import Context, camel_case_spaced


class AppBase:
    """
    This is the development level base class and should not be subclassed directly.
    Use the App Class one level above.
    """

    ctx = None
    argparser = None
    description = "No Description set for this application"
    app_name = None  # Human Friendly Name like "App Base", default is class name
    epilog = None  # Text to display at the end of the help
    context_class = Context  # The Context Class to use for this app.  Can be overriden to use a custom Context Class.
    host = None

    def __init__(self, ctx=None, argparser=None):
        if not self.app_name:
            self.app_name = camel_case_spaced(self.__class__.__name__)

        self.determine_host()

        # If no argparser is set, create one
        if not argparser and not self.argparser:
            self.argparser = self.create_argparser()

        # TODO: Add default arguments all apps should have here

        self.add_arguments()

        self.parse_args()

        self.set_context(ctx)  # After the Arg Parser is created,

        self.ctx.host = self.host

    def determine_host(self):
        if self.host is None:
            self.host = "cli"

    def create_argparser(self):
        return argparse.ArgumentParser(
            prog=self.app_name,
            description=self.description,
            epilog=self.epilog,
        )

    def add_arguments(self):
        """Args that need to be included in the app"""
        pass

    def add_argument(self, *args, **kwargs):
        """A wrapper around the arg parser to allow updates without breaking users code."""
        self.argparser.add_argument(*args, **kwargs)

    def parse_args(self):
        """parse args based on the input"""
        parsed, extra_args = self.argparser.parse_known_args()
        try:
            self.arg_dict = vars(
                parsed
            )  # This can fail with unrecognized arguments in the app
        except TypeError:
            self.arg_dict = {}
        return self.arg_dict

    # Create and set the Context object
    def set_context(self, ctx):
        """
        Set Context will set the context to one passed in or will generate one.  One is provided only if it is
        pre-generated somewhere else and passed in, like in the case of chaining App instances.

        Args:
            ctx (Context): Context Class or None

        Returns:
            Context: Instance of the Context Class
        """

        # args = self.parse_args()  # TODO: Handle extra args

        # If no context is passed in, create one
        if ctx:
            self.ctx = ctx
            # TODO: Add any missing required args to the context
        else:
            self.ctx = self.create_context()

        return self.ctx

    def create_context(self):
        """Create a context object to use for the app.  This can be overridden to use a custom context object or method."""
        return self.context_class()

    def __call__(self, ctx=None):
        """
        This is the entry point to run the app.  It should not be overridden, and instead, just override the run()
        method.

        Args:
            ctx (Context, optional): This is an optional context object. Defaults to None.
        """
        if not ctx:
            ctx = self.ctx
        ctx = self.pre(ctx)
        self.run(ctx)
        self.post()

    def pre(self, ctx):
        """
        A method that runs before the main application.  This an entry point for a Mix-In Class that modifies a context.

        Args:
            ctx (Context): The Context object to use.

        Returns:
            Context: The expected return context object.
        """
        return ctx

    def post(self):
        """
        Called after the main run() method for any necessary cleanup or final steps.  This an entry point for a Mix-In
        Class.
        """
        pass

    def run(self, ctx):
        """Place where business logic is added in a subclassed app.

        Args:
            ctx (Context): Context Object to work with.
        """
        print("I do nothing yet except print my context.")
        print(ctx)
