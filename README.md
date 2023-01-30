# Atlas App Framework

This is a simple framework for creating Class based applications that can be run as a command line application or importated and run as a module. It's goal is to remove a lot of boiler plate that is typically done when writting CLI and GUI apps.

## Example

Here is a simple CLI app to show how this all works.

```python
from atlas.app.cli import CLIApp


class SampleApp(CLIApp):

    description = "This is a sample App"

    def add_arguments(self):
        self.add_argument("-s", "--sample", help="A sample CLI argument")
        self.add_argument("-v", "--verbose", action="store_true")

    def run(self, ctx):
        print("Hello All")


def main():
    """This the function that instantiates the App Class and runs it.  This is to make it easy to create 'project.scripts'
    in your pyproject.toml to run command from the command line.
    """
    app = SampleApp()
    app()


if __name__ == "__main__":
    main()
```

This first step imports the app class to inherit from. In this case it's the CLIApp class.

```python
from atlas.app.cli import CLIApp
```

The next thing we do is subclass the base app class (CLIApp) to make our own App Class.

```python
class SampleApp(CLIApp):
    pass
```

If we just run this, we will get the default output (which is to print our execution context to the screen). This is good to show that it works but it's not what we really want to do.

Right now our app does not have any command line arguments so we need to add some.

```python
    def add_arguments(self):
        self.add_argument("-s", "--sample", help="A sample CLI argument")
        self.add_argument("-v", "--verbose", action="store_true")
```

By overriding the `add_arguments()` method we add our arguments in there one at a time. It's the same syntax as Python's ArgParse library so there is a lot of documentation on the format available. If you run the app again, you will now notice that the context output shows two more keys, "sample" and "verbose".

The next thing to do is add some business logic to our app by overriding the `run()` method. In the example it's this:

```python
    def run(self, ctx):
        print("Hello All")
```

That is pretty easy. Inside the run() method we have access to the context in which we are executing our code. The Context() object (ctx) is an advanced dictionary that brings together a bunch of pieces of data from a configuation file, the environment, and command line arguments into a single context with each overriding the values from the prior. So anything set in a configuation file is overwritten by environment variables which are then overridden by command line arguments.

That's the basic use of the framework.

## Making the app available on the Command Line

The last two parts of te example show how you can launch your app.

```python
if __name__ == "__main__":
    main()
```

The last part here is a traditional way where Python will run the function `main()` if it's in the first file the Python interpreter loads. This works for demonstration purposes but it's not a very intuitive way to do things. It requires typing on the command line a long string that does not look like our app (`python test/sample.py -s "bob"` for example). We want something cleaner than that like `sample_app -s "bob"`.

To do this we will leverage a convention used when packaging our app. In setup.py they are called "entry_points" and in pyproject.toml they are called 'project.scripts'.

The first step is with this:

```python
def main():
    """This the function that instantiates the App Class and runs it.  This is to make it easy to create 'project.scripts'
    in your pyproject.toml to run command from the command line.
    """
    app = SampleApp()
    app()
```

We define a function called `main()` that instatiates our App Class and then calls it. With the main() function defines, in our pyproject.toml we add this to our code.

```toml
[project.scripts]
sample_app = "test.sample:main"
```

...and for setup.py (the older, deprecated way) it looks like this:

```python
setup(
    # ...,
    entry_points={
        'console_scripts': [
            'sample_app = test.sample:main',
        ]
    }
)
```

In both cases you will notice it's the name of the CLI app `sample_app` followed by `=` and then the import path to the module (`test.sample`), followed by a `:` and the method to call (`main`). When you install the package it will also link the executeable to work in your command line shell on Linux, MacOS and Windows.
