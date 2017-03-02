package com.hundredwordsgof.observer;

/**
 * ConcreteSubject stores state of interest to ConcreteObserver objects, sends a
 * notification to its observers when its state changes.
 *
 */
public class ConcreteSubject extends Subject {

  private int state;

  public int getState() {
    return state;
  }

  public void setState(int state) {
    this.state = state;
    this.notifyObervers();
  }
}
