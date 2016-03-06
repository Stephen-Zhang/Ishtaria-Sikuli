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
    def __init__(self, region):
        self.region = region
        self.battlesDone = False
        self.leveledUp = True
        self.finished = False
        self.strong_unit = 4

        self.state = 'Battle'

        self.constants = Constants.ConstantsManager(self.region)
        self.mainMenu = MainMenu.MainMenu(self)
        self.battleMenu = BattleMenu.BattleMenu(self)
        self.questMenu = QuestMenu.QuestMenu(self)

    def run(self):
        r = self.region
        login_screen = r.exists(self.constants.LOGIN, 0)
        if login_screen:
            while not r.exists(self.constants.HOME_CHRISTMAS, 0):
                r.click(self.constants.REGION_TOP)
            r.click(self.constants.HOME_CHRISTMAS)
        if r.exists(self.constants.CONNECT_FAILED, 0):
            r.click(self.constants.CONFIRM)
        if self.state == 'MainMenu':
            self.mainMenu.run()
        if self.state == 'Battle':
            self.battleMenu.run()
        if self.state == 'Quest':
            self.questMenu.run()

    def selectStrong(self):
        choices = (1, 2, 4)
        selected = select("Which unit is your strongest unit?", choices)
        if selected == choices[0]:
            self.strong_unit = 1
        elif selected == choices[1]:
            self.strong_unit = 2
        elif selected == choices[2]:
            self.strong_unit = 4