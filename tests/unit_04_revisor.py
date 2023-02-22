import unittest

from pathlib import Path
from crystapp04c.revisor import Revisor

class revisorUnit(unittest.TestCase):
    def test_mockup(self):
        # arrange
        destination = "tests/"
        map = Path(destination)
        map_list = [child for child in map.iterdir()]
        tested = Revisor(destination)

        # act
        map_list.sort()
        tested.map.sort()
        rez = ( map_list == tested.map )

        # assert
        self.assertTrue(rez)
        # self.assertTrue(False)
