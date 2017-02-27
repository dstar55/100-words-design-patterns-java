package com.hundredwordsgof.mediator;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

/**
 * Test implementation of the Mediator pattern.
 */
public class MediatorTest {

  @Test
  public void testMediator() {

    ConcreteMediator mediator = new ConcreteMediator();

    Colleague colleague1 = new ConcreteColleague1(mediator);
    Colleague colleague2 = new ConcreteColleague2(mediator);

    mediator.addColleague(colleague1);
    mediator.addColleague(colleague2);

    colleague1.notifyColleague("Hello from ConcreteColleague1");
    colleague2.notifyColleague("Hello from ConcreteColleague2");

    assertEquals("Hello from ConcreteColleague2",
        ((ConcreteColleague1) colleague1).getReceivedMessage());
    assertEquals("Hello from ConcreteColleague1",
        ((ConcreteColleague2) colleague2).getReceivedMessage());
  }
}
