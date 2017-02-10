from context import *

import unittest
import mstmanager.db.engine as db


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
    
