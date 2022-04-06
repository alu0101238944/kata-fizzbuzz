package kata.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class FizzBuzzTest {
  @Test
  void shouldGetStateOfRegularNumberAsString() {
    FizzBuzz fizzbuzz1 = new FizzBuzz(1);
    assertEquals("1", fizzbuzz1.getState());
    FizzBuzz fizzbuzz7 = new FizzBuzz(7);
    assertEquals("7", fizzbuzz7.getState());
  }

  @Test
  void shouldGetNextStateOfThePreviousOfRegularNumberAsString() {
    FizzBuzz fizzbuzz1 = new FizzBuzz(1);
    assertEquals("2", fizzbuzz1.getNextState());
    FizzBuzz fizzbuzz6 = new FizzBuzz(6);
    assertEquals("7", fizzbuzz6.getNextState());
  }
}
