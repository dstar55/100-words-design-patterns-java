package com.hundredwordsgof.memento;

/**
 * 
 * Caretaker responsible for the Memento's safekeeping.
 *
 */
public class Caretaker {

  private Memento memento;

  public Memento getMemento() {
    return memento;
  }

  public void setMemento(Memento memento) {
    this.memento = memento;
  }
}
