from sikuli import *

class ConstantsManager(object):
    def __init__(self, region):
        self.region = region

        self.init_main_buttons()
        self.init_regions()

    def init_main_buttons(self):
        self.HOME = "HOME.png"
        self.BATTLE = "BATTLE.png"
        self.CONFIRM = "CONFIRM.png"
        self.CLOSE = "CLOSE.png"
        self.NEXT = "NEXT.png"
        self.SELECT = "SELECT.png"
        self.SKIP = "SKIP.png"

    def init_regions(self):
        self.REGION_TOP = self.create_click_region(.5, .19)
        self.REGION_BOT = self.create_click_region(.5, .65)


    def create_click_region(self, x_mod, y_mod):
        width = self.region.getW()
        height = self.region.getH()
        x = self.region.getX()
        y = self.region.getY()

        print 'x: {}'.format(x)
        print 'y: {}'.format(y)
        print 'width: {}'.format(width)
        print 'height: {}'.format(height)

        return Region(int(x + width * x_mod), int(y + height * y_mod), 2, 2)
