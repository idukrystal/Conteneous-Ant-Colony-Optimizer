from src.main.simulation_helper import SimulationHelper, get_weight, calculate_sd
from src.main.params import solution_archive_size, q_value, e_value
import scipy

import unittest

class TestSimulationHelperModule(unittest.TestCase):
    test_rank = 5
    test_x = 5.5
    test_list = [3, 2, 5.2, 4.1, 5.5, 3.2, 5.5]
    sd_answer =  e_value*(10/(solution_archive_size - 1))
    def test_get_weight(self):
        weight1 = get_weight(self.test_rank)
        weight2 = scipy.stats.norm.pdf(
            self.test_rank, loc=1,
            scale=solution_archive_size*q_value
        )
        self.assertEqual(weight1, round(weight2, 5))
    def test_calculate_sd(self):
        self.assertEqual(
            calculate_sd(self.test_x, self.test_list),
            self.sd_answer
        ) 
        

class TestSimulationHelperClass(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
