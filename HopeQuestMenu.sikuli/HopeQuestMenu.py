from sikuli import *

import Images
reload(Images)

class HopeQuestMenu(object):
    def __init__(self, botRunner):
        self.bot = botRunner
        self.state = 'Start'

        self.standing_match = None
        
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
                palace_match = r.exists(Pattern("Palace_of_fire.png").targetOffset(194,0), 0)
                if palace_match:
                    r.click(palace_match)
                    self.state = 'Find Hope'
                    return
                r.dragDrop(self.bot.constants.REGION_BOT, self.bot.constants.REGION_TOP)

        elif self.state == 'Find Hope':
            standing_match = r.exists(Pattern("1457252112225.png").similar(0.90).targetOffset(420,71), .25)
            if not standing_match:
                r.dragDrop(self.bot.constants.REGION_BOT, self.bot.constants.REGION_TOP)
            else:
                self.standing_match = standing_match
                r.click(standing_match)
                self.started = True
                self.state = 'Select'

        elif self.state == 'Select':
            pot = r.exists(Pattern("1457252951166.png").similar(0.94).targetOffset(341,13), 0)
            if pot:
                r.click(pot)
                wait(.5)
                r.click(Pattern(self.bot.constants.CONFIRM).similar(.8))
                r.waitVanish(Pattern(self.bot.constants.CONFIRM).similar(.8))
                wait(.5)
                r.click(Pattern(self.bot.constants.CLOSE).similar(.8))
                r.waitVanish(Pattern(self.bot.constants.CLOSE).similar(.8))

                r.click(self.standing_match)
                return

            confirm_match = r.exists(self.bot.constants.CONFIRM, 0)
            if confirm_match:
                r.click(confirm_match)
                self.state = 'Waiting'
                return

            all_out_match = r.exists(self.bot.constants.ALL_OUT_ATTACK, .1)
            if all_out_match:
                r.click(all_out_match)
                return

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
                print "found Back!"
                self.state = 'Attacking'
            print "found nothing!"

        elif self.state == 'Attacking':
            burst_match = r.exists(self.bot.constants.BURST, .1)
            if burst_match:
                "Bursting Boss"
                self.burst(burst_match)
                self.state = 'Waiting'
                return
            self.attack(type='NORMAL_MULTI')
            self.state = 'Waiting'

        elif self.state == 'StatsScreen':
            if r.exists(self.bot.constants.QUEST_END, .1):
                print "Quest Ended"
                next_match = r.exists(self.bot.constants.NEXT, .1)
                if next_match:
                    r.click(next_match)
                    self.state = 'End'
            else:
                r.click(self.bot.constants.REGION_TOP)
        elif self.state == 'End':
            if r.exists(self.bot.constants.ENEMY_APPEARS, .1) or r.exists(self.bot.constants.RAID_AREA, .1):
                while not r.exists(self.bot.constants.RAID_BANNER, .1):
                    r.click(self.bot.constants.REGION_TOP)
                home_match = r.exists(self.bot.constants.HOME, .1)
                if home_match:
                    r.click(home_match)
                    self.state = 'Start'
            else:
                self.state = 'Find Hope'

    def attack(self, type):
        r = self.bot.region
        self.clickSequence([5, 4, 3, 2, 1])
        r.click(self.bot.constants.ATTACK)
    
    def burst(self, burst_match):
        r = self.bot.region

        r.click(burst_match)
        wait(.1)

        self.clickSequence([4, 4, 4, 4, 4, 4, 4, 4])
        
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
