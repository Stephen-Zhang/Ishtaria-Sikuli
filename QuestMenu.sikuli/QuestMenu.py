from sikuli import *

import Images
reload(Images)

class QuestMenu(object):
    def __init__(self, botRunner):
        self.bot = botRunner
        self.state = 'Start'
        self.currentMap = None

        self.first_unit = self.createUnitRegion(.1, .73)
        self.second_unit = self.createUnitRegion(.3, .73)
        self.third_unit = self.createUnitRegion(.5, .73)
        self.fourth_unit = self.createUnitRegion(.7, .73)
        self.fifth_unit = self.createUnitRegion(.9, .73)

    def run(self):
        r = self.bot.region
        print self.state
        if self.state == 'Start':
            if self.state == 'Idle':
                return
            else:
                quest_icon_match = r.exists(self.bot.constants.QUEST_MENU, .1)
                if quest_icon_match:
                    r.click(quest_icon_match)
                    self.state = 'PickMap'

        elif self.state == 'PickMap':
            skip_match = r.exists(self.bot.constants.SKIP, .1)
            if skip_match:
                r.click(skip_match)
            else:
                dunes_match = r.exists(self.bot.constants.DUNE, 0)
                if dunes_match:
                    r.click(dunes_match)
                    self.currentMap = Images.Map7()
                    self.state = 'Select'
                    return

                den_match = r.exists(self.bot.constants.DEN, 0)
                if den_match:
                    r.click(den_match)
                    self.currentMap = Images.Map6()
                    self.state = 'Select'
                    return

                cave_match = r.exists(self.bot.constants.CAVE, 0)
                if cave_match:
                    r.click(cave_match)
                    self.currentMap = Images.Map5()
                    self.state = 'Select'
                    return

                pride_match = r.exists(self.bot.constants.PRIDE, 0)
                if pride_match:
                    r.click(pride_match)
                    self.currentMap = Images.Map4()
                    self.state = 'Select'
                    return

                lair_match = r.exists(self.bot.constants.LAIR, 0)
                if lair_match:
                    r.click(lair_match)
                    self.currentMap = Images.Map3()
                    self.state = 'Select'
                    return

                tower_match = r.exists(self.bot.constants.TOWER, 0)
                if tower_match:
                    r.click(tower_match)
                    self.currentMap = Images.Map2()
                    self.state = 'Select'
                    return

                ruins_match = r.exists(self.bot.constants.RUINS, 0)
                if ruins_match:
                    r.click(ruins_match)
                    self.currentMap = Images.Map1()
                    self.state = 'Select'
                    return

        elif self.state == 'Select':
            mini_pot = r.exists(self.bot.constants.MINI_POT, 0)
            if mini_pot:
                r.click(mini_pot)
                self.state = 'Pot'
                return

            confirm_match = r.exists(self.bot.constants.CONFIRM, 0)
            if confirm_match:
                r.click(confirm_match)
                self.state = 'Waiting'
                return

            deploy_match = r.exists(self.bot.constants.DEPLOY, 0)
            if deploy_match:
                r.click(deploy_match)
                return

            select_match = r.exists(self.bot.constants.SELECT, .1)
            if select_match:
                r.click(select_match)
                return

        elif self.state == 'Pot':
            confirm_match = r.exists(Pattern(self.bot.constants.CONFIRM).similar(self.bot.constants.enemy_similarity), 2)
            r.click(confirm_match)

            r.waitVanish(Pattern(self.bot.constants.CONFIRM).similar(self.bot.constants.enemy_similarity), 2)

            wait(1)

            close_match = r.exists(Pattern(self.bot.constants.CLOSE).similar(self.bot.constants.enemy_similarity), 2)
            r.click(close_match)

            select_match_pot = r.exists(self.bot.constants.SELECT, 2)
            r.click(select_match_pot)
            self.state = 'Select'

        elif self.state == 'Waiting':
            if r.exists(self.bot.constants.QUEST_CLEAR, .1):
                wait(1)
                click(self.bot.constants.REGION_TOP)
                self.state = 'StatsScreen'
                return
            elif r.exists(self.bot.constants.QUEST_END, .1):
                self.state = 'StatsScreen'
                return

            if r.exists(self.bot.constants.BACK, .1):
                self.state = 'Attacking'

        elif self.state == 'Attacking':
            for lion in self.currentMap.lions:
                lion_match = r.exists(Pattern(lion).similar(self.bot.constants.enemy_similarity), .25)
                if lion_match:
                    r.click(lion_match)
                    self.attack(type='REND_MULTI')
                    self.state = 'Waiting'
                    return
            for boss in self.currentMap.boss:
                boss_match = r.exists(boss, .1)
                if boss_match:
                    print "Boss Match: {}".format(boss)
                    r.click(boss_match)
                    burst_match = r.exists(self.bot.constants.BURST, .1)
                    if burst_match:
                        "Bursting Boss"
                        self.burst(burst_match)
                    else:
                        self.attack_boss()
                    self.state = 'Waiting'
                    return

            for norm_enemy in self.currentMap.normal:
                norm_enemy_match = r.exists(Pattern(norm_enemy).similar(self.bot.constants.enemy_similarity), .1)
                if norm_enemy_match:
                    r.click(norm_enemy_match)
                    print "Normal Enemy Match: {}".format(norm_enemy)
                    self.attack(type='NORMAL_MULTI')
                    self.state = 'Waiting'
                    return

            for armored_enemy in self.currentMap.armored:
                armored_enemy_match = r.exists(Pattern(armored_enemy).similar(self.bot.constants.enemy_similarity), .1)
                if armored_enemy_match:
                    print "Armored Enemy Match: {}".format(armored_enemy)
                    r.click(armored_enemy_match)
                    self.attack(type='REND_RUSH')
                    self.state = 'Waiting'
                    return

            for strong_enemy in self.currentMap.strong:
                strong_enemy_match = r.exists(Pattern(strong_enemy).similar(self.bot.constants.enemy_similarity), .1)
                if strong_enemy_match:
                    print "Strong Enemy Match: {}".format(strong_enemy)
                    r.click(strong_enemy_match)
                    self.attack(type='NORMAL_RUSH')
                    self.state = 'Waiting'
                    return

            print "No Match Found."
            self.attack(type='REND_RUSH')
            self.state = 'Waiting'

        elif self.state == 'StatsScreen':
            if r.exists(self.bot.constants.QUEST_END, .1):
                print "Quest Ended"
                if r.exists(self.bot.constants.LEVEL_UP, .1):
                    print "Leveled Up"
                    self.bot.leveledUp = True

                next_match = r.exists(self.bot.constants.NEXT, .1)
                if next_match:
                    r.click(next_match)
                    self.state = 'End'
            else:
                r.click(self.bot.constants.REGION_TOP)
        elif self.state == 'End':
            skip_match = r.exists(self.bot.constants.SKIP, 2)
            if skip_match:
                r.click(skip_match)
                wait(.75)
                return
            elif r.exists(self.bot.constants.ENEMY_APPEARS, .1) or r.exists(self.bot.constants.RAID_AREA, .1):
                while not r.exists(self.bot.constants.RAID_BANNER, .1):
                    r.click(self.bot.constants.REGION_TOP)
                home_match = r.exists(self.bot.constants.HOME, .1)
                if home_match:
                    self.bot.state = 'Battle'
                    self.bot.battleMenu.state = 'Start'
                    return
            elif self.bot.leveledUp:
                home_match = r.exists(self.bot.constants.HOME, .1)
                if home_match:
                    r.click(home_match)
                    self.bot.state = 'Battle'
                    self.bot.battleMenu.state = 'Start'
            elif r.exists(self.bot.constants.SELECT, .1):
                self.state = 'Select'
                return

    def attack(self, type):
        r = self.bot.region
        if type == 'NORMAL_RUSH':
            self.clickSequence([2, 3, 4, 5, 1])
            r.click(self.bot.constants.ATTACK)
        elif type == 'NORMAL_MULTI':
            self.clickSequence([5, 4, 3, 2, 1])
            r.click(self.bot.constants.ATTACK)
        elif type == 'REND_RUSH':
            self.clickSequence([1, 4, 2, 3, 5])
            r.click(self.bot.constants.ATTACK)
        elif type == 'REND_MULTI':
            self.clickSequence([1, 4, 5, 3, 2])
            r.click(self.bot.constants.ATTACK)
        else:
            print "Attack with no type, using default RUSH"
            self.clickSequence([2, 3, 4, 5, 1])
            r.click(self.bot.constants.ATTACK)

    def attack_boss(self):
        map_num = self.currentMap
        attack_type = ''
        if isinstance(map_num, Images.Map1):
            attack_type = 'NORMAL_MULTI'
        elif isinstance(map_num, Images.Map2):
            attack_type = 'NORMAL_RUSH'
        elif isinstance(map_num, Images.Map3):
            attack_type = 'REND_RUSH'
        elif isinstance(map_num, Images.Map4):
            attack_type = 'NORMAL_RUSH'
        elif isinstance(map_num, Images.Map5):
            attack_type = 'NORMAL_RUSH'
        elif isinstance(map_num, Images.Map6):
            attack_type = 'NORMAL_RUSH'
        elif isinstance(map_num, Images.Map7):
            attack_type = 'NORMAL_RUSH'
        else:
            attack_type = 'NORMAL_RUSH'
        self.attack(type=attack_type)

    def burst(self, burst_match):
        r = self.bot.region
        u = self.bot.strong_unit

        r.click(burst_match)
        wait(.1)
        if isinstance(self.currentMap, Images.Map3):
            self.clickSequence([1, 4, 2, 2, u, u, u, u])
        else:
            self.clickSequence([2, 2, u, u, u, u, u, u])
        r.click(self.bot.constants.ATTACK)

    def createUnitRegion(self, x_mod, y_mod):
        width = self.bot.region.getW()
        height = self.bot.region.getH()
        x = self.bot.region.getX()
        y = self.bot.region.getY()

        return Region(int(x + width * x_mod), int(y + height * y_mod), 2, 2)

    def clickSequence(self, list, wait_amt=.1):
        r = self.bot.region
        for token in list:
            if token == 1:
                r.click(self.first_unit)
            elif token == 2:
                r.click(self.second_unit)
            elif token == 3:
                r.click(self.third_unit)
            elif token == 4:
                r.click(self.fourth_unit)
            elif token == 5:
                r.click(self.fifth_unit)
            wait(wait_amt)
