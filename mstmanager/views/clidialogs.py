class EpisodeEntryDialog:
    def __init__(self):
        self.prompt = '>>>'

    def init(self):
        pass

    def run(self):
        print('Please enter the episode number. Leave blank to cancel.')
        episode_number = input(self.prompt)
        episode_number = episode_number.strip()

        if episode_number == '':
            return True, '', ''

        print('Please enter the episode title. Leave blank to cancel.')
        title = input(self.prompt)
        title = title.strip()
        
        if title == '':
            return True, '', ''
        
        return False, episode_number, title
