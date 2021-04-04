from datetime import datetime
import pyautogui
import time
import os

cwd = os.getcwd()
screenWidth, screenHeight = pyautogui.size()

banner = '''
             _                                       _    
  __ _ _   _| |_ ___         __ _  ___ ___ ___ _ __ | |_  
 / _` | | | | __/ _ \ _____ / _` |/ __/ __/ _ \ '_ \| __| 
| (_| | |_| | || (_) |_____| (_| | (_| (_|  __/ |_) | |_  
 \__,_|\__,_|\__\___/       \__,_|\___\___\___| .__/ \__| 
       Coded by Drew Alleman                  |_|         
'''

imageNames = ['readyButtonNormal.png','acceptButton.png']

def printInfo(msg):
    now = datetime.now()
    prettyTime = now.strftime('[%H:%M:%S] ')
    print(prettyTime + msg)

def clickButton():
    for image in imageNames:
        readyButton = pyautogui.locateCenterOnScreen(cwd+'\\'+image,grayscale=True,confidence=0.9)
        if readyButton is not None: # If readyButton is found
            readyButtonX, readyButtonY = readyButton
            pyautogui.click(readyButtonX, readyButtonY)
            return True
        return False

def mainLoop():
    printInfo('Press CTRL+C in this program to stop it.')
    while True:
        try:
            result = clickButton()
            if result:
                printInfo('Starting Game!')
            time.sleep(7)
        except KeyboardInterrupt:
            exit()

if __name__ == '__main__':
    print(banner)
    mainLoop()