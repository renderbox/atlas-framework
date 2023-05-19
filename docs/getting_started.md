# Getting Started

This is a simple "How To" doc that takes you through the basics of setting up your application with the Atlas Framework.

## Example

### Installation

Before you can do anything, make sure you import the package into your environment:

```bash
> pip install atlas
```

> NOTE: It is highly reconmended to develop with a Python Virtual Environment when possible.

### The Sample App

You can run the sample app by copying the code below and putting it in a file called `sample_app.py`.

```python
from atlas.app import App


class SampleApp(App):

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

You can run it just by calling it with the python interpreter.

```bash
> python sample_app.py
```

If everything worked as expected you should see a message in the command prompt that says "Hello All".

## Code Breakdown

To help make this clear to understand let's break down what is going on. This first step is very common in Python code and imports the app class to inherit from. In this case it's the App class.

```python
from atlas.app import App
```

Using the principle of code inheritence, the next thing we do is subclass the App class to make our own App. Every app using the Atlas Framework is based on the App class. It provides the core features and structure in which to write our apps. Other features (such as GUIs) are added as Mixin Classes (which we will get into later) but for now we will stick with the basic CLI foundation.

```python
class SampleApp(App):
    pass
```

If we just run this, we will get the default output (which is to print our execution context to the screen). This is good to show that it works but it's not a useful app yet. Let's try to give it something more to do.

Right now our app does not have any command line arguments. These arguments allow us provide information to the application when we launch it. They can be input values or simply switches that change it's behavior to how we want it to work. In the example we replaced the `pass` placeholder with the following.

```python
    def add_arguments(self):
        self.add_argument("-s", "--sample", help="A sample CLI argument")
        self.add_argument("-v", "--verbose", action="store_true")
```

By adding (technically overriding) the `add_arguments()` method we provide a method to add our own arguments to our app. The framework uses the same syntax as Python's ArgParse library so there is a lot of documentation on the format available. If you run the app again, you will now notice that the context output shows two more keys, "sample" and "verbose".

If we want to see the help documentation for our app, we simply add the standard `-h` to the command when we run it.

Atlas' goal is to try to keep you focused on the business logic so the next thing to do is add some business logic to our app by adding a `run()` method. This is where _your_ app's unique business logic goes. In the example we just present you with a nice greeting.

```python
    def run(self, ctx):
        print("Hello All")
```

That is pretty easy. Inside the run() method we have access to the context in which we are executing our code. The Context() object (ctx) is an extended dictionary that provides your app with a bunch of relevent information. It is a compilation of a configuation file, the environment, and command line arguments into a single context with each overriding the values in an order of importance. So values in a configuation file are overwritten by environment variables which are then overridden by command line arguments. If you want to access the different original data sources for any reason, they are all still available as part the context object as well.

That's how we write an app. Now lets see a way to make it run.

## Making the app available on the Command Line

The last two parts of te example show how you can launch your app.

```python
if __name__ == "__main__":
    main()
```

These lines at the end will run the function `main()` if it's in the first file the Python interpreter loads, aka the entry point.

This works for demonstration purposes but it's not a very intuitive way to do things. It requires typing on the command line a long string that does not look like our app (`python test/sample.py -s "bob"` for example). We want something cleaner than that like `sample_app -s "bob"`.

To make this available as a command line app we will leverage a convention used when packaging our project. In setup.py they are called "entry_points" and in `pyproject.toml` they are called 'project.scripts'. We follow the `pyproject.toml` aproach since, in addition to being more secure, it's the reconmended way from the PSF (Python Software Foundation).

The first step is to create a function we can call.

```python
def main():
    """This the function that instantiates the App Class and runs it.  This is to make it easy to create 'project.scripts' in your pyproject.toml to run command from the command line.
    """
    app = SampleApp()
    app()
```

We defined a function called `main()` that creates and instance of our App Class and then calls it. With the main() function defined we need to tell our package config about it and how to use it

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

In both cases you will notice it's the name of the CLI app `sample_app` followed by `=` and then the import path to the module (`test.sample`), followed by a `:` and the method to call (`main`). The advantage of this aproach is when you install the package it will link the script to work on your command line shell, regardless of being on Linux, MacOS or Windows.

Next Step -> [Pyside2 GUI App](pyside2app.md)
