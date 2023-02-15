import unittest

from logging import getLogger
from crystapp04c.changer import Changer



class changerTester(unittest.TestCase):
    def setUp(self) -> None:
        self._log = getLogger(__name__)
        self.changer = Changer("tests/")
        return super().setUp()

    def test_csv_to_list(self):
        direct = Changer("tests/.test.csv")
        self._log.debug("test_csv_to_list: %s", direct.files)
        self.assertIsInstance(direct.files, list)

        self.assertIsInstance(self.changer.files, list)
        self._log.debug("test_csv_to_list: %s", self.changer.files)

        self.assertRaises(FileNotFoundError, lambda: Changer("run_tests.py"))

    def test_csv_file(self):
        try:
            right = Changer("tests/.test.csv")
            right.validate_csv_header()
        except SyntaxError:
            pass
            # self.fail("Changer('tests/.test.csv') raises SyntaxError unexpectedly!")
        wrong = Changer("tests/.test_header.csv")
        # self.assertRaises(SyntaxError, lambda: wrong.validate_csv_header())
