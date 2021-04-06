
# Auto Accept
CS:GO auto game acceptor.

# How To Download
You can download the latest *compiled* binary from [here](https://github.com/Drew-Alleman/auto-accept/releases).

# FAQ

## Will this get me VAC banned?
No this program doesnt interact with CS:GO's memory.

## It Just Closes/Crashes!
make sure the executable is in the same directory as the image.

## How do I compile the binary myself?
You can download python 3 from [here](https://www.python.org/downloads/).
Go into the directory where the tool is located using the command cd in cmd.
```
pip install -r requirements.txt
```
Or Convert the file into an executable  
```
pip3 install pyinstaller
```
compile the python file to a exe
```
pyinstaller --onefile --icon=C:\PATH_TO_ICON\auto.ico -n autoaccept C:\PATH_TO_PYTHON_FILE\ main.py
```

# To Do
* Hotkey exit
