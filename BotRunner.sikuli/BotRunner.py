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
        self.leveledUp = True
        self.finished = False

        self.state = 'Battle'

        self.mainMenu = MainMenu.MainMenu(self)
        self.battleMenu = BattleMenu.BattleMenu(self)
        self.questMenu = QuestMenu.QuestMenu(self)

    def run(self):
        login_screen = Constants.FULL_SCREEN.exists(Pattern('login.png').similar(0.50), .25)
        if login_screen:
            while not Constants.MENU_BAR.exists(Constants.HOME_CHRISTMAS, 0):
                Constants.FULL_SCREEN.click(Constants.REGION_TOP)
            Constants.MENU_BAR.click(Constants.HOME_CHRISTMAS)
        if Constants.FULL_SCREEN.exists("Connect_failed.png", 0):
            Constants.MAIN_WINDOW.click(Constants.CONFIRM)
        if self.state == 'MainMenu':
            self.mainMenu.run()
        if self.state == 'Battle':
            self.battleMenu.run()
        if self.state == 'Quest':
            self.questMenu.run()
