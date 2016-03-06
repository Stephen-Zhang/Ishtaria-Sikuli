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
        join_battle_match = r.exists('join_battle.png', 0)
        if join_battle_match:
            r.click(join_battle_match)
            return
        if self.state == 'Start':
            if self.bot.battlesDone:
                self.state = 'End'
                return
            battle_button_exists = r.exists(self.bot.constants.BATTLE, 0)
            if battle_button_exists:
                self.state = 'Scroll'
                r.click(battle_button_exists)
                return
        elif self.state == 'Scroll':
            if r.exists("battle_select_screen.png", 0):
                if r.exists('has_bp.png', .1):
                    for i in range(4):
                        r.dragDrop(self.bot.constants.REGION_BOT, self.bot.constants.REGION_TOP)
                    next_battle_match = r.exists(Pattern('battle_button.png').similar(0.89), 0)
                    if next_battle_match:
                        r.click(next_battle_match)
                        r.waitVanish("battle_select_screen.png")
                        self.state = 'Enter'
                        return
                else:
                    self.state = 'End'
        elif self.state == 'Enter':
            if r.exists(Pattern('50_wins.png').similar(0.95), 0):
                self.bot.battlesDone = True
                self.state = 'End'
            else:
                fancy_battle_match = r.exists('battle_normal.png', 0)
                if fancy_battle_match:
                    r.click(fancy_battle_match)
                    self.state = 'During'
                    return
                last_battle_match = r.exists(Pattern('battle_button.png').similar(0.54), 0)
                if last_battle_match:
                    r.click(last_battle_match)
        elif self.state == 'During':
            if r.exists('victory_points.png', 0):
                next_match = r.exists(Pattern('next_battle.png').similar(.8), 0)
                if next_match:
                    r.click(next_match)
                    self.state = 'Next'
            else:
                r.click(self.bot.constants.REGION_TOP)
        elif self.state == 'Next':
            if r.exists('battle_bar.png', 0):
                self.state = 'Scroll'
        elif self.state == 'End':
            home_match = r.exists(self.bot.constants.HOME_CHRISTMAS, 0)
            if home_match:
                r.click(home_match)
                self.bot.state = 'MainMenu'
                self.bot.leveledUp = False
                self.bot.mainMenu.state = 'Start'