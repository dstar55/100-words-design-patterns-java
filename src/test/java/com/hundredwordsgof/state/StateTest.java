package com.hundredwordsgof.state;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the State pattern.
 */
public class StateTest {

  @Test
  public void testState() {

    State state1 = new ConcreteState1();
    State state2 = new ConcreteState2();

    assertEquals(false, ((ConcreteState1) state1).isHandleInvoked());
    assertEquals(false, ((ConcreteState2) state2).isHandleInvoked());

    Context context = new Context();
    context.setState(state1);
    context.request();

    assertEquals(true, ((ConcreteState1) state1).isHandleInvoked());

    context.setState(state2);
    context.request();

    assertEquals(true, ((ConcreteState2) state2).isHandleInvoked());
  }
}
