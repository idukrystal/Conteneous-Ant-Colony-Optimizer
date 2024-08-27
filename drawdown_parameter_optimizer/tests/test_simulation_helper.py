from src.main.simulation_helper import SimulationHelper
from src.main.params import solution_archive_size, q_value
import scipy

import unittest
"""
loader = unittest.TestLoader()
suite = loader.discover(
    start_dir=".",
    top_level_dir="/data/data/com.termux/files/home/programming/project/FinalYearProject/drawdown_parameter_optimizer"
)"""

test_rank = 5

class TestSimulationHelper(unittest.TestCase):
    def setUp(self):
        self.simulation_helper = SimulationHelper()
        
    def test_get_weight(self):
        weight1 = self.simulation_helper.get_weight(test_rank)
        weight2 = scipy.stats.norm.pdf(
            test_rank, loc=1,
            scale=solution_archive_size*q_value
        )
        self.assertEqual(weight1, round(weight2, 5))
        


if __name__ == "__main__":
    unittest.main()
