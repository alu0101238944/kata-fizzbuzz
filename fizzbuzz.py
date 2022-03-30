
class FizzBuzz:
  def int_to_string(self, value: int):
    result = ''
    if value % 3 == 0:
      result += 'Fizz'
    if value % 5 == 0:
      result += 'Buzz'
    if result == '':
      result += str(value)
    return result
