from collections import namedtuple

EpisodeEntryResult = namedtuple('EpisodeEntryResult',
                                'canceled, episode_number, title')


class EpisodeEntryController:
    def __init__(self):
        self.view = EpisodeEntryView()

    def get_episode_info(self):
        result = self.view.show()
        if not result.canceled:
            self.validate_episode_number(result.episode_number)
            self.validate_title(result.title)
            return result

    def validate_episode_number(self, episode_number):
        """
        :param episode_number: The full episode number, including season code.
        :type episode_number: str
        :return: True if the episode number is valid, False otherwise.
        """
        if len(episode_number) >= 3:
            (seasonCode, episodeCode) = self._split_episode_number(episode_number)

            if self._is_integer(episodeCode):
                if seasonCode.isalnum():
                    return True
                else:
                    print("The characters '" + seasonCode + "' are not all alphanumeric.")
                    return False
            else:
                print("The characters " + episodeCode + " are not numeric digits.")
                return False

            # TODO: check that the new episode number doesn't exist already... not here,
            # though, this method should only validate the input.

        else:
            print("Not enough characters in the given episode number.")
            return False

    def validate_title(self, title):
        return len(title) > 0

    def _is_integer(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def _split_episode_number(self, episodeNum):
        seasonCode = episodeNum[:-2]
        episodeCode = episodeNum[-2:]
        return (seasonCode, episodeCode)

    
class EpisodeEntryView:
    def __init__(self):
        self.prompt = '--> '

    def show(self):
        print('Enter the episode number. Leave this blank to cancel.')
        episode_number = input(self.prompt)
        episode_number = episode_number.strip()
        if episode_number == '':
            return EpisodeEntryResult(True, '', '')
        
        print('Enter the episode title. Leave this blank to cancel.')
        title = input(self.prompt)
        title = title.strip()
        if title == '':
            return EpisodeEntryResult(True, '', '')

        return EpisodeEntryResult(False, episode_number, title)
