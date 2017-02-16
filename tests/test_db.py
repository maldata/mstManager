from . import context

import unittest
import mstmanager.db.engine as db
import mstmanager.db.models as models


class EmptyDbTestSuite(unittest.TestCase):
    def setUp(self):
        try:
            os.remove('./mst3k.db')
        except OSError:
            pass

        self.engine = db.DbEngine()
        self.engine.initialize()

    def tearDown(self):
        db_file = self.engine.deinitialize()

    def test_add_season(self):
        s1 = self.engine.add_or_get_season('K')
        s2 = self.engine.add_or_get_season('1')
        s3 = self.engine.add_or_get_season('K')

        self.assertEqual(s1, s3)
        self.assertNotEqual(s1, s2)
        self.assertEqual(len(self.engine.get_all_seasons()), 2)

    def test_add_episode(self):
        e1 = self.engine.add_episode('K07', 'Gamera vs. Zigra')
        es = self.engine._session.query(models.Episode).all()
        self.assertEqual(len(es), 1)
        self.assertEqual(e1, es[0])

    def test_add_media_set(self):
        m1 = self.engine.add_media_set('DAP DVD')
        ms = self.engine._session.query(models.MediaSet).all()
        self.assertEqual(len(ms), 1)
        self.assertEqual(m1, ms[0])

    def test_get_seasons(self):
        s1 = self.engine.add_or_get_season('K')
        s2 = self.engine.add_or_get_season('1')
        s3 = self.engine.add_or_get_season('K')
        s4 = self.engine.add_or_get_season('2')

        self.assertEqual(self.engine.get_all_season_numbers(), ['K', '1', '2'])
        

class PopulatedDbTestSuite(unittest.TestCase):
    def setUp(self):
        try:
            os.remove('./mst3k.db')
        except OSError:
            pass

        self.engine = db.DbEngine()
        self.engine.initialize()

    def tearDown(self):
        db_file = self.engine.deinitialize()

    def test_create(self):
        pass


if __name__ == '__main__':
    unittest.main()
    
