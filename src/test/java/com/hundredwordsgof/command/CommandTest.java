package com.hundredwordsgof.command;

import static org.junit.Assert.*;
import org.junit.Test;

/**
 * Test implementation of the Test pattern.
 */
public class CommandTest {

  @Test
  public void testCommand() {

    Receiver receiver = new Receiver();
    Command command = new ConcreteCommand(receiver);
    Invoker invoker = new Invoker(command);

    // operation on receiver is not performed
    assertEquals(false, receiver.isOperationPerfomed());

    // this will invoke method action on receiver
    invoker.execute();

    // operation on receiver is performed
    assertEquals(true, receiver.isOperationPerfomed());
  }
}
