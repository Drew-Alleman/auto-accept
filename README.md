# auto-accept
CS:GO Auto Game Acceptor.

# How To Download
You can download the latest *compiled* binary from [here](https://github.com/Drew-Alleman/auto-accept/releases).

# FAQ
## Will this get me VAC banned?
No this program doesnt mess with CS:GO's memory

## How do I compile the binary myself?
You can download python 3 from [here](https://www.python.org/downloads/) and install it.
Go into the directory where the tool is located using the command cd in cmd
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

