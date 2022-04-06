package kata.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class FizzBuzzTest {
  @Test
  void shouldGetStateOfRegularNumber() {
    FizzBuzz fizzbuzz = new FizzBuzz(1);
    assertEquals("1", fizzbuzz.getState());
  }
}
