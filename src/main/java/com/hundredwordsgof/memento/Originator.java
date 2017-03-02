package com.hundredwordsgof.memento;

/**
 * 
 * Originator creates a Memento containing a snapshot of its current internal
 * state. Originator use Memento to restore its internal state.
 * 
 */
public class Originator {

  private int state;

  public void setMemento(Memento memento) {
    this.state = memento.getState();
  }

  public Memento createMemento() {
    return new Memento(this.state);
  }

  public int getState() {
    return state;
  }

  public void setState(int state) {
    this.state = state;
  }

}
