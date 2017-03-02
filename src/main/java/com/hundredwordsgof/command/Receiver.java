package com.hundredwordsgof.command;

/**
 * 
 * Receiver class, knows how to perform the operations associated with carrying
 * out a request
 *
 */
public class Receiver {

  private boolean operationPerfomed = false;

  public void action() {
    operationPerfomed = true;
  }

  protected boolean isOperationPerfomed() {
    return operationPerfomed;
  }
}
