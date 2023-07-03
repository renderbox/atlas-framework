#!/usr/bin/env python3
from atlas.app import App
from atlas.app.gui import Pyside2Mixin, Pyside2Widget
from PySide2.QtWidgets import QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout


class DemoWidgetOne(Pyside2Widget):
    pass


class SampleGuiApp(Pyside2Mixin, App):

    description = "This is a sample App"

    def add_arguments(self):
        self.add_argument("-s", "--sample", help="A sample CLI argument")
        self.add_argument("-v", "--verbose", action="store_true")

    def run(self, ctx):
        print("Hello All")

    def post_load_ui(self):
        widget = DemoWidgetOne(parent=self.root)
        # self.window.horizontalLayout.addWidget(widget)
        lay = self.root.findChild(QVBoxLayout, "verticalLayout")
        lay.addWidget(widget)

    def connect_signals_and_slots(self):
        self.line = self.root.findChild(QLineEdit, "lineEdit")

        btn = self.root.findChild(QPushButton, "pushButton")
        btn.clicked.connect(self.ok_handler)

    def ok_handler(self):
        language = "None" if not self.line.text() else self.line.text()
        print("Favorite language: {}".format(language))


def main():
    """This the function that instantiates the App Class and runs it.  This is to make it easy to create 'entry points'
    in your pyproject.toml to run command from the command line.
    """
    app = SampleGuiApp()
    app()


if __name__ == "__main__":
    main()
