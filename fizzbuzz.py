
class FizzBuzz:
  def __init__(self):
    self.fizz = 'Fizz'
    self.buzz = 'Buzz'

  def int_to_string(self, value: int):
    if value == 15:
      return 'FizzBuzz'
    if value % 3 == 0 or '3' in str(value):
      return self.fizz
    elif value % 5 == 0 or '5' in str(value):
      return self.buzz
    else:
      return str(value)
