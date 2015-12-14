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
    '''
    while True:
        matched = findAll()
        if matched:
            for match in matched:
                match.highlight(True)
    return
    '''
    
    bot = BotRunner.BotObject()
    
    while bot.state != 'Finished':
        bot.run()
    
if __name__ == "__main__":
    Settings.MinSimilarity = .90
    Settings.WaitScanRate = 10
    setFindFailedResponse(SKIP)
    main()