package com.hundredwordsgof.memento;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the Memento pattern.
 */
public class MementoTest {

  @Test
  public void testVisitor() {

    // init state of the Originator
    Originator originator = new Originator();
    originator.setState(1);

    assertEquals(1, originator.getState());

    // Caretaker stores current state of the Originator
    Caretaker caretaker = new Caretaker();
    caretaker.setMemento(originator.createMemento());

    // change a Originator's state
    originator.setState(2);
    assertEquals(2, originator.getState());

    // undo Originator's initial state
    originator.setMemento(caretaker.getMemento());
    assertEquals(1, originator.getState());
  }
}
