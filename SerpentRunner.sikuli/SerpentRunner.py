from sikuli import *

import MainMenu
reload(MainMenu)

import BattleMenu
reload(BattleMenu)

import SerpentQuestMenu
reload(SerpentQuestMenu)

import Constants
reload(Constants)

class BotObject(object):
    def __init__(self, region):
        self.region = region
        self.finished = False

        self.constants = Constants.ConstantsManager(self.region)
        self.questMenu = SerpentQuestMenu.SerpentQuestMenu(self)

        self.region.click(self.constants.HOME)

    def run(self):
        r = self.region
        login_screen = r.exists(self.constants.LOGIN, 0)
        if login_screen:
            while not r.exists(self.constants.HOME, 0):
                r.click(self.constants.REGION_TOP)
            r.click(self.constants.HOME)
        if r.exists(self.constants.CONNECT_FAILED, 0):
            r.click(self.constants.CONFIRM)

        self.questMenu.run()

    def selectStrong(self):
        pass