from sikuli import *

import Constants
reload(Constants)

class MainMenu(object):
    states = [
        'Start',
        'CollectStart',
        'MailCollect',
        'ChallengesCollect',
        'ChallengesCollect',
        'End'
    ]

    def __init__(self, botInfo):
        self.botInfo = botInfo
        self.state = 'Start'

    def run(self):
        print self.state
        if self.state == 'Start':
            self.state = 'End'
        elif self.state == 'End':
            self.state = 'Start'
            self.botInfo.leveledUp = False
            self.botInfo.state = 'Quest'
            self.botInfo.questMenu.state = 'Start'
