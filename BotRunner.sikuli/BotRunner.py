from sikuli import *

import MainMenu
reload(MainMenu)

import BattleMenu
reload(BattleMenu)

class BotObject(object):
    def __init__(self):
        self.current_level = 0
        self.copiedDeck = False
        self.battlesDone = False
        
        self.mainMenu = MainMenu.MainMenu(self)
        self.battleMenu = BattleMenu.BattleMenu(self)

    def run(self):
        self.mainMenu.check()

        sleep(5)
        self.mainMenu.battle_open()

    def perform_level_up_actions(self):
        self.do_battles