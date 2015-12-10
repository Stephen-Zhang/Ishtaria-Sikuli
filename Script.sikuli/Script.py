myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)

import BotRunner
reload(BotRunner)

import Constants
reload(Constants)

def main():
    bot = BotRunner.BotObject()
        
    while not(exists("sikuli_stop.png", .25) or bot.state == 'Finished'):
        bot.run()
        
    # Save File. The Cycle begins again.

if __name__ == "__main__":
    Settings.MinSimilarity = .95
    setFindFailedResponse(SKIP)
    main()