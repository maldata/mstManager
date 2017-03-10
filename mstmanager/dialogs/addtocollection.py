from collections import namedtuple

AddToCollectionResult = namedtuple('AddToCollectionResult',
                                   'canceled, episode_number, media_set_id')


class AddToCollectionController:
    def __init__(self, db):
        self.db = db
        self.view = AddToCollectionView()

    def get_addition_info(self):
        result = self.view.show()
        if not result.canceled:
            e = self.validate_episode_number(result.episode_number)
            m = self.validate_media_set(result.media_set_id)
            if e and m:
                return (e, m)

    def validate_episode_number(self, episode_number):
        """
        :param episode_number: The full episode number, including season code.
        :type episode_number: str
        :return: The episode object or None
        """
        e = self.db.get_episode_by_code(episode_number)
        return e

    def validate_media_set(self, media_set_id):
        ms = self.db.get_all_media_sets()
        try:
            m = ms[media_set_id]
            return m
        except IndexError:
            return None

    def _is_integer(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    
class AddToCollectionView:
    def __init__(self):
        self.prompt = '--> '

    def show(self):
        print('Enter the episode number. Leave this blank to cancel.')
        episode_number = input(self.prompt)
        episode_number = episode_number.strip()
        if episode_number == '':
            return AddToCollectionResult(True, '', '')
        
        print('Enter the media set ID from the list below. Leave this blank to cancel.')
        media_set_id = input(self.prompt)
        media_set_id = media_set_id.strip()
        if media_set_id == '':
            return AddToCollectionResult(True, '', '')

        return AddToCollectionResult(False, episode_number, media_set_id)
