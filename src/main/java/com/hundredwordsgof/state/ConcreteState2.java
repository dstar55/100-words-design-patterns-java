package com.hundredwordsgof.state;

/**
 * ConcreteState2 implements a behavior associated with a state of the Context.
 *
 */
public class ConcreteState2 implements State {

  private boolean handleInvoked = false;

  public void handle() {
    this.handleInvoked = true;
  }

  protected boolean isHandleInvoked() {
    return handleInvoked;
  }
}
