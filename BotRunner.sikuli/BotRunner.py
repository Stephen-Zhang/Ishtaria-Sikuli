from sikuli import *

import MainMenu
reload(MainMenu)

import BattleMenu
reload(BattleMenu)

import QuestMenu
reload(QuestMenu)

import Constants
reload(Constants)

class BotObject(object):
    states = [
        'MainMenu',
        'Battle',
        'Quest'
    ]

    def __init__(self):
        self.copiedDeck = False
        self.battlesDone = False
        self.leveledUp = True
        self.finished = False

        self.state = 'Battle'

        self.mainMenu = MainMenu.MainMenu(self)
        self.battleMenu = BattleMenu.BattleMenu(self)
        self.questMenu = QuestMenu.QuestMenu(self)

    def run(self):
        if exists(Pattern("login.png").similar(0.60), .25):
            while not exists(Constants.HOME_CHRISTMAS):
                click(Constants.REGION_TOP)
        if exists("Connect_failed.png", .25):
            click(Constants.CONFIRM)
        if self.state == 'MainMenu':
            self.mainMenu.run()
        if self.state == 'Battle':
            self.battleMenu.run()
        if self.state == 'Quest':
            self.questMenu.run()

    def save(self):
        # TODO:
        click(Pattern("open_apps.png").exact())
        dragDrop("ishtaria_face.png", bottom_delete = Region(1214,823,60,58))
        click("file_explorer_app.png")
        click("folder.png")
        while not exists("rename.png"):
            mouseDown("current_file.png")
        click("rename.png")
        wait("dialog.png")
        type(self.name + str(self.num))
        click("okay.png")

        # Rename file next to you
        while not exists("rename.png"):
            mouseDown("current_file.png")
        # Click ES Explorer
        # Click

    def do_level_5_actions(self):
        # Grab Review Card
        # Set Leader
        # Sell Units
        # Spend Medals
        # Enhance Units
        # Do normal level up actions
        pass

ishtaria_app = "ishtaria_app.png"
folder = "folder.png"
next_file = "next_file.png"
dialog = "dialog.png"
okay = "okay.png"
scroll_lo = Region(944,241,34,30)
scroll_hi = Region(947,132,33,25)
tab_home = "tab_home.png"
left = Region(622,501,125,78)
down = Region(467,588,147,76)
current_file2 = "current_file2.png"
view = "view_button.png"
medium_list = "medium_list.png"
