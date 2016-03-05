from sikuli import *
FULL_SCREEN = Region(1290,30,623,970)
MENU_BAR = Region(1283,897,637,140)
HOME = "HOME.png" 
HOME_CHRISTMAS = "HOME_CHRISTMAS.png"
MENU = "MENU.png"
MENU_CHRISTMAS = "MENU_CHRISTMAS.png"
BATTLE = "1456423363758.png"
BATTLE_CHRISTMAS = "BATTLE.png"
PACKS = "PACKS.png"

MAIN_WINDOW = Region(1289,29,629,868)
CONFIRM = "CONFIRM.png"
CLOSE = "CLOSE.png"
RECEIVE_ALL = "RECEIVE_ALL.png"
NEXT = "NEXT.png"
SELECT = "SELECT.png"
DETAILS = "DETAILS.png"
SKIP = "SKIP.png"
REGION_TOP = Region(1579,214,38,35)
REGION_BOT = Region(1583,706,39,25)

State = {
    'MainMenu' : 0,
    'Quests' : 1,
    'Battle' : 2
}

MainMenu_State = {
    'Leveled' : 0,
    'NotLeveled' : 1
}

Quests_State = {
    'Start' : 0,
    'Pick' : 1,
    'Select' : 2,
    'Wait' : 3,
    'Attack' : 4,
    'End' : 5
}