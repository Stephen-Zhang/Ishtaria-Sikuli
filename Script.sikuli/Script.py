import os
from sikuli.Sikuli import *

myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)

import BotRunner
reload(BotRunner)

import LevelRunner
reload(LevelRunner)

import HopeRunner
reload(HopeRunner)

import SerpentRunner
reload(SerpentRunner)

def main():
    bluestacks = App.focus('BlueStacks App Player')
    region = Region(App.focusedWindow())

    bot = None

    bot_options = ('3k Crowns', 'Level To 50', 'Deftwo', 'Deftevent')
    selected = select('What do you want to do?', options=bot_options)
    if selected == bot_options[0]:
        bot = BotRunner.BotObject(region)
    elif selected == bot_options[1]:
        bot = LevelRunner.BotObject(region)
    elif selected == bot_options[2]:
        bot = HopeRunner.BotObject(region)
    elif selected == bot_options[3]:
        bot = SerpentRunner.BotObject(region)
    else:
        return

    bot.selectStrong()
    
    while not bot.finished:
        bot.run()
    
if __name__ == "__main__":
    Settings.MinSimilarity = .95
    Settings.WaitScanRate = 20
    setFindFailedResponse(SKIP)
    main()