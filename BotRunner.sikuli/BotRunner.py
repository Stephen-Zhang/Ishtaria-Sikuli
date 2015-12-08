from sikuli import *

import MainMenu
reload(MainMenu)

import BattleMenu
reload(BattleMenu)

import QuestMenu
reload(QuestMenu)

class BotObject(object):
    def __init__(self):
        self.copiedDeck = False
        self.battlesDone = False
        self.leveledUp = False
        self.finished = False
        
        self.mainMenu = MainMenu.MainMenu(self)
        self.battleMenu = BattleMenu.BattleMenu(self)
        self.questMenu = QuestMenu.QuestMenu(self)

    def run(self):
        while not self.finished:
            self.questMenu.start_quests()
    
    def do_level_up_actions(self):
        self.mainMenu.check()
        self.battleMenu.do_battles()

        # TODO: If at 3000+ crowns, set self.finished.
        # Perform Save of the xml.

    def do_level_5_actions(self):
        # Grab Review Card
        # Set Leader
        # Sell Units
        # Spend Medals
        # Enhance Units
        # Do normal level up actions
        pass
