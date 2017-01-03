from views import baseView


class CliView(baseView.BaseView):
    def __init__(self):
        super().__init__()
        self.prompt = '>>> '
        divLen = 20
        self.div1 = divLen * '='
        self.div2 = divLen * '-'
        self.div3 = divLen * '.'
        self.mainOptions = [("Add an episode", self.addEpisodeEvent),
                            ("Add a media set", self.addMediaSetEvent),
                            ("Add to Collection", self.addToCollectionEvent)]

    def init_ui(self):
        pass

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

    def show_dialog_get_episode(self):
        """
        :return: A tuple (ok, seasonCode, episodeCode). seasonCode is a string representing the
        season code (from the user). episodeCode is the episode number string from the user.
        ok is true if these comprise a valid episode number. ok is false if the user cancels
        or enters an invalid episode number string.
        """
        print("Enter the episode number. The last two characters must be digits.")
        print("There must be at least one alphanumeric character before those two digits.")
        print("These leading alphanumeric characters will be considered the season code.")
        epNum = input(self.prompt)
        (seasonCode, episodeCode) = self._split_episode_number(epNum)

        if self.validate_episode_number(epNum):
            return (True, seasonCode, episodeCode)
        else:
            return (False, seasonCode, episodeCode)

    # TODO: this is business logic that does not belong here
    def validate_episode_number(self, episodeNum):
        """
        :param episodeNum: A string representing the episode number. This is user input.
        :return: true if the episode number is valid, false otherwise.
        """
        if len(episodeNum) >= 3:
            (seasonCode, episodeCode) = self._split_episode_number(episodeNum)

            if self._is_integer(episodeCode):
                if seasonCode.isalnum():
                    return True
                else:
                    print("The characters '" + seasonCode + "' are not all alphanumeric.")
                    return False
            else:
                print("The characters " + episodeCode + " are not numeric digits.")
                return False

            # TODO: check that the new episode number doesn't exist already... not here, though,
            # this method should only validate the input

        else:
            print("Not enough characters in the given episode number.")
            return False

    # TODO: this is business logic that does not belong here
    def _is_integer(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    # TODO: this is business logic that does not belong here
    def _split_episode_number(self, episodeNum):
        seasonCode = episodeNum[:-2]
        episodeCode = episodeNum[-2:]
        return (seasonCode, episodeCode)
