from ntop import some
import unittest

class AddTestCase(unittest.TestCase):
  def setUp(self) -> None:
    self.args = (100, 99)
    return super().setUp()

  def tearDown(self) -> None:
    self.args = None
    return super().tearDown()

  def test_add(self):
    expected = 199;
    result = some.add(*self.args);
    self.assertEqual(expected, result);
        
suite = unittest.TestSuite()
suite.addTest(AddTestCase('test_add'))

unittest.TextTestRunner(verbosity=2).run(suite)