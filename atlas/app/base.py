from ..context import Context
import argparse


class AppBase:


    ctx = None
    argparser = None
    description = "What the program does"
    app_name = "App Base"  # Human Friendly Name, default is class name
    epilog = None

    def init(self, ctx=None, argparser=None):
        if not argparser and not self.argparser:
            self.argparser =

    def create_argparser(self):
        return argparse.ArgumentParser(
            prog=self.app_name,
            description=self.description,
            epilog=self.epilog,
        )

    def add_args(self):
        """Args that need to be included in the app"""
        pass

    def parse_args(self):
        """parse args based on the input"""
        pass

    # Parse Args

    # Create Context
    def set_context(self, args=None):
        if not args:
            args = self.argparser.parse_args()
        self.ctx = Context(args)
        return self.ctx

    def __call__(self, ctx=None):
        self.pre()
        self.run()
        self.post()

    def pre(self, ctx):
        pass

    def post(self):
        pass

    def run(self, ctx):
        pass
