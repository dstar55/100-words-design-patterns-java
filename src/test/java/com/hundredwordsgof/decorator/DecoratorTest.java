package com.hundredwordsgof.decorator;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test Decorator pattern.
 */
public class DecoratorTest {

  @Test
  public void testDecorator() {

    Component component = new ConcreteComponent();

    Decorator decoratorA = new ConcreteDecoratorA();
    decoratorA.setComponent(component);
    decoratorA.operation();

    assertEquals(true, ((ConcreteDecoratorA) decoratorA).isState());

    Decorator decoratorB = new ConcreteDecoratorB();
    decoratorB.setComponent(component);

    assertEquals(false,
        ((ConcreteDecoratorB) decoratorB).isBehaviorMethodInvoked());

    decoratorB.operation();

    assertEquals(true,
        ((ConcreteDecoratorB) decoratorB).isBehaviorMethodInvoked());
  }
}
