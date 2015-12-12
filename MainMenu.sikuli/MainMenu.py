from sikuli import *

import Constants
reload(Constants)

class MainMenu(object):
    states = [
        'Start',
        'CollectStart',
        'MailCollect',
        'ChallengesCollect',
        'ChallengesCollect',
        'End'
    ]

    def __init__(self, botInfo):
        self.botInfo = botInfo;
        self.state = 'Start'

    def run(self):
        print self.state
        if self.state == 'Start':
            if exists("2800_crowns.png", .1):
                #self.botInfo.questMenu.state = 'Purify'
                self.botInfo.state = 'Quest'
            if exists("finished_crowns.png", .1):
                self.botInfo.finished = True
                self.state = 'End'
            if self.botInfo.leveledUp:
                self.state = 'CollectStart'
            else:
                self.state = 'End'
        elif self.state == 'CollectStart':
            if exists("mail_found.png", .25):
                click("mail_found.png")
                self.state = 'MailCollect'
            elif exists("challenge_found.png", .25):
                self.state = 'ChallengesCollect'
                click("challenge_found.png")
                sleep(.5)
                click(Constants.DETAILS)
            else:
                self.state = 'End'
        elif self.state == 'MailCollect':
            if exists("receive.png", .1):
                click(Constants.RECEIVE_ALL)
                sleep(.25)
                click(Constants.CONFIRM)
                sleep(.25)
                click(Constants.CLOSE)
            elif exists("no_more_mail.png", .1):
                self.state = 'CollectStart'
                Constants.MENU_BAR.click(Constants.HOME_CHRISTMAS)
            sleep(.25)
        elif self.state == 'ChallengesCollect':
            click(Constants.RECEIVE_ALL)
            sleep(.25)
            click(Constants.CLOSE)
            self.state = 'ChallengesPage2'
        elif self.state == 'ChallengesPage2':
            if exists("page_2.png", .1):
                click("page_2.png")
                sleep(.25)
                self.state = 'ChallengesCollect'
            else:
                self.state = 'End'
                Constants.MENU_BAR.click(Constants.HOME_CHRISTMAS)
        elif self.state == 'End':
            self.state = 'Start'
            self.botInfo.leveledUp = False
            self.botInfo.state = 'Quest'
            self.botInfo.questMenu.state = 'Start'

    def review_gold_card(self):
        pass
    
    def copy_deck(self):
        click(Constants.MENU)
        click("edit_deck.png")
        wait("copy_deck.png")
        click("copy_deck.png")
        click(Constants.CONFIRM)
        wait("copy_deck.png")
        click(Constants.HOME_CHRISTMAS)
