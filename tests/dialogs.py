import unittest

import mstmanager.dialogs.episodeentry

class EpisodeEntryTestSuite(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_validate_episode_number(self):
        ctrlr = mstmanager.dialogs.episodeentry.EpisodeEntryController()
        episode_number = ''
        self.assertFalse(ctrlr.validate_episode_number(episode_number))
        episode_number = ' '
        self.assertFalse(ctrlr.validate_episode_number(episode_number))
        episode_number = '1'
        self.assertFalse(ctrlr.validate_episode_number(episode_number))
        episode_number = '12'
        self.assertFalse(ctrlr.validate_episode_number(episode_number))
        episode_number = '             '
        self.assertFalse(ctrlr.validate_episode_number(episode_number))
        episode_number = '   34a'
        self.assertFalse(ctrlr.validate_episode_number(episode_number))
        episode_number = '       21'
        self.assertFalse(ctrlr.validate_episode_number(episode_number))
        episode_number = 'AB21'
        self.assertTrue(ctrlr.validate_episode_number(episode_number))


    def test_validate_title(self):
        ctrlr = mstmanager.dialogs.episodeentry.EpisodeEntryController()
        title = ''
        self.assertFalse(ctrlr.validate_title(title))
        title = '1'
        self.assertTrue(ctrlr.validate_title(title))

        
if __name__ == '__main__':
    unittest.main()
    
