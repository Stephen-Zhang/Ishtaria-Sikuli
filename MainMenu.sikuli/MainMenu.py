from sikuli import *

import Constants
reload(Constants)

class MainMenu(object):
    def __init__(self, botInfo):
        self.botInfo = botInfo;

    def check(self):
        self.check_challenges()
        self.check_mailbox()

    def review_gold_card(self):
        pass
    
    def check_challenges(self):
        if exists("challenge_found.png", .25):
            # Found a screenshot with challenges
            click("challenge_found.png")
            click(Constants.DETAILS)
            self.collect_challenges()
    
    def _collect_challenges(self):
        print "Collecting Challenges"
        # First Time accessing... Salix Face
        while exists("salix_face.png", .25):
            click(Region(1593,814,48,59))
        click(Constants.RECEIVE_ALL)
        wait(Constants.CLOSE)
        click(Constants.CLOSE)
        click(Constants.HOME)
    
    def check_mailbox(self):
        if exists("mail_found.png", .25):
            print "Checking mailbox!"
            # Found a screenshot with challenges
            click("mail_found.png")
            self.collect_mail()
    
    def _collect_mail(self):
        wait(Constants.RECEIVE_ALL, 3)
        while exists(Constants.RECEIVE_ALL, .25):
            click(Constants.RECEIVE_ALL)
            wait(Constants.CONFIRM)
            click(Constants.CONFIRM)
            wait(Constants.CLOSE)
            click(Constants.CLOSE)
            
        click(Constants.HOME)

    def copy_deck(self):
        click(Constants.MENU)
        click("edit_deck.png")
        wait("copy_deck.png")
        click("copy_deck.png")
        click(Constants.CONFIRM)
        wait("copy_deck.png")
        click(Constants.HOME)