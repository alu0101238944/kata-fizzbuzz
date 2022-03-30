
import unittest
from io import StringIO
import sys
from fizzbuzz import FizzBuzz

class FizzBuzzTests(unittest.TestCase):
  def setUp(self):
    self.fizz_buzz = FizzBuzz()
    
  def test_give_1_return_1(self):
    self.assertEqual(self.fizz_buzz.int_to_string(1), '1')

  def test_give_3_return_fizz(self):
    self.assertEqual(self.fizz_buzz.int_to_string(3), 'Fizz')

  # Multiple only of 3 means that is not multiple of 5
  def test_give_multiple_only_of_3_or_has_3_in_it_return_fizz(self):
    multiples_only_of_3 = []
    for i in range(5 - 1):
      multiples_only_of_3 += list(range(1 + i, 100, 5))
    for i in multiples_only_of_3:
      # If has a 3 return Fizz
      if '3' in str(i) and '5' not in str(i):
        self.assertEqual(self.fizz_buzz.int_to_string(i), 'Fizz')
      # Else multiple of 3 return Fizz
      elif '5' not in str(i * 3):
        self.assertEqual(self.fizz_buzz.int_to_string(i * 3), 'Fizz')

  def test_give_5_return_buzz(self):
    self.assertEqual(self.fizz_buzz.int_to_string(5), 'Buzz')

    # Multiple only of 5 means that is not multiple of 3
  def test_give_multiple_only_of_5_or_has_5_in_it_return_fizz(self):
    multiples_only_of_5 = []
    for i in range(3 - 1):
      multiples_only_of_5 += list(range(1 + i, 100, 3))
    for i in multiples_only_of_5:
      # If has a 5 return Fizz
      if '5' in str(i) and '3' not in str(i):
        self.assertEqual(self.fizz_buzz.int_to_string(i), 'Buzz')
      # Else multiple of 5 return Fizz
      elif '3' not in str(i * 5):
        self.assertEqual(self.fizz_buzz.int_to_string(i * 5), 'Buzz')

  def test_give_15_return_fizzbuzz(self):
    self.assertEqual(self.fizz_buzz.int_to_string(15), 'FizzBuzz')

  def test_fizzbuzz_number_return_fizzbuzz(self):
    for i in range(100):
      if (i % 3 == 0 or '3' in str(i)) and (i % 5 == 0 or '5' in str(i)):
        self.assertEqual(self.fizz_buzz.int_to_string(i), 'FizzBuzz')
      else:
        self.assertEqual(self.fizz_buzz.int_to_string(i * 3 * 5), 'FizzBuzz')

  def test_main_function_fizzbuzz(self):
    captured_output = StringIO()
    sys.stdout = captured_output
    self.fizz_buzz.run()
    sys.stdout = sys.__stdout__
    print('Captured', captured_output.getvalue())

if __name__ == '__main__':
  unittest.main()
