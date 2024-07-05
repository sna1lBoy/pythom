# pythom: a python preprocessor
## installation
a linux executable can be found in the releases section or bundled with the source code

on other operating systems, you can either run the python file or package it along with the ico into an compatible executable using tools like [pyinstaller](https://pypi.org/project/pyinstaller/)

`python3 -m PyInstaller  -F --noconsole --icon=pythom.ico  --onefile pythom.py`

## usage
pass a python file as an argument

if using the executable

`./pythom pythonFile.py`

if using the pythom python file

`python3 pythom.py pythonFile.py`