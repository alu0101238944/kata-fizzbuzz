package kata.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class FizzBuzzTest {
  @Test
  void shouldGetStateOfRegularNumberAsItsString() {
    FizzBuzz fizzbuzz1 = new FizzBuzz(1);
    assertEquals("1", fizzbuzz1.getState());
    FizzBuzz fizzbuzz7 = new FizzBuzz(7);
    assertEquals("7", fizzbuzz7.getState());
  }

  @Test
  void shouldGetNextStateOfThePreviousOfRegularNumberAsItsString() {
    FizzBuzz fizzbuzz1 = new FizzBuzz(1);
    assertEquals("2", fizzbuzz1.getNextState());
    FizzBuzz fizzbuzz6 = new FizzBuzz(6);
    assertEquals("7", fizzbuzz6.getNextState());
  }

  @Test
  void shouldGetStateOfMultipleOf3AsFizz() {
    FizzBuzz fizzbuzz1 = new FizzBuzz(3);
    assertEquals("Fizz", fizzbuzz1.getState());
    FizzBuzz fizzbuzz6 = new FizzBuzz(102);
    assertEquals("Fizz", fizzbuzz6.getState());
  }
}
