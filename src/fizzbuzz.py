
class FizzBuzz:
  def __init__(self):
    self.fizz = 'Fizz'
    self.buzz = 'Buzz'

  def int_to_string(self, value: int):
    result = ''
    if value % 3 == 0 or '3' in str(value):
      result += self.fizz
    if value % 5 == 0 or '5' in str(value):
      result += self.buzz
    return result if result != '' else str(value)

  def run(self):
    for i in range(100):
      print(self.int_to_string(i + 1))
