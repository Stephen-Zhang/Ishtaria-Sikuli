from sikuli import *

import Constants
reload(Constants)

class BattleMenu(object):
    states = [
        'Start',
        'Join'
        'Scroll',
        'Enter',
        'During',
        'End'
    ]
    def __init__(self, botInfo):
        self.botInfo = botInfo
        self.state = 'Start'

    def run(self):
        print(self.state)
        if self.state == 'Start':
            if self.botInfo.battlesDone:
                self.state = 'End'
            self.state = 'Join'
            Constants.MENU_BAR.click(Constants.BATTLE_CHRISTMAS)
        elif self.state == 'Join':
            if Constants.MAIN_WINDOW.exists(Constants.NEXT):
                Constants.MAIN_WINDOW.click(Constants.NEXT)
                return
            elif Constants.MAIN_WINDOW.exists("join_battle.png", .1):
                Constants.MAIN_WINDOW.click("join_battle.png")
            else:
                self.state = 'Scroll'
        elif self.state == 'Scroll':
            if Constants.MAIN_WINDOW.exists("has_bp.png"):
                for i in range(4):
                    dragDrop(Constants.REGION_BOT, Constants.REGION_TOP)
                Constants.MAIN_WINDOW.click(Pattern("battle_button.png").similar(0.89))
                self.state = 'Enter'
            else:
                self.state = 'End'
        elif self.state == 'Enter':
            if Constants.MAIN_WINDOW.exists(Pattern("50_wins.png").similar(0.90)):
                self.botInfo.battlesDone = True
                self.state = 'End'
            else:
                if Constants.MAIN_WINDOW.exists(Pattern("battle_button.png").similar(0.54)):
                    Constants.MAIN_WINDOW.click(Pattern("battle_button.png").similar(0.54))
                    wait(.5)
                    Constants.MAIN_WINDOW.click("battle_normal.png")
                    self.state = 'During'
        elif self.state == 'During':
            if Constants.MAIN_WINDOW.exists("victory_points.png", .1):
                self.state = 'Next'
                Constants.MAIN_WINDOW.click("next_battle.png")
            else:
                click(Constants.REGION_TOP)
        elif self.state == 'Next':
            if Constants.MAIN_WINDOW.exists("battle_bar.png", .1):
                self.state = 'Scroll'
        elif self.state == 'End':
            Constants.MENU_BAR.click(Constants.HOME_CHRISTMAS)
            self.botInfo.state = 'MainMenu'
            self.botInfo.leveledUp = False
            self.botInfo.mainMenu.state = 'Start'