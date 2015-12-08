from sikuli import *

import Constants
reload(Constants)

class QuestMenu(object):
    first_unit = Region(1296,589,117,330)
    second_unit = Region(1420,587,118,333)
    third_unit = Region(1543,587,119,330)
    fourth_unit = Region(1668,588,118,330)
    fifth_unit = Region(1792,588,119,332)
    normal_monsters = [Pattern("savage_tribe.png").similar(0.35),
            Pattern("skeleton.png").similar(0.40),
            Pattern("little_devil.png").similar(0.40),
            Pattern("wolf.png").similar(0.40),
            Pattern("bat.png").similar(0.35),
            Pattern("wizard.png").similar(0.40),
            Pattern("cat.png").similar(0.40),
            Pattern("bee.png").similar(0.40),
           Pattern("frog.png").similar(0.40),
           Pattern("snake.png").similar(0.40)]
    strong_monsters = [Pattern("cerberus.png").similar(0.40)]
    armored_monsters = [Pattern("armor.png").similar(0.40),
            Pattern("crab.png").similar(0.41),
            Pattern("scorpion.png").similar(0.40)]
    boss = [Pattern("purity_boss.png").similar(0.35),
            Pattern("purity_boss_2.png").similar(0.35),
            Pattern("peace_boss_1.png").similar(0.35)]
    def __init__(self, botRunner):
        self.botRunner = botRunner

    def start_quests(self):
        Constants.MAIN_WINDOW.click("quest_icon.png")
        if Constants.MAIN_WINDOW.exists(Constants.SKIP):
            Constants.MAIN_WINDOW.click(Constants.SKIP)
        if Constants.MAIN_WINDOW.exists(Pattern("stronghold_of_peace.png").targetOffset(188,54)):
            Constants.MAIN_WINDOW.click(Pattern("stronghold_of_peace.png").targetOffset(188, 54))
        elif Constants.MAIN_WINDOW.exists(Pattern("ruins_of_purity.png").targetOffset(190,47)):
            Constants.MAIN_WINDOW.click(Pattern("ruins_of_purity.png").targetOffset(197,43))
        self.do_quest()
        
    def do_quest(self):
        Constants.MAIN_WINDOW.click(Constants.SELECT)
        Constants.MAIN_WINDOW.click("deploy.png")

        # TODO: If Out of AP, DRINK POTS
        
        Constants.MAIN_WINDOW.click(Constants.CONFIRM)

        # TODO Find all types of enemies
        while not Constants.MAIN_WINDOW.exists("quest_clear.png"):
            for arm_enemy in self.armored_monsters:
                if exists(arm_enemy):
                    click(arm_enemy)
                    rend_single()
                    break
            for norm_enemy in self.normal_monsters:
                if exists(norm_enemy):
                    click(enemy)
                    norm_aoe()
                    break
            norm_single()

        click(Constants.REGION_TOP)
        if Constants.MAIN_WINDOW.exists("level_up.png"):
            while not Constants.MAIN_WINDOW.exists("finish_quest.png"):
                click(Constants.REGION_TOP)
            self.botRunner.leveledUp = True
            if (Constants.MAIN_WINDOW.exists("level5.png") or
                    Constants.MAIN_WINDOW.exists("level6.png")):
                self.botRunner.do_level_5_actions()
            else:
                self.botRunner.do_level_up_actions()
        else:
            wait("finish_quest.png")
            Constants.MAIN_WINDOW.click(Constants.NEXT)

            # TODO: If End of map, Skip necessary.
       

    def norm_aoe(self):
        click(self.fifth_unit)
        click(self.fourth_unit)
        click(self.third_unit)
        click(self.second_unit)
        click(self.first_unit)

    def rend_aoe(self):
        click(self.first_unit)
        click(self.fourth_unit)
        click(self.fifth_unit)
        click(self.third_unit)
        click(self.second_unit)

    def norm_single(self):
        click(self.second_unit)
        click(self.third_unit)
        click(self.fourth_unit)
        click(self.fifth_unit)
        click(self.first_unit)

    def rend_single(self):
        click(self.first_unit)
        click(self.fifth_unit)
        click(self.second_unit)
        click(self.third_unit)
        click(self.fourth_unit)

    def burst(self):
        # TODO: Write some burst logic revolving around saved leader
        pass
review_notice = "review_notice.png"
play_store_wait = "play_store_wait.png"
back_button = "back_button.png"
ishtaria_icon = "ishtaria_icon.png"
map_clear = "map_clear.png"
