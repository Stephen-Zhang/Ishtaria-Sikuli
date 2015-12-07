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

        while Constants.MAIN_WINDOW.exists("has_bp.png", .25):
            if self.botInfo.battlesDone:
                return
            while not Constants.MAIN_WINDOW.exists(Pattern("rank_c.png").similar(0.50), .25):
                dragDrop(Constants.REGION_BOT, Constants.REGION_TOP)

            sleep(.25)
            
            self.do_battle()

    def do_battle(self):
        click(Pattern("battle.png").similar(0.89))
        sleep(.25)
        Constants.MAIN_WINDOW.wait("battle.png")
        if Constants.MAIN_WINDOW.exists("50_wins.png"):
            self.botInfo.battlesDone = True
            return
        Constants.MAIN_WINDOW.click("battle.png")
        Constants.MAIN_WINDOW.click("battle_normal.png")
        while (not Constants.MAIN_WINDOW.exists("win_battle.png") or
                not Constants.MAIN_WINDOW.exists(Pattern("1449466155066.png").similar(0.40))):
            click(Constants.REGION_TOP)

        click(Constants.REGION_BOT)
        Constants.MAIN_WINDOW.wait("next_battle.png")
        Constants.MAIN_WINDOW.click("next_battle.png")
        
        Constants.MAIN_WINDOW.wait("battle_bar.png")