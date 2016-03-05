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
    map5 = Images.Map5()
    map6 = Images.Map6()
    map7 = Images.Map7()

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
                quest_icon_match = Constants.MAIN_WINDOW.exists("1456423118705.png", .1)
                if quest_icon_match:
                    Constants.MAIN_WINDOW.click(quest_icon_match)
                    self.state = 'PickMap'

        elif self.state == 'PickMap':
            skip_match = Constants.MAIN_WINDOW.exists(Constants.SKIP, .1)
            if skip_match:
                Constants.MAIN_WINDOW.click(skip_match)
            else:
                dunes_match = Constants.MAIN_WINDOW.exists(Pattern("western_wind_dunes.png").targetOffset(194,50), 0)
                if dunes_match:
                    #self.botRunner.state = 'Finished'
                    #return

                    Constants.MAIN_WINDOW.click(dunes_match)
                    self.currentMap = self.map7
                    self.state = 'Select'
                    return

                den_match = Constants.MAIN_WINDOW.exists(Pattern("den_of_the_dragon.png").targetOffset(191,2), 0)
                if den_match:
                    #self.botRunner.state = 'Finished'
                    #return 

                    Constants.MAIN_WINDOW.click(den_match)
                    self.currentMap = self.map6
                    self.state = 'Select'
                    return

                cave_match = Constants.MAIN_WINDOW.exists(Pattern("cave_of_temptation.png").targetOffset(195,16), 0)
                if cave_match:
                    #self.botRunner.state = 'Finished'
                    #return

                    Constants.MAIN_WINDOW.click(cave_match)
                    self.currentMap = self.map5
                    self.state = 'Select'
                    return

                pride_match = Constants.MAIN_WINDOW.exists(Pattern("pride_of_the_gryffin.png").targetOffset(186,-8), 0)
                if pride_match:
                    #self.botRunner.state = 'Finished'
                    #return

                    Constants.MAIN_WINDOW.click(pride_match)
                    self.currentMap = self.map4
                    self.state = 'Select'
                    return

                lair_match = Constants.MAIN_WINDOW.exists(Pattern("the_lair_of_fire.png").targetOffset(181,2), 0)
                if lair_match:
                    Constants.MAIN_WINDOW.click(lair_match)
                    self.currentMap = self.map3
                    self.state = 'Select'
                    return

                tower_match = Constants.MAIN_WINDOW.exists(Pattern("stronghold_of_peace.png").targetOffset(187,-5), 0)
                if tower_match:
                    Constants.MAIN_WINDOW.click(tower_match)
                    self.currentMap = self.map2
                    self.state = 'Select'
                    return

                ruins_match = Constants.MAIN_WINDOW.exists(Pattern("ruins_of_purity.png").targetOffset(190,-9), .1)
                if ruins_match:
                    Constants.MAIN_WINDOW.click(ruins_match)
                    self.currentMap = self.map1
                    self.state = 'Select'
                    return

        elif self.state == 'Select':
            mini_pot = Constants.MAIN_WINDOW.exists(Pattern("mini_ap_pot.png").targetOffset(196,9), .1)
            if mini_pot:
                Constants.MAIN_WINDOW.click(mini_pot)
                self.state = 'Pot'
                return

            confirm_match = Constants.MAIN_WINDOW.exists(Constants.CONFIRM, .1)
            if confirm_match:
                Constants.MAIN_WINDOW.click(confirm_match)
                self.state = 'Waiting'
                return

            deploy_match = Constants.MAIN_WINDOW.exists("deploy.png", .1)
            if deploy_match:
                Constants.MAIN_WINDOW.click(deploy_match)
                return

            select_match = Constants.MAIN_WINDOW.exists(Constants.SELECT, .1)
            if select_match:
                Constants.MAIN_WINDOW.click(select_match)
                return

        elif self.state == 'Pot':
            confirm_match = Constants.MAIN_WINDOW.exists(Pattern(Constants.CONFIRM).similar(.8), 2)
            Constants.MAIN_WINDOW.click(confirm_match)

            Constants.MAIN_WINDOW.waitVanish(Pattern(Constants.CONFIRM).similar(.8), 2)

            wait(1)

            close_match = Constants.MAIN_WINDOW.exists(Pattern(Constants.CLOSE).similar(.8), 2)
            Constants.MAIN_WINDOW.click(close_match)

            select_match_pot = Constants.MAIN_WINDOW.exists(Constants.SELECT, 2)
            Constants.MAIN_WINDOW.click(select_match_pot)
            self.state = 'Select'

        elif self.state == 'Waiting':
            if Constants.MAIN_WINDOW.exists("quest_clear.png", .1):
                wait(1)
                click(Constants.REGION_TOP)
                self.state = 'StatsScreen'
                return
            elif Constants.MAIN_WINDOW.exists("quest_end.png", .1):
                self.state = 'StatsScreen'
                return

            if Constants.FULL_SCREEN.exists(Pattern("back.png").similar(0.98), .1):
                self.state = 'Attacking'

        elif self.state == 'Attacking':
            for lion in self.currentMap.lions:
                lion_match = Constants.MAIN_WINDOW.exists(Pattern(lion).similar(.8), 1)
                if lion_match:
                    Constants.MAIN_WINDOW.click(lion_match)
                    self.rend_single()
                    self.state = 'Waiting'            
                    return
            for boss in self.currentMap.boss:
                boss_match = Constants.MAIN_WINDOW.exists(boss, .1)
                if boss_match:
                    if Constants.MAIN_WINDOW.exists("quest_clear.png", .1):
                        self.state = 'StatsScreen'
                        return
                    print "found boss match!"
                    Constants.MAIN_WINDOW.click(boss_match)
                    burst_match = Constants.MAIN_WINDOW.exists("burst.png", .1)
                    if burst_match:
                        "with burst!"
                        self.burst(burst_match)
                    else:
                        self.attack_boss()
                    self.state = 'Waiting'
                    return

            for norm_enemy in self.currentMap.normal:
                norm_enemy_match = Constants.MAIN_WINDOW.exists(Pattern(norm_enemy).similar(.8), .1)
                if norm_enemy_match:
                    if Constants.MAIN_WINDOW.exists("quest_clear.png", .1):
                        self.state = 'StatsScreen'
                        return
                    Constants.MAIN_WINDOW.click(norm_enemy_match)
                    print "found normal enemy match!"
                    self.norm_aoe()
                    self.state = 'Waiting'
                    return

            for armored_enemy in self.currentMap.armored:
                armored_enemy_match = Constants.MAIN_WINDOW.exists(Pattern(armored_enemy).similar(.8), .1)
                if armored_enemy_match:
                    if Constants.MAIN_WINDOW.exists("quest_clear.png", .1):
                        self.state = 'StatsScreen'
                        return
                    print "found armored match!"
                    Constants.MAIN_WINDOW.click(armored_enemy_match)
                    self.rend_single()
                    self.state = 'Waiting'
                    return

            for strong_enemy in self.currentMap.strong:
                strong_enemy_match = Constants.MAIN_WINDOW.exists(Pattern(strong_enemy).similar(.8), .1)
                if strong_enemy_match:
                    if Constants.MAIN_WINDOW.exists("quest_clear.png", .1):
                        self.state = 'StatsScreen'
                        return
                    print "found strong match!"
                    Constants.MAIN_WINDOW.click(strong_enemy_match)
                    self.norm_single()
                    self.state = 'Waiting'
                    return

            print "didnt find any match!"
            if Constants.MAIN_WINDOW.exists("quest_clear.png", 2):
                self.state = 'StatsScreen'
                return
            self.rend_single()
            self.state = 'Waiting'
        elif self.state == 'StatsScreen':
            if Constants.MAIN_WINDOW.exists("quest_end.png", .1):
                print "finished quest. looking for Next!"
                if Constants.MAIN_WINDOW.exists("level_up.png", .1):
                    self.botRunner.leveledUp = True

                next_match = Constants.MENU_BAR.exists(Constants.NEXT, .1)
                if next_match:
                    Constants.MENU_BAR.click(next_match)
                    self.state = 'End'
            else:
                Constants.MAIN_WINDOW.click(Constants.REGION_TOP)
        elif self.state == 'End':
            skip_match = Constants.MAIN_WINDOW.exists(Constants.SKIP, 2)
            if skip_match:
                Constants.MAIN_WINDOW.click(skip_match)
                wait(.75)
                return
            elif Constants.MAIN_WINDOW.exists(Pattern("1452272299241.png").similar(0.50), .1) or Constants.MAIN_WINDOW.exists("1452272332929.png", .1):
                while not Constants.MAIN_WINDOW.exists("raid_battles.png", .1):
                    Constants.MAIN_WINDOW.click(Constants.REGION_TOP)
                home_match = Constants.MENU_BAR.exists(Constants.HOME_CHRISTMAS, .1)
                if home_match:
                    self.botRunner.state = 'Battle'
                    self.botRunner.battleMenu.state = 'Start'
                    return
            elif self.botRunner.leveledUp:
                home_match = Constants.MENU_BAR.exists(Constants.HOME_CHRISTMAS, .1)
                if home_match:
                    Constants.MENU_BAR.click(home_match)
                    self.botRunner.state = 'Battle'
                    self.botRunner.battleMenu.state = 'Start'
            elif Constants.MAIN_WINDOW.exists(Constants.SELECT, .1):
                self.state = 'Select'
                return

    def purify_start(self):
        Constants.MAIN_WINDOW.click("1456423177912.png")
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
                wait("purified.png", 12)
                wait(Constants.CLOSE)
                click(Constants.CLOSE)

    def norm_aoe(self):
        Constants.MAIN_WINDOW.click(self.fifth_unit)
        Constants.MAIN_WINDOW.click(self.fourth_unit)
        Constants.MAIN_WINDOW.click(self.third_unit)
        Constants.MAIN_WINDOW.click(self.second_unit)
        Constants.MAIN_WINDOW.click(self.first_unit)
        Constants.MENU_BAR.click(self.attack)

    def rend_aoe(self):
        Constants.MAIN_WINDOW.click(self.first_unit)
        Constants.MAIN_WINDOW.click(self.fourth_unit)
        Constants.MAIN_WINDOW.click(self.fifth_unit)
        Constants.MAIN_WINDOW.click(self.third_unit)
        Constants.MAIN_WINDOW.click(self.second_unit)
        Constants.MENU_BAR.click(self.attack)

    def norm_single(self):
        Constants.MAIN_WINDOW.click(self.second_unit)
        Constants.MAIN_WINDOW.click(self.third_unit)
        Constants.MAIN_WINDOW.click(self.fourth_unit)
        Constants.MAIN_WINDOW.click(self.fifth_unit)
        Constants.MAIN_WINDOW.click(self.first_unit)
        Constants.MENU_BAR.click(self.attack)

    def rend_single(self):
        Constants.MAIN_WINDOW.click(self.first_unit)
        Constants.MAIN_WINDOW.click(self.fourth_unit)
        Constants.MAIN_WINDOW.click(self.second_unit)
        Constants.MAIN_WINDOW.click(self.third_unit)
        Constants.MAIN_WINDOW.click(self.fifth_unit)
        Constants.MENU_BAR.click(self.attack)

    def attack_boss(self):
        map_num = self.currentMap
        if isinstance(map_num, Images.Map1):
            self.norm_single()
        elif isinstance(map_num, Images.Map2):
            self.norm_single()
        elif isinstance(map_num, Images.Map3):
            self.rend_single()
        elif isinstance(map_num, Images.Map4):
            self.norm_single()
        elif isinstance(map_num, Images.Map5):
            self.norm_single()
        elif isinstance(map_num, Images.Map6):
            self.norm_single()
        elif isinstance(map_num, Images.Map7):
            self.norm_single()
        else:
            self.norm_single()

    def burst(self, burst_match):
        if Constants.MAIN_WINDOW.exists("idun.png", .25):
            print "Idun burst"
            Constants.MAIN_WINDOW.click(burst_match)
            wait(.1)
            Constants.MAIN_WINDOW.click(self.first_unit)
            wait(.1)
            Constants.MAIN_WINDOW.click(self.fourth_unit)
            wait(.1)
            Constants.MAIN_WINDOW.click(self.second_unit)
            wait(.1)
            Constants.MAIN_WINDOW.click(self.second_unit)
            wait(.1)
            Constants.MAIN_WINDOW.click(self.second_unit)
            wait(.1)
            Constants.MAIN_WINDOW.click(self.second_unit)
            wait(.1)
            Constants.MAIN_WINDOW.click(self.second_unit)
            wait(.1)
            Constants.MAIN_WINDOW.click(self.second_unit)
            wait(.1)
            Constants.MENU_BAR.click(self.attack)
        elif Constants.MAIN_WINDOW.exists("hel.png", .25):
            print "Hel burst"
            Constants.MAIN_WINDOW.click(burst_match)
            wait(.1)
            Constants.MAIN_WINDOW.click(self.first_unit)
            wait(.1)
            Constants.MAIN_WINDOW.click(self.fourth_unit)
            wait(.1)
            Constants.MAIN_WINDOW.click(self.second_unit)
            wait(.1)
            Constants.MAIN_WINDOW.click(self.second_unit)
            wait(.1)
            Constants.MAIN_WINDOW.click(self.first_unit)
            wait(.1)
            Constants.MAIN_WINDOW.click(self.first_unit)
            wait(.1)
            Constants.MAIN_WINDOW.click(self.first_unit)
            wait(.1)
            Constants.MAIN_WINDOW.click(self.first_unit)
            wait(.1)
            Constants.MENU_BAR.click(self.attack)
        else:
            print isinstance(self.currentMap, Images.Map3)
            if isinstance(self.currentMap, Images.Map3):
                Constants.MAIN_WINDOW.click(burst_match)
                wait(.1)
                Constants.MAIN_WINDOW.click(self.first_unit)
                wait(.1)
                Constants.MAIN_WINDOW.click(self.fourth_unit)
                wait(.1)
                Constants.MAIN_WINDOW.click(self.second_unit)
                wait(.1)
                Constants.MAIN_WINDOW.click(self.second_unit)
                wait(.1)
                Constants.MAIN_WINDOW.click(self.fourth_unit)
                wait(.1)
                Constants.MAIN_WINDOW.click(self.fourth_unit)
                wait(.1)
                Constants.MAIN_WINDOW.click(self.fourth_unit)
                wait(.1)
                Constants.MAIN_WINDOW.click(self.fourth_unit)
                wait(.1)
                Constants.MENU_BAR.click(self.attack)
            else:
                Constants.MAIN_WINDOW.click(burst_match)
                wait(.1)
                Constants.MAIN_WINDOW.click(self.second_unit)
                wait(.1)
                Constants.MAIN_WINDOW.click(self.second_unit)
                wait(.1)
                Constants.MAIN_WINDOW.click(self.fourth_unit)
                wait(.1)
                Constants.MAIN_WINDOW.click(self.fourth_unit)
                wait(.1)
                Constants.MAIN_WINDOW.click(self.fourth_unit)
                wait(.1)
                Constants.MAIN_WINDOW.click(self.fourth_unit)
                wait(.1)
                Constants.MAIN_WINDOW.click(self.fourth_unit)
                wait(.1)
                Constants.MAIN_WINDOW.click(self.fourth_unit)
                wait(.1)
                Constants.MENU_BAR.click(self.attack)