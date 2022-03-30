
class FizzBuzz():
  def to_fizzbuzz(self, number: int):
    result = ''
    if self.is_fizz(number):
      result += 'Fizz'
    if self.is_buzz(number):
      result += 'Buzz'
    return str(number) if result == '' else result
    
  def is_fizz(self, number: int):
    return self.get_recursive_digit_sum(number) in [3, 6, 9] or '3' in str(number)
    
  def get_recursive_digit_sum(self, number):
    return (number if number < 10
      else self.get_recursive_digit_sum(self.get_digit_sum(number))
    )

  def get_digit_sum(self, number: int):
    digit_sum = 0
    while number > 0:
      digit_sum += number % 10
      number //= 10
    return digit_sum

  def is_buzz(self, number: int):
    return number % 10 in [0, 5] or '5' in str(number)
