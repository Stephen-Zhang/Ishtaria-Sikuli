from sikuli import *

import Constants
reload(Constants)

class QuestMenu(object):
    first_unit = Region(1296,589,117,330)
    second_unit = Region(1420,587,118,333)
    third_unit = Region(1543,587,119,330)
    fourth_unit = Region(1668,588,118,330)
    fifth_unit = Region(1792,588,119,332)
    attack = "attack.png"
    normal_monsters = [Pattern("savage_tribe.png").similar(0.50),
                       Pattern("skeleton.png").similar(0.50),
                       Pattern("little_devil.png").similar(0.50),
                       Pattern("wolf.png").similar(0.50),
                       Pattern("bat.png").similar(0.50),
                       Pattern("wizard.png").similar(0.50),
                       Pattern("cat.png").similar(0.50),
                       Pattern("bee.png").similar(0.50),
                       Pattern("frog.png").similar(0.50),
                       Pattern("snake.png").similar(0.50)]
    strong_monsters = [Pattern("cerberus.png").similar(0.50)]
    armored_monsters = [Pattern("armor.png").similar(0.50), Pattern("crab.png").similar(0.50), Pattern("scorpion.png").similar(0.50)]
    boss = [Pattern("purity_boss.png").similar(0.35), Pattern("purity_boss_2.png").similar(0.35), Pattern("peace_boss_1.png").similar(0.35), Pattern("1449633028821.png").similar(0.35)]

    states = [
        'Start',
        'PickMap',
        'Select',
        'Waiting',
        'Attacking',
        'StatsScreen',
        'End',
        'Idle'
    ]

    def __init__(self, botRunner):
        self.botRunner = botRunner
        self.state = 'Start'

    def run(self):
        print self.state
        if self.state == 'Start':
            if self.state == 'Idle':
                return
            else:
                Constants.MAIN_WINDOW.click("quest_icon.png")
                self.state = 'PickMap'
        elif self.state == 'PickMap':
            if Constants.MAIN_WINDOW.exists(Constants.SKIP):
                Constants.MAIN_WINDOW.click(Constants.SKIP)
            else:
                if Constants.MAIN_WINDOW.exists(Pattern("pride_of_the_gryffin.png").targetOffset(191,50), .1):
                    Constants.MAIN_WINDOW.click(Pattern("pride_of_the_gryffin.png").targetOffset(191,50))
                elif Constants.MAIN_WINDOW.exists(Pattern("the_lair_of_fire.png").targetOffset(191,47), .1):
                    Constants.MAIN_WINDOW.click(Pattern("the_lair_of_fire.png").targetOffset(191,47))
                elif Constants.MAIN_WINDOW.exists(Pattern("stronghold_of_peace.png").targetOffset(188,54), .1):
                    Constants.MAIN_WINDOW.click(Pattern("stronghold_of_peace.png").targetOffset(188,54))
                elif Constants.MAIN_WINDOW.exists(Pattern("ruins_of_purity.png").targetOffset(190,47), .1):
                    Constants.MAIN_WINDOW.click(Pattern("ruins_of_purity.png").targetOffset(197,43))
                self.state = 'Select'
        elif self.state == 'Select':
            if Constants.MAIN_WINDOW.exists(Pattern("mini_ap_pot.png").targetOffset(196,9), .25):
                click("mini_ap_pot.png")
                click(Constants.CONFIRM)
                click(Constants.CLOSE)
                click(Constants.SELECT)
            elif Constants.MAIN_WINDOW.exists("deploy.png", .1):
                Constants.MAIN_WINDOW.click("deploy.png")
                Constants.MAIN_WINDOW.click(Constants.CONFIRM)
                self.state = 'Waiting'
            elif Constants.MAIN_WINDOW.exists(Constants.SELECT, .1):
                Constants.MAIN_WINDOW.click(Constants.SELECT)
        elif self.state == 'Waiting':
            if Constants.MAIN_WINDOW.exists(Pattern("quest_clear.png").similar(0.50), .1):
                sleep(1)
                click(Constants.REGION_TOP)
                self.state = 'StatsScreen'
            elif exists("back.png", .1):
                self.state = 'Attacking'
        elif self.state == 'Attacking':
            self.state = 'Waiting'
            for arm_enemy in self.armored_monsters:
                if exists(arm_enemy, .1):
                    click(arm_enemy)
                    self.rend_single()
                    return
            for norm_enemy in self.normal_monsters:
                if exists(norm_enemy, .1):
                    click(norm_enemy)
                    self.norm_aoe()
                    return
            for boss in self.boss:
                if exists(boss, .1):
                    click(boss)
                    if self.has_burst():
                        self.burst()
                    self.norm_single()
                    return
            self.norm_single()
        elif self.state == 'StatsScreen':
            if Constants.MAIN_WINDOW.exists(Pattern("map_clear.png").similar(0.60), .1):
                print "map cleared!"
                click(Constants.REGION_TOP)
            elif Constants.MAIN_WINDOW.exists(Pattern("level_up.png").similar(0.60), .1):
                print "leveled up!"
                self.botRunner.leveledUp = True
                click(Constants.REGION_TOP)
            elif Constants.MAIN_WINDOW.exists("quest_end.png", .1):
                print "finished quest. looking for Next!"
                if (Constants.MAIN_WINDOW.exists("level5.png") or
                        Constants.MAIN_WINDOW.exists("level6.png")):
                    self.botRunner.review = True

                if Constants.MENU_BAR.exists(Constants.NEXT, .1):
                    Constants.MENU_BAR.click(Constants.NEXT)
                    self.state = 'End'
            else:
                print "NOTHING!"
        elif self.state == 'End':
            if Constants.MAIN_WINDOW.exists(Pattern("enemy_appears.png").similar(0.45), .1):
                click(Constants.REGION_TOP)
                wait(Constants.HOME)
                self.state = 'Start'
                click(Constants.HOME)
            elif Constants.MAIN_WINDOW.exists(Constants.SKIP, .1):
                click(Constants.SKIP)
            elif self.botRunner.leveledUp:
                self.botRunner.state = 'MainMenu'
                Constants.MENU_BAR.click(Constants.HOME)
                self.state = 'Idle'
            elif Constants.MAIN_WINDOW.exists(Constants.SELECT, .1):
                self.state = 'Select'
        elif self.state == 'Idle':
            Constants.MENU_BAR.click(Constants.HOME)
            pass

    def norm_aoe(self):
        click(self.fifth_unit)
        click(self.fourth_unit)
        click(self.third_unit)
        click(self.second_unit)
        click(self.first_unit)
        click(self.attack)

    def rend_aoe(self):
        click(self.first_unit)
        click(self.fourth_unit)
        click(self.fifth_unit)
        click(self.third_unit)
        click(self.second_unit)
        click(self.attack)

    def norm_single(self):
        click(self.second_unit)
        click(self.third_unit)
        click(self.fourth_unit)
        click(self.fifth_unit)
        click(self.first_unit)
        click(self.attack)

    def rend_single(self):
        click(self.first_unit)
        click(self.fifth_unit)
        click(self.second_unit)
        click(self.third_unit)
        click(self.fourth_unit)
        click(self.attack)

    def burst(self):
        if Constants.MAIN_WINDOW.exists("idun.png", .25):
            click("burst.png")
            click(self.first_unit)
            click(self.fifth_unit)
            click(self.second_unit)
            click(self.second_unit)
            click(self.second_unit)
            click(self.second_unit)
            click(self.second_unit)
            click(self.second_unit)
            click(self.attack)
        elif Constants.MAIN_WINDOW.exists("hel.png", .25):
            click("burst.png")
            click(self.first_unit)
            click(self.fifth_unit)
            click(self.second_unit)
            click(self.second_unit)
            click(self.first_unit)
            click(self.first_unit)
            click(self.first_unit)
            click(self.first_unit)
            click(self.attack)

    def has_burst(self):
        if exists(Pattern("burst.png").targetOffset(-155,-13), .25):
            return True
        return False

review_notice = "review_notice.png"
play_store_wait = "play_store_wait.png"
back_button = "back_button.png"
ishtaria_icon = "ishtaria_icon.png"
map_clear = "map_clear.png"
quest_end = "quest_end.png"