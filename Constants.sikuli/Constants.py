from sikuli import *

class ConstantsManager(object):
    def __init__(self, region):
        self.region = region

        self.init_main_buttons()
        self.init_regions()
        self.init_login_images()
        self.init_battle_menu_images()
        self.init_quest_map_images()
        self.init_quest_menu_images()
        self.init_leveling_images()

    def init_main_buttons(self):
        self.HOME = "HOME.png"
        self.BATTLE_MENU = "BATTLE.png"
        self.CONFIRM = "CONFIRM.png"
        self.CLOSE = "CLOSE.png"
        self.NEXT = "NEXT.png"
        self.SELECT = "SELECT.png"
        self.SKIP = "SKIP.png"

    def init_regions(self):
        self.REGION_TOP = self.create_click_region(.5, .19)
        self.REGION_BOT = self.create_click_region(.5, .65)

    def init_login_images(self):
        self.LOGIN = Pattern("LOGIN.png").similar(0.50)
        self.CONNECT_FAILED = "CONNECT_FAILED.png"

    def init_battle_menu_images(self):
        self.JOIN_BATTLE = "JOIN_BATTLE.png"
        self.BATTLE_SELECT = "BATTLE_SELECT.png"
        self.HAS_BP = "HAS_BP.png"
        self.BATTLE_BUTTON_SMALL = Pattern("BATTLE_BUTTON_SMALL.png").similar(0.89)
        self.BATTLE_BUTTON_BIG = "BATTLE_BUTTON_BIG.png"
        self.WINS_MET = Pattern("WINS_MET.png").similar(0.95)
        self.BATTLE_NORMAL = "BATTLE_NORMAL.png"
        self.VICTORY_POINTS = "VICTORY_POINTS.png"
        self.NEXT_BATTLE = Pattern("NEXT_BATTLE.png").similar(0.80)
        self.BATTLE_BAR = "BATTLE_BAR.png"

    def init_quest_map_images(self):
        self.QUEST_MENU = "QUEST_MENU.png"
        self.DUNE = Pattern("WESTERN_WIND_DUNES.png").targetOffset(194,50)
        self.DEN = Pattern("DEN_OF_THE_DRAGON.png").targetOffset(191,2)
        self.CAVE = Pattern("CAVE_OF_TEMPTATION.png").targetOffset(195,16)
        self.PRIDE = Pattern("PRIDE_OF_THE_GRYFFIN.png").targetOffset(186,-8)
        self.LAIR = Pattern("THE_LAIR_OF_FIRE.png").targetOffset(181,2)
        self.TOWER = Pattern("STRONGHOLD_OF_PEACE.png").targetOffset(187,-5)
        self.RUINS = Pattern("RUINS_OF_PURITY.png").targetOffset(190,-9)

    def init_quest_menu_images(self):
        self.enemy_similarity = .8
        self.MINI_POT = Pattern("MINI_POT.png").targetOffset(196,9)
        self.DEPLOY = "DEPLOY.png"
        self.QUEST_CLEAR = Pattern("QUEST_CLEAR.png").similar(0.90)        
        self.QUEST_END = Pattern("QUEST_END.png").similar(0.90)
        self.BACK = Pattern("back.png").similar(0.95)
        self.ATTACK = "ATTACK.png"
        self.BURST = "BURST.png"
        self.LEVEL_UP = "LEVEL_UP.png"
        self.ENEMY_APPEARS = Pattern("ENEMY_APPEARS.png").similar(0.50)
        self.RAID_AREA = "RAID_AREA.png"
        self.RAID_BANNER = "RAID_BANNER.png"

    def init_leveling_images(self):
        self.STANDING_IN_WAY_2 = Pattern("STANDING_IN_WAY_2.png").targetOffset(196,74)
        self.ALL_OUT_ATTACK = "ALL_OUT_ATTACK.png"

    def create_click_region(self, x_mod, y_mod):
        width = self.region.getW()
        height = self.region.getH()
        x = self.region.getX()
        y = self.region.getY()

        return Region(int(x + width * x_mod), int(y + height * y_mod), 2, 2)
