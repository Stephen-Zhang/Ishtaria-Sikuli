"""
Pictures To Move:
"join_battle.png"
battle_select_screen.png
has_bp.png
battle_button.png

"""

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
        self.bot = botInfo
        self.state = 'Start'

    def run(self):
        r = self.bot.region
        print(self.state)
        next_exists = r.exists(self.bot.constants.NEXT, 0)
        if next_exists:
            r.click(next_exists)
            return
        join_battle_match = r.exists(self.bot.constants.JOIN_BATTLE, 0)
        if join_battle_match:
            r.click(join_battle_match)
            return
        if self.state == 'Start':
            if self.bot.battlesDone:
                self.state = 'End'
                return
            battle_button_exists = r.exists(self.bot.constants.BATTLE_MENU, 0)
            if battle_button_exists:
                self.state = 'Scroll'
                r.click(battle_button_exists)
                return
        elif self.state == 'Scroll':
            if r.exists(self.bot.constants.BATTLE_SELECT, 0):
                if r.exists(self.bot.constants.HAS_BP, .1):
                    for i in range(4):
                        r.dragDrop(self.bot.constants.REGION_BOT, self.bot.constants.REGION_TOP)
                    next_battle_match = r.exists(self.bot.constants.BATTLE_BUTTON_SMALL, 0)
                    if next_battle_match:
                        r.click(next_battle_match)
                        r.waitVanish(self.bot.constants.BATTLE_SELECT)
                        self.state = 'Enter'
                        return
                else:
                    self.state = 'End'
        elif self.state == 'Enter':
            if r.exists(self.bot.constants.WINS_MET, 0):
                self.bot.battlesDone = True
                self.state = 'End'
            else:
                normal_battle_match = r.exists(self.bot.constants.BATTLE_NORMAL, 0)
                if normal_battle_match:
                    r.click(normal_battle_match)
                    self.state = 'During'
                    return
                last_battle_match = r.exists(self.bot.constants.BATTLE_BUTTON_BIG, 0)
                if last_battle_match:
                    r.click(last_battle_match)
        elif self.state == 'During':
            if r.exists(self.bot.constants.VICTORY_POINTS, 0):
                next_match = r.exists(self.bot.constants.NEXT_BATTLE, 0)
                if next_match:
                    r.click(next_match)
                    self.state = 'Next'
            else:
                r.click(self.bot.constants.REGION_TOP)
        elif self.state == 'Next':
            if r.exists(self.bot.constants.BATTLE_BAR, 0):
                self.state = 'Scroll'
        elif self.state == 'End':
            home_match = r.exists(self.bot.constants.HOME_CHRISTMAS, 0)
            if home_match:
                r.click(home_match)
                self.bot.state = 'MainMenu'
                self.bot.leveledUp = False
                self.bot.mainMenu.state = 'Start'