from sikuli import *

import Constants
reload(Constants)

class BattleMenu(object):
    states = [
        'Start',
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
        next_exists = Constants.MAIN_WINDOW.exists(Constants.NEXT, 0)
        if next_exists:
            Constants.MAIN_WINDOW.click(next_exists)
            return
        join_battle_match = Constants.MAIN_WINDOW.exists('join_battle.png', 0)
        if join_battle_match:
            Constants.MAIN_WINDOW.click(join_battle_match)
            return
        if self.state == 'Start':
            if self.botInfo.battlesDone:
                self.state = 'End'
                return
            battle_button_exists = Constants.MENU_BAR.exists(Constants.BATTLE_CHRISTMAS, 0)
            if battle_button_exists:
                self.state = 'Scroll'
                Constants.MENU_BAR.click(battle_button_exists)
                return
        elif self.state == 'Scroll':
            if Constants.MAIN_WINDOW.exists("battle_select_screen.png", 0):
                if Constants.MAIN_WINDOW.exists('has_bp.png', .1):
                    for i in range(4):
                        dragDrop(Constants.REGION_BOT, Constants.REGION_TOP)
                    next_battle_match = Constants.MAIN_WINDOW.exists(Pattern('battle_button.png').similar(0.89), 0)
                    if next_battle_match:
                        Constants.MAIN_WINDOW.click(next_battle_match)
                        Constants.MAIN_WINDOW.waitVanish("battle_select_screen.png")
                        self.state = 'Enter'
                        return
                else:
                    self.state = 'End'
        elif self.state == 'Enter':
            if Constants.MAIN_WINDOW.exists(Pattern('50_wins.png').similar(0.95), 0):
                self.botInfo.battlesDone = True
                self.state = 'End'
            else:
                fancy_battle_match = Constants.MAIN_WINDOW.exists('battle_normal.png', 0)
                if fancy_battle_match:
                    Constants.MAIN_WINDOW.click(fancy_battle_match)
                    self.state = 'During'
                    return
                last_battle_match = Constants.MAIN_WINDOW.exists(Pattern('battle_button.png').similar(0.54), 0)
                if last_battle_match:
                    Constants.MAIN_WINDOW.click(last_battle_match)
        elif self.state == 'During':
            if Constants.MAIN_WINDOW.exists('victory_points.png', 0):
                next_match = Constants.MAIN_WINDOW.exists(Pattern('next_battle.png').similar(.8), 0)
                if next_match:
                    Constants.MAIN_WINDOW.click(next_match)
                    self.state = 'Next'
            else:
                Constants.MAIN_WINDOW.click(Constants.REGION_TOP)
        elif self.state == 'Next':
            if Constants.MAIN_WINDOW.exists('battle_bar.png', 0):
                self.state = 'Scroll'
        elif self.state == 'End':
            home_match = Constants.MENU_BAR.exists(Constants.HOME_CHRISTMAS, 0)
            if home_match:
                Constants.MENU_BAR.click(home_match)
                self.botInfo.state = 'MainMenu'
                self.botInfo.leveledUp = False
                self.botInfo.mainMenu.state = 'Start'