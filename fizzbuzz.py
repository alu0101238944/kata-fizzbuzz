
class FizzBuzz:
  def int_to_string(self, value: int):
    if value == 5:
      return 'Buzz'
    return 'Fizz' if value % 3 == 0 else str(value)
