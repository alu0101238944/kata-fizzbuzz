
class FizzBuzz:
  def __init__(self):
    self.fizz = 'Fizz'

  def int_to_string(self, value: int):
    if value % 3 == 0 or '3' in str(value):
      return self.fizz
    if value == 5:
      return 'Buzz'
    return str(value)
