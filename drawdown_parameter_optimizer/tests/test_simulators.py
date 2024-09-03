from src.main.simulators import get_pwf

import unittest

from src.main.data import dataset

class TestSimulatorsModule(unittest.TestCase):
    def test_get_pwf(self):
        pwf = get_pwf(dataset, 5, 6.09, 77.1)
        self.assertEqual(round(pwf, 5), 3146.97446)


if __name__ == "__main__":
    unittest.main()
