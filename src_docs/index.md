# Atlas App Framework

## Philosophy

The Atlas App Framework was built out of over 15 years of Python experience developing apps for special use and across many different large scale Feature VFX and Animation Production pipelines, where the sheer amount of data is extremely high, integrations with 3rd parties is a constant and the end product needs to just be robust, but simply never fail.

Out of this the need for a standard way for TDs and Engineers to develop dependable, ready for production apps very quickly

The framework has a couple core elements to it's design:

- **Pure Standard Python** - The framework should be as free from external dependencies as possible. To meet this goal, the base of Atlas (for making CLI apps) has no external dependencies. The library only brings in what is needed (such as Pyside2 for GUIs) and the rest is up to you.
- **The App Class _is_ the Boilerplate** - You should avoid re-writting boilerplate whenever possible. Boilerplate code should be kept as consistent & stable as possible so it's DRY, robust and dependable.
- **Stay Focused On Business Logic** - Since Atlas takes care of the boilerplate, you are free to focus on the logic you need to implement.
- **Apps are _Classes_** - App classes themselves can be imported and used inside of other App classes or within other applications that support it (Maya, etc). This maximizes the code usage with DRY principles and lets you adapt the tool for the context it is written in.
- **Mixins as Feature Plugins** - If a highly reuseable feature is created (like adding a Pyside2 GUI), it should be added to your class using the mixin pattern. This extends what makes up the _boilerplate_ foundation for your app with something that is thuroughly tested and ready for use.

With that in mind, lets get to the next step, Getting Started.

## Getting Started

If this is your fist time here, check out the [Getting Started](getting_started.md) page to understand how to build something quickly with the Atlas App Framework.

## Pyside2 GUI App

Here is where you can extend your learning and create Pyside2 GUI based apps: [PySide2 GUI Apps](pyside2app.md).

## Installed App

Here is where you can find the docs on how to make your app installable: [Installed Apps](installed_app.md).

## API

If you are already familiar with the framework, here are the [API](api.md) docs to help you dive a little furhter in.

## Change Notes

[Change Notes](change_notes.md) are available here.

## Want to help?

I am always open to people interested in helping make this an even more capable and robust project. If you are interested in helping, just add a support ticket and we will connect.
