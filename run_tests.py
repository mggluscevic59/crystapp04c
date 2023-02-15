import unittest

from logging import basicConfig, DEBUG
from tests.test_changer import changerTester

if __name__ == "__main__":
    basicConfig(level=DEBUG)
    unittest.main()
