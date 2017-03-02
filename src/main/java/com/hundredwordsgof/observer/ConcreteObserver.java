package com.hundredwordsgof.observer;

/**
 * ConcreteObserver maintains a reference to a ConcreteSubject object, stores
 * state that should stay consistent with the subject's, implements the Observer
 * updating interface to keep its state consistent with the subject's.
 *
 */
public class ConcreteObserver implements Observer {

  private int observerState;

  private ConcreteSubject subject;

  public ConcreteObserver(ConcreteSubject subject) {
    this.subject = subject;
  }

  public void update() {
    observerState = subject.getState();
  }

  protected int getObserverState() {
    return observerState;
  }
}
