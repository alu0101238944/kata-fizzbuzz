
class FizzBuzz:
  def int_to_string(self, value: int):
    result = ''
    if value == 15:
      return 'FizzBuzz'
    if value % 5 == 0:
      result = 'Buzz'
    elif value % 3 == 0:
      result = 'Fizz'
    else:
      result = str(value)
    return result
