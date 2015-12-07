from sikuli import *

import Constants
reload(Constants)

class BattleMenu(object):
    def __init__(self, botInfo):
        self.botInfo = botInfo

    def do_battles(self):
        if self.botInfo.battlesDone:
            return
        Constants.MENU_BAR.click(Constants.BATTLE)
        if Constants.MAIN_WINDOW.exists(Constants.NEXT):
            Constants.MAIN_WINDOW.click(Constants.NEXT)
        if Constants.MAIN_WINDOW.exists("join_battle.png"):
            Constants.MAIN_WINDOW.wait("join_battle.png")
            Constants.MAIN_WINDOW.click("join_battle.png")
        
        while Constants.MAIN_WINDOW.exists("has_bp.png", 2):
            if self.botInfo.battlesDone:
                return
            while not Constants.MAIN_WINDOW.exists(Pattern("rank_c.png").similar(0.60), .25):
                dragDrop(Constants.REGION_BOT, Constants.REGION_TOP)

            sleep(.25)
            
            self.do_battle()

        Constants.MENU_BAR.click(Constants.HOME)

    def do_battle(self):
        Constants.MAIN_WINDOW.click(Pattern("battle_button.png").similar(0.89))
        sleep(.25)
        Constants.MAIN_WINDOW.wait(Pattern("battle_button.png").similar(0.54))
        if Constants.MAIN_WINDOW.exists("50_wins.png"):
            self.botInfo.battlesDone = True
            return
        Constants.MAIN_WINDOW.click(Pattern("battle_button.png").similar(0.54))
        Constants.MAIN_WINDOW.click("battle_normal.png")
        while (not Constants.MAIN_WINDOW.exists("1449473832450.png")):
            click(Constants.REGION_TOP)
        Constants.MAIN_WINDOW.click("next_battle.png")
        
        Constants.MAIN_WINDOW.wait("battle_bar.png")