package com.hundredwordsgof.state;

/**
 * Context maintains an instance of a ConcreteState subclass that defines the
 * current state.
 *
 */
public class Context {

  private State state;

  public void request() {
    state.handle();
  }

  public void setState(State state) {
    this.state = state;
  }
}
