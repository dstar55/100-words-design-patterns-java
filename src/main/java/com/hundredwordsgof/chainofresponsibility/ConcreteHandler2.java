package com.hundredwordsgof.chainofresponsibility;

/**
 * 
 * ConcreteHandler2 class, handles the request, can access to the next object in
 * a chain and forward the request if necessary.
 * 
 */
public class ConcreteHandler2 extends Handler {

  private boolean handleRequestInvoked = false;

  void handleRequest() {
    handleRequestInvoked = true;
  }

  protected boolean isHandleRequestInvoked() {
    return handleRequestInvoked;
  }
}
