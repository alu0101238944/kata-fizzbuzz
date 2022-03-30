
class FizzBuzz:
  def __init__(self):
    self.fizz = 'Fizz'

  def int_to_string(self, value: int):
    if value == 3:
      return self.fizz
    return str(value)
