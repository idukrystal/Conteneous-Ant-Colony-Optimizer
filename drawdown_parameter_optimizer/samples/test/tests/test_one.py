import unittest
loader = unittest.TestLoader()
suite = loader.discover(
    start_dir="./test",
    top_level_dir="/data/data/com.termux/files/home/programming/project/FinalYearProject/drawdown_parameter_optimizer/samples/test"
)

from test.package.one import one
class OneTest(unittest.TestCase):
    def test_one(self):
        self.assertEquals(one(), "yes")
        
