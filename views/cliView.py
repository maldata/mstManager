from views import baseView
from views import cliMenu


class CliView(baseView.BaseView):
    def __init__(self):
        self.currentMenu = None

    def transition(self, nextMenu):
        self.currentMenu = nextMenu
        self.currentMenu.list()
