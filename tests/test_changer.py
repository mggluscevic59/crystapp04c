import unittest

from logging import getLogger
from crystapp04c.changer import Changer
from crystapp04c.constants import HEADER, TEST


class changerTester(unittest.TestCase):
    def setUp(self) -> None:
        self._log = getLogger(__name__)
        self.changer = Changer("tests/")
        # mock test.csv & test_no_header.csv
        with open("tests/.test.csv", mode="w") as file:
            file.writelines([HEADER,TEST])
        with open("tests/.test_no_header.csv", mode="w") as file:
            file.writelines([TEST])
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
        wrong = Changer("tests/.test_no_header.csv")
        self.assertFalse(wrong.validate_csv_header()[0])

    def test_functionallity(self):
        lenght_before = []
        # read first CSV
        file_path = self.changer.get_first_valid_csv()
        if file_path:
            self._log.info("test_functionallity: %s",file_path.name)
            with file_path.open() as file:
                for line in file.readlines():
                    listed = line.split(",")
                    lenght_before.append(len(listed))

        # add two new lines at #1 & #3 position
        self.changer.add_constants_to_columns()

        lenght_after = []
        # file = self.changer.get_first_valid_csv()
        if file_path:
            self._log.info("test_functionallity: %s",file_path.name)
            with file_path.open() as file:
                for line in file.readlines():
                    listed = line.split(",")
                    lenght_after.append(len(listed))

        self._log.info("test_functionallity: %s, %s", lenght_before, lenght_after)

        # run some tests
        self.assertEqual(2, lenght_after[1]-lenght_before[1])
        self.assertEqual(lenght_after[1],lenght_after[2])
