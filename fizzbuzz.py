
class FizzBuzz:
  def int_to_string(self, value: int):
    if value == 5:
      return 'Buzz'
    elif value % 3 == 0:
      return 'Fizz'
    else:
      return str(value)
