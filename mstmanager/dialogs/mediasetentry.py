from collections import namedtuple

MediaSetEntryResult = namedtuple('MediaSetEntryResult',
                                 'canceled, media_set_name')


class MediaSetEntryController:
    def __init__(self):
        self.view = MediaSetEntryView()

    def get_media_set_name(self):
        result = self.view.show()
        if not result.canceled:
            self.validate_media_set_name(result.media_set_name)
            return result

    def validate_media_set_name(self, media_set_name):
        return len(media_set_name) > 0

    
class MediaSetEntryView:
    def __init__(self):
        self.prompt = '--> '

    def show(self):
        print('Enter the name of the media set. Leave this blank to cancel.')
        media_set_name = input(self.prompt)
        media_set_name = media_set_name.strip()
        if media_set_name == '':
            return MediaSetEntryResult(True, '')
        
        return MediaSetEntryResult(False, media_set_name)
