import unittest

from logging import basicConfig, DEBUG, INFO
# from tests.test_changer import changerTester
from tests.unit_04_revisor import revisorUnit

if __name__ == "__main__":
    basicConfig(level=DEBUG)
    # 0=quiet; 1=default; 2=verbose
    unittest.main(verbosity=0)
