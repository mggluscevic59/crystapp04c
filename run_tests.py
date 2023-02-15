import unittest

from logging import basicConfig, DEBUG, INFO
from tests.test_changer import changerTester

if __name__ == "__main__":
    basicConfig(level=INFO)
    # 0=quiet; 1=default; 2=verbose
    unittest.main(verbosity=0)
