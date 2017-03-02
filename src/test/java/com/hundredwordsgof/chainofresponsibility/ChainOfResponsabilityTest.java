package com.hundredwordsgof.chainofresponsibility;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the ChainOfResponsability pattern.
 */
public class ChainOfResponsabilityTest {

  @Test
  public void testChainOfResponsability() throws Exception {

    // create two handlers
    Handler concreteHandler1 = new ConcreteHandler1();
    Handler concreteHandler2 = new ConcreteHandler2();
    // connect handler in chain
    concreteHandler1.setSuccesor(concreteHandler2);

    // handleRequest on handlers is not invoked
    assertEquals(false,
        ((ConcreteHandler1) concreteHandler1).isHandleRequestInvoked());
    assertEquals(false,
        ((ConcreteHandler2) concreteHandler2).isHandleRequestInvoked());

    concreteHandler1.handleRequest();

    // handleRequest on handlers is invoked
    assertEquals(true,
        ((ConcreteHandler1) concreteHandler1).isHandleRequestInvoked());
    assertEquals(true,
        ((ConcreteHandler2) concreteHandler2).isHandleRequestInvoked());
  }
}
