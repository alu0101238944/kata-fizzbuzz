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
    FizzBuzz fizzbuzz3 = new FizzBuzz(3);
    assertEquals("Fizz", fizzbuzz3.getState());
    FizzBuzz fizzbuzz102 = new FizzBuzz(102);
    assertEquals("Fizz", fizzbuzz102.getState());
  }

  @Test
  void shouldGetStateOfMultipleOf5AsBuzz() {
    FizzBuzz fizzbuzz5 = new FizzBuzz(5);
    assertEquals("Buzz", fizzbuzz5.getState());
    FizzBuzz fizzbuzz110 = new FizzBuzz(110);
    assertEquals("Buzz", fizzbuzz110.getState());
  }
}
