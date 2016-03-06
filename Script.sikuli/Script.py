import os
from sikuli.Sikuli import *

myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)

import BotRunner
reload(BotRunner)

def main():
    bluestacks = App.focus('BlueStacks App Player')
    region = Region(App.focusedWindow())
    print region
    bot = BotRunner.BotObject(region)
    
    while bot.state != 'Finished':
        bot.run()
    
if __name__ == "__main__":
    Settings.MinSimilarity = .95
    Settings.WaitScanRate = 20
    setFindFailedResponse(SKIP)
    main()