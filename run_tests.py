import unittest

from logging import basicConfig, DEBUG
from tests.test_changer import changerTester

if __name__ == "__main__":
    basicConfig(level=DEBUG)
    # 0=quiet; 1=default; 2=verbose
    unittest.main(verbosity=2)
