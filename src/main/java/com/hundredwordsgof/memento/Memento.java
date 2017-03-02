package com.hundredwordsgof.memento;

/**
 * 
 * Memento stores internal state of the Originator object, protects against
 * access by objects other than the Originator.
 *
 */
public class Memento {

  private int state;

  public Memento(int state) {
    this.state = state;
  }

  public int getState() {
    return state;
  }
}
