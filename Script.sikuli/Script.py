myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)

import time

import BotRunner
reload(BotRunner)

def main():
    bot = BotRunner.BotObject()

    bot.battleMenu.do_battle();
    
    while(True):
        if exists("sikuli_stop.png"):
            break
        # bot.run()

if __name__ == "__main__":
    Settings.MinSimilarity = .95
    setFindFailedResponse(SKIP)
    main()