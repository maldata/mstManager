import logging

from mstmanager.views import baseView
from mstmanager.utilities.event import Event


logger = logging.getLogger(__name__)


class CliView(baseView.BaseView):
    def __init__(self):
        super().__init__()
        self.prompt = '--> '
        divLen = 20
        self.div1 = divLen * '='
        self.div2 = divLen * '-'
        self.div3 = divLen * '.'
        
        self.mainOptions = [("Add an episode", self.addEpisodeEvent),
                            ("Add a media set", self.addMediaSetEvent),
                            ("Add to Collection", self.addToCollectionEvent)]

    def init_ui(self):
        logger.info('Initializing command-line interface.')

    def run_ui(self):
        keepGoing = True
        while keepGoing:
            print("MAIN MENU:")
            print("Enter Q to quit.")
            print(self.div1)

            for option in range(len(self.mainOptions)):
                print(str(option) + ": " + self.mainOptions[option][0])

            mainCmd = input(self.prompt)

            if len(mainCmd) > 0 and mainCmd[0].upper() == 'Q':
                keepGoing = False

            if self._is_integer(mainCmd):
                index = int(mainCmd)
                try:
                    eventToFire = self.mainOptions[index][1]
                    eventToFire.fire()
                except IndexError:
                    print("That's not a thing.")

        print("Quitting.")

    def _is_integer(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False
