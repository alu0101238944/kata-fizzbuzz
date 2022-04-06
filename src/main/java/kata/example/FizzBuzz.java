package kata.example;

public class FizzBuzz {
  private int state_ = -1;

  public FizzBuzz(int state) {
    this.state_ = state;
  }

  public String getState() {
    String string = "";
    if (this.state_ % 3 == 0)
      string += "Fizz";
    if (this.state_ % 5 == 0)
      string += "Buzz";
    return string == "" ? Integer.toString(this.state_) : string;
  }

  public void next() {
    this.state_++;
  }

  public String getNextState() {
    this.next();
    return this.getState();
  }
};
