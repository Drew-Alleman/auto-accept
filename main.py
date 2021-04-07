from datetime import datetime # Module for getting time
import pyautogui # For clicking and finding the image
import time # For sleeping
import os # For getting current directory

cwd = os.getcwd() # Get current working directory
version = "0.1.0" # Current version


banner = '''
             _                                       _    
  __ _ _   _| |_ ___         __ _  ___ ___ ___ _ __ | |_  
 / _` | | | | __/ _ \ _____ / _` |/ __/ __/ _ \ '_ \| __| 
| (_| | |_| | || (_) |_____| (_| | (_| (_|  __/ |_) | |_  
 \__,_|\__,_|\__\___/       \__,_|\___\___\___| .__/ \__| 
       Coded by Drew Alleman:{}            |_|         
'''.format(version) # Bannner message


def printFunc(msg): # Print function format: [<time>] message
    now = datetime.now() # Get time
    prettyTime = now.strftime('[%H:%M:%S] ') # Format time
    print(prettyTime + msg) # Print message

def clickButton():
    try:
        readyButton = pyautogui.locateCenterOnScreen(cwd+'\\1.png',grayscale=True,confidence=0.8) # Look for image
    except IOError: # If file not found
        printFunc('File: 1.png was not found! Make sure the image is in the SAME directory as the exe/python file!')
        exit() # Exit
    if readyButton is not None: # If readyButton is found
        readyButtonX, readyButtonY = readyButton # Define cords
        pyautogui.click(readyButtonX, readyButtonY) # Click cords
        return True # It worked!
    return False # It didnt :(

def mainLoop():
    printFunc('Press CTRL+C in this program to stop it.') # Print message/warning
    while True: # Loop Forever
        try: # Try
            result = clickButton() # Run func clickButton() and store result in variable 'result'
            if result: # if result == True
                printFunc('Starting game!') # print [<time>] Starting game!
            time.sleep(5) # Sleep for 5 seconds
        except KeyboardInterrupt: # Except CTRL+C
            exit() # Then exit

if __name__ == '__main__':
    print(banner) # Print banner
    mainLoop() # Run main loop
