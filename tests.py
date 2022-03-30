
import unittest
from fizzbuzz import FizzBuzz

class FizzBuzzTests(unittest.TestCase):
  def setUp(self):
    self.fizz_buzz = FizzBuzz()
    
  def test_give_1_return_1(self):
    self.assertEqual(self.fizz_buzz.int_to_string(1), '1')

  def test_give_3_return_fizz(self):
    self.assertEqual(self.fizz_buzz.int_to_string(3), 'Fizz')
  
  # Multiple only of 3 means that is not multiple of 5
  def test_give_multiple_only_of_3_return_fizz(self):
    multiples_only_of_3 = []
    for i in range(5 - 1):
      multiples_only_of_3 += list(range(1 + i, 100, 5))
    for i in multiples_only_of_3:
      self.assertEqual(self.fizz_buzz.int_to_string(i * 3), 'Fizz')

  def test_give_5_return_buzz(self):
    self.assertEqual(self.fizz_buzz.int_to_string(5), 'Buzz')

  # Multiple only of 5 means that is not multiple of 3
  def test_give_multiple_only_of_5_return_fizz(self):
    multiples_only_of_5 = []
    for i in range(3 - 1):
      multiples_only_of_5 += list(range(1 + i, 100, 3))
    for i in multiples_only_of_5:
      self.assertEqual(self.fizz_buzz.int_to_string(i * 5), 'Buzz')

  def test_give_multiple_of_3_and_5_return_fizzbuzz(self):
    self.assertEqual(self.fizz_buzz.int_to_string(15), 'FizzBuzz')

if __name__ == '__main__':
  unittest.main()
