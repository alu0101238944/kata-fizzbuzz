package kata.example;

public class FizzBuzz {
  private int state_ = -1;

  public FizzBuzz(int state) {
    this.state_ = state;
  }

  public String getState() {
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
