package com.hundredwordsgof.bridge;

import static org.junit.Assert.*;
import org.junit.Test;

/**
 * Test implementation of the Bridge pattern.
 */
public class BridgeTest {

  @Test
  public void testBuilder() {

    // creates refined abstraction with concreteimplementorA
    RefinedAbstraction refinedAbstractionA = new RefinedAbstraction(
        new ConcreteImplementorA());
    // invokes operation
    assertEquals("com.hundredwordsgof.bridge.ConcreteImplementorA",
        refinedAbstractionA.operation());

    // creates refined abstraction with concreteimplementorB
    RefinedAbstraction refinedAbstractionB = new RefinedAbstraction(
        new ConcreteImplementorB());
    // invokes operation
    assertEquals("com.hundredwordsgof.bridge.ConcreteImplementorB",
        refinedAbstractionB.operation());
  }
}
