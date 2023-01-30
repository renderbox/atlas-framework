from atlas.app.cli import CLIApp


class SampleApp(CLIApp):

    description = "This is a sample App"

    def add_arguments(self):
        self.add_argument("-s", "--sample", help="A sample CLI argument")
        self.add_argument("-v", "--verbose", action="store_true")

    def run(self, ctx):
        print("Hello All")


def main():
    """This the function that instantiates the App Class and runs it.  This is to make it easy to create 'entry points'
    in your pyproject.toml to run command from the command line.
    """
    app = SampleApp()
    app()


if __name__ == "__main__":
    main()
