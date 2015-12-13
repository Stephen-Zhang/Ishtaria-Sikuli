import os
from sikuli.Sikuli import *

myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)

import BotRunner
reload(BotRunner)

import Constants
reload(Constants)

import Images
reload(Images)

def main():
    #bluestacks = App("BlueStacks App Player")
    #bluestacks.focus()
    #app_region = bluestacks.window()
    #while not exists("sikuli_stop.png", .25):
    bot = BotRunner.BotObject()
    while bot.state != 'Finished':
        bot.run()
    
if __name__ == "__main__":
    Settings.MinSimilarity = .95
    Settings.WaitScanRate = 2
    setFindFailedResponse(SKIP)
    main()