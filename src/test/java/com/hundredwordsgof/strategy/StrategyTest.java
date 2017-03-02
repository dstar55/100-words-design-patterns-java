package com.hundredwordsgof.strategy;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the Strategy pattern.
 */
public class StrategyTest {

  @Test
  public void testStrategy() {

    Context context = new Context(new ConcreteStrategyA());
    assertEquals("Go to airport with ConcreteStrategyA, take a taxi",
        context.contextInterface());

    context = new Context(new ConcreteStrategyB());
    assertEquals("Go to airport with ConcreteStrategyB, take a bus",
        context.contextInterface());

    context = new Context(new ConcreteStrategyC());
    assertEquals("Go to airport with ConcreteStrategyC, take a metro",
        context.contextInterface());
  }
}
