from sikuli import *

import MainMenu
reload(MainMenu)

import BattleMenu
reload(BattleMenu)

import QuestMenu
reload(QuestMenu)

import Constants
reload(Constants)

class BotObject(object):
    states = [
        'MainMenu',
        'Battle',
        'Quest'
    ]

    def __init__(self):
        self.copiedDeck = False
        self.battlesDone = False
        self.leveledUp = False
        self.finished = False

        self.state = 'Battle' # Start as Quest

        self.mainMenu = MainMenu.MainMenu(self)
        self.battleMenu = BattleMenu.BattleMenu(self)
        self.questMenu = QuestMenu.QuestMenu(self)

    def run(self):
        if Constants.MAIN_WINDOW.exists("3k_crowns.png", .25):
            self.state = 'Finished'
        if self.state == 'MainMenu':
            self.mainMenu.run()
        if self.state == 'Battle':
            self.battleMenu.run()
        if self.state == 'Quest':
            self.questMenu.run()

    def do_level_up_actions(self):
        self.mainMenu.check()
        self.battleMenu.do_battles()

        if Constants.MAIN_WINDOW.exists("3k_crowns.png", .25):
            self.finished = True

        click(Constants.HOME)

        # Perform Save of the xml.

    def do_level_5_actions(self):
        # Grab Review Card
        # Set Leader
        # Sell Units
        # Spend Medals
        # Enhance Units
        # Do normal level up actions
        pass
