import unittest

from logging import getLogger
from crystapp04c.changer import Changer

class changerTester(unittest.TestCase):
    def setUp(self) -> None:
        self._log = getLogger(__name__)
        return super().setUp()

    def test_csv_to_list(self):
        # changer = Changer("tests/.test.csv")
        # self._log.debug("First list: %s", changer.path)
        # self.assertIsInstance(changer.files, list)

        changer = Changer("tests/")
        self.assertIsInstance(changer.files, list)
        self._log.debug("test_csv_to_list: %s", changer.files)

        # self.assertRaises(FileNotFoundError, lambda: Changer("run_tests.py"))
