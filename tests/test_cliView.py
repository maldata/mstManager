import unittest
from unittest.mock import patch

from context import *

import mstmanager.views.cliView

# app = views.cliView.CliView()
# app.run_ui()
#


class CliTestSuite(unittest.TestCase):
    def setUp(self):
        self.view = mstmanager.views.cliView.CliView()
        self.view.init_ui()

    def tearDown(self):
        pass

    def test_entering_nothing(self):
        print("Don't enter anything, just hit enter:\n")
        result = self.view.show_dialog_get_episode()
        self.assertFalse(result[0])
        self.assertIsNone(result[1])
        self.assertIsNone(result[2])

    @patch
    def test_enter_K07(self):
        print("Enter K07 and hit enter:\n")
        result = self.view.show_dialog_get_episode()
        self.assertTrue(result[0])
        self.assertEqual(result[1], 'K')
        self.assertEqual(result[2], '07')

    def test_enter_1013(self):
        print("Enter 1013 and hit enter:\n")
        result = self.view.show_dialog_get_episode()
        self.assertTrue(result[0])
        self.assertEqual(result[1], '10')
        self.assertEqual(result[2], '13')

    def test_enter_A7(self):
        print("Enter A7 and hit enter:\n")
        result = self.view.show_dialog_get_episode()
        self.assertFalse(result[0])

    
        

if __name__ == '__main__':
    unittest.main()
