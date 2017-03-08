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
        
        self.mainOptions = [("Add an episode", self.addEpisodeEvent.fire),
                            ("Add a media set", self.addMediaSetEvent.fire),
                            ("Add to collection", self.addToCollectionEvent.fire),
                            ("List a season", self.getSeasonToList)]

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
#                    eventToFire = self.mainOptions[index][1]
#                    eventToFire.fire()
                    method_to_execute = self.mainOptions[index][1]
                    method_to_execute()
                except IndexError:
                    print("That's not a thing.")

        print("Quitting.")

    def _is_integer(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def getSeasonToList(self):
        print("Enter the season code for which you'd like to see episodes. Leave this blank to cancel.")
        season_code = input(self.prompt)
        self.listSeasonEvent.fire(season_code)

    def show_episodes_for_selected_season(self, episodes):
        if episodes:
            print('\n' + self.div2 + '\n')
        
            for episode in episodes:
                print('{0}\t{1}'.format(episode.episode_code, episode.name))
                
            print('\n' + self.div2 + '\n')
        
