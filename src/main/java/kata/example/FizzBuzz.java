package kata.example;

public class FizzBuzz {
  private int state_ = -1;

  public FizzBuzz(int state) {
    this.state_ = state;
  }

  public String getState() {
    if (this.state_ % 3 == 0)
      return "Fizz";
    if (this.state_ % 5 == 0)
      return "Buzz";
    return Integer.toString(this.state_);
  }

  public void next() {
    this.state_++;
  }

  public String getNextState() {
    this.next();
    return this.getState();
  }
};
