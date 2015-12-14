from sikuli import *

import Constants
reload(Constants)

import Images
reload(Images)

class QuestMenu(object):
    first_unit = Region(1296,589,117,330)
    second_unit = Region(1420,587,118,333)
    third_unit = Region(1543,587,119,330)
    fourth_unit = Region(1668,588,118,330)
    fifth_unit = Region(1792,588,119,332)
    attack = "attack.png"
    map1 = Images.Map1()
    map2 = Images.Map2()
    map3 = Images.Map3()
    map4 = Images.Map4()

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
        self.currentMap = None

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
                    self.botRunner.state = 'Finished'
                    return
                elif Constants.MAIN_WINDOW.exists(Pattern("the_lair_of_fire.png").targetOffset(191,47), .1):
                    Constants.MAIN_WINDOW.click(Pattern("the_lair_of_fire.png").targetOffset(191,47))
                    self.currentMap = self.map3
                elif Constants.MAIN_WINDOW.exists(Pattern("stronghold_of_peace.png").targetOffset(188,54), .1):
                    Constants.MAIN_WINDOW.click(Pattern("stronghold_of_peace.png").targetOffset(188,54))
                    self.currentMap = self.map2
                elif Constants.MAIN_WINDOW.exists(Pattern("ruins_of_purity.png").targetOffset(190,47), .1):
                    Constants.MAIN_WINDOW.click(Pattern("ruins_of_purity.png").targetOffset(197,43))
                    self.currentMap = self.map1
                self.state = 'Select'
        elif self.state == 'Select':
            if Constants.MAIN_WINDOW.exists(Pattern("mini_ap_pot.png").targetOffset(196,9), .25):
                click(Pattern("mini_ap_pot.png").targetOffset(196,9))
                wait(Constants.CONFIRM)
                click(Constants.CONFIRM)
                wait(Constants.CLOSE)
                click(Constants.CLOSE)
                wait(Constants.SELECT)
                click(Constants.SELECT)
            elif Constants.MAIN_WINDOW.exists("deploy.png", .1):
                Constants.MAIN_WINDOW.click("deploy.png")
                wait(.5)
                Constants.MAIN_WINDOW.click(Constants.CONFIRM)
                self.state = 'Waiting'
            elif Constants.MAIN_WINDOW.exists(Constants.SELECT, .1):
                Constants.MAIN_WINDOW.click(Constants.SELECT)
        elif self.state == 'Waiting':
            if Constants.MAIN_WINDOW.exists("1450071819288.png", .1):
                wait(1)
                click(Constants.REGION_TOP)
                self.state = 'StatsScreen'
            elif Constants.MAIN_WINDOW.exists("quest_end.png", .1):
                self.state = 'StatsScreen'
            elif exists(Pattern("back.png").similar(0.98), .1):
                self.state = 'Attacking'
        elif self.state == 'Attacking':
            self.state = 'Waiting'
            for norm_enemy in self.currentMap.normal:
                if exists(norm_enemy, .1):
                    click(norm_enemy)
                    self.norm_aoe()
                    return
            for boss in self.currentMap.boss:
                if exists(boss, .1):
                    click(boss)
                    if self.has_burst():
                        self.burst()
                        return
                    self.attack_boss()
                    return
            for armored_enemy in self.currentMap.armored:
                if exists(armored_enemy, .1):
                    click(armored_enemy)
                    self.rend_single()
                    return
            for strong_enemy in self.currentMap.strong:
                if exists(strong_enemy, .1):
                    click(strong_enemy)
                    self.norm_single()
                    return
            self.norm_single()
        elif self.state == 'StatsScreen':
            if Constants.MAIN_WINDOW.exists("quest_end.png", .1):
                print "finished quest. looking for Next!"
                if Constants.MAIN_WINDOW.exists("1450072743996.png", .1):
                    self.botRunner.leveledUp = True
                    if (Constants.MAIN_WINDOW.exists("level5.png") or
                            Constants.MAIN_WINDOW.exists("level6.png")):
                        self.botRunner.review = True
                if Constants.MENU_BAR.exists(Constants.NEXT, .1):
                    Constants.MENU_BAR.click(Constants.NEXT)
                    self.state = 'End'
            else:
                click(Constants.REGION_TOP)
        elif self.state == 'End':
            if Constants.MAIN_WINDOW.exists(Constants.SKIP, 2):
                click(Constants.SKIP)
            elif self.botRunner.leveledUp:
                self.botRunner.state = 'Battle'
                self.botRunner.battleMenu.state = 'Start'
                Constants.MENU_BAR.click(Constants.HOME_CHRISTMAS)
                self.state = 'Idle'
            elif Constants.MAIN_WINDOW.exists(Constants.SELECT, 1):
                self.state = 'Select'
        elif self.state == 'Idle':
            Constants.MENU_BAR.click(Constants.HOME_CHRISTMAS)
            pass

    def purify_start(self):
        Constants.MAIN_WINDOW.click("quest_icon.png")
        wait("select_area.png", 3)

        self.purify(Pattern("ruins_of_purity.png").targetOffset(197,43))

        click("back_button.png")
        wait(1)
        click("back_button.png")

        self.purify(Pattern("stronghold_of_peace.png").targetOffset(188,54))

    def purify(self, pattern):
        dragDrop(Constants.REGION_BOT, Constants.REGION_TOP)
        Constants.MAIN_WINDOW.click(pattern)
        wait("purify_button.png", 3)
        click("purify_button.png")
        for aura in ["attack_aura.png", "life_aura.png", "prep_aura.png", "skill_aura.png"]:
            for j in range(3):
                click(aura)
                wait(Constants.CONFIRM)
                click(Constants.CONFIRM)
                wait("purified.png", 10)
                click(Constants.CLOSE)

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

    def attack_boss(self):
        map_num = self.currentMap.__class__
        if map_num is Images.Map1:
            self.norm_single()
        elif map_num is Images.Map2:
            self.norm_single()
        elif map_num is Images.Map3:
            self.rend_single()
        elif map_num is Images.Map4:
            self.rend_single()

    def burst(self):
        if Constants.MAIN_WINDOW.exists("idun.png", .25):
            click(Pattern("burst.png").targetOffset(-151,-12))
            wait(.1)
            click(self.first_unit)
            wait(.1)
            click(self.fifth_unit)
            wait(.1)
            click(self.second_unit)
            wait(.1)
            click(self.second_unit)
            wait(.1)
            click(self.second_unit)
            wait(.1)
            click(self.second_unit)
            wait(.1)
            click(self.second_unit)
            wait(.1)
            click(self.second_unit)
            wait(.1)
            click(self.attack)
        elif Constants.MAIN_WINDOW.exists("hel.png", .25):
            click(Pattern("burst.png").targetOffset(-160,2))
            wait(.1)
            click(self.first_unit)
            wait(.1)
            click(self.fifth_unit)
            wait(.1)
            click(self.second_unit)
            wait(.1)
            click(self.second_unit)
            wait(.1)
            click(self.first_unit)
            wait(.1)
            click(self.first_unit)
            wait(.1)
            click(self.first_unit)
            wait(.1)
            click(self.first_unit)
            wait(.1)
            click(self.attack)

    def has_burst(self):
        if exists(Pattern("burst.png").targetOffset(-155,-13), 1):
            return True
        return False

review_notice = "review_notice.png"
play_store_wait = "play_store_wait.png"
back_button = "back_button.png"
ishtaria_icon = "ishtaria_icon.png"
map_clear = "map_clear.png"
quest_end = "quest_end.png"
purify_button = "purify_button.png"
back_button = "back_button.png"