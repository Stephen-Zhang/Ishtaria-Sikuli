myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)

import BotRunner
reload(BotRunner)

import Constants
reload(Constants)

def main():
    while not exists("sikuli_stop.png", .25):
        bot = BotRunner.BotObject()
        bot.battleMenu.do_battles()

        return
        # bot.run()
        
        # Save File. The Cycle begins again.

if __name__ == "__main__":
    Settings.MinSimilarity = .95
    setFindFailedResponse(SKIP)
    main()