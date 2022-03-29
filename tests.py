
import unittest
from fizzbuzz import FizzBuzz

class FizzBuzzTests(unittest.TestCase):
  def setUp(self):
    self.fizz_buzz = FizzBuzz()
    
  def test_give_1_return_1(self):
    self.assertEqual(self.fizz_buzz.int_to_string(1), '1')

  def test_give_3_return_fizz(self):
    self.assertEqual(self.fizz_buzz.int_to_string(3), 'Fizz')
  
  def test_give_multiple_of_3_return_fizz(self):
    for i in range(100):
      self.assertEqual(self.fizz_buzz.int_to_string(3 * i), 'Fizz')

  def test_give_5_return_buzz(self):
    self.assertEqual(self.fizz_buzz.int_to_string(5), 'Buzz')

if __name__ == '__main__':
  unittest.main()
