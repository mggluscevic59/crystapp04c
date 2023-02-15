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
        right = Changer("tests/.test.csv")
        self.assertTrue(right.validate_csv_header()[0])
        wrong = Changer("tests/.test_header.csv")
        self.assertFalse(wrong.validate_csv_header()[0])
        
    def test_functionallity(self):
        lenght_before = []
        # read first CSV
        file = self.changer.get_first_valid_csv()
        if file:
            with file.open() as file:
                for line in file.readlines():
                    listed = line.split(",")
                    lenght_before.append(len(listed))
        self.changer.add_constants_to_columns()

        lenght_after = []
        file = self.changer.get_first_valid_csv()
        if file:
            self._log.debug("test_functionallity: %s",file.name)
            with file.open() as file:
                for line in file.readlines():
                    listed = line.split(",")
                    lenght_after.append(len(listed))

        self._log.debug("test_functionallity: %s, %s", lenght_before, lenght_after)

        # added two columns
        self.assertEqual(2, lenght_after[1]-lenght_before[1])
        self.assertEqual(lenght_after[1],lenght_after[2])
        
