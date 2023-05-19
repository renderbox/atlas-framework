## Making an Installed GUI App with PyInstaller

BTW, if you are going to build a Pyside2 based GUI application using PyInstaller, make sure to include the ".ui" file in the spec file. The first value in the tuple is the path to the .ui file and the second is where to put it as part of the install.

```bash
datas=[('SampleApp.ui','.')],
```
