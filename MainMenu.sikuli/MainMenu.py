from sikuli import *

import Constants
reload(Constants)

class MainMenu(object):
    states = [
        'Start',
        'MailStart',
        'MailCollect',
        'ChallengesStart',
        'ChallengesCollect',
        'End'
    ]

    def __init__(self, botInfo):
        self.botInfo = botInfo;
        self.state = 'Start'

    def run(self):
        if self.state == 'Start':
            if self.botInfo.leveledUp:
                self.state = 'Mail'
        elif self.state == 'MailStart':
            if exists("mail_found.png", .25):
                click("mail_found.png")
                self.state = 'MailCollect'
        elif self.state == 'MailCollect':
            if exists(Constants.RECEIVE_ALL, .1):
                click(Constants.RECEIVE_ALL)
                click(Constants.CONFIRM)
                click(Constants.CLOSE)
            elif exists("no_more_mail.png", .1):
                self.state = 'ChallengesStart'
                Constants.MENU_BAR.click(Constants.HOME)
        elif self.state == 'ChallengesStart':
            pass
        elif self.state == 'End':
            pass

            self.botInfo.leveledUp = False
            self.check()
            self.botInfo.state = 'Battle'
            self.botInfo.battleMenu.state = 'Start'
            Constants.MENU_BAR.click(Constants.HOME)
        else:
            self.botInfo.state = 'Quest'
            self.botInfo.questMenu.state = 'Start'
            Constants.MENU_BAR.click(Constants.HOME)

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
            self._collect_challenges()
    
    def _collect_challenges(self):
        click(Constants.RECEIVE_ALL)
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
