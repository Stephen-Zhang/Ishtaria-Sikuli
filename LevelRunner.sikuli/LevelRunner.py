from sikuli import *

import MainMenu
reload(MainMenu)

import BattleMenu
reload(BattleMenu)

import LevelQuestMenu
reload(LevelQuestMenu)

import Constants
reload(Constants)

class BotObject(object):
    def __init__(self, region):
        self.region = region
        self.finished = False
        self.strong_unit = 4

        self.constants = Constants.ConstantsManager(self.region)
        self.questMenu = LevelQuestMenu.LevelQuestMenu(self)

        self.region.click(self.constants.HOME)


    def run(self):
        r = self.region
        login_screen = r.exists(self.constants.LOGIN, 0)
        if login_screen:
            while not r.exists(self.constants.HOME, 0):
                low_match = r.exists(self.constants.LOGIN, 0)
                if low_match:
                    r.click(low_match)
                else:
                    r.click(self.constants.REGION_TOP)
            r.click(self.constants.HOME)
        if r.exists(self.constants.CONNECT_FAILED, 0):
            r.click(self.constants.CONFIRM)

        self.questMenu.run()

    def selectStrong(self):
        choices = ("Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5")
        selected = select("Which unit do you want to rush burst with?", options=choices)
        if selected == choices[0]:
            self.strong_unit = 1
        elif selected == choices[1]:
            self.strong_unit = 2
        elif selected == choices[2]:
            self.strong_unit = 3
        elif selected == choices[3]:
            self.strong_unit = 4
        elif selected == choices[4]:
            self.strong_unit = 5
        else:
            self.finished = True