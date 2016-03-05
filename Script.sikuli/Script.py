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
    bot = BotRunner.BotObject()
    
    #'''
    bot.state = 'Quest'
    bot.questMenu.currentMap = Images.Map3()
    bot.questMenu.state = 'Waiting'
    #'''
    
    while bot.state != 'Finished':
        bot.run()
    
if __name__ == "__main__":
    Settings.MinSimilarity = .95
    Settings.WaitScanRate = 20
    setFindFailedResponse(SKIP)
    main()