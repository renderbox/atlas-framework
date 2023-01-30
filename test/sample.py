from atlas.app.cli import CLIApp


class SampleApp(CLIApp):
    def add_args(self):
        self.add_arg("-s", "--sample", help="A sample CLI argument")


def main():
    """This the function that instantiates the App Class and runs it.  This is to make it easy to create 'entry points'
    in your pyproject.toml to run command from the command line.
    """
    app = SampleApp()
    app()
