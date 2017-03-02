package com.hundredwordsgof.chainofresponsibility;

/**
 * 
 * ConcreteHandler1 class, handles the request, can access to the next object in
 * a chain and forward the request if necessary.
 * 
 */
public class ConcreteHandler1 extends Handler {

  private boolean handleRequestInvoked = false;

  void handleRequest() {

    handleRequestInvoked = true;

    // if some condition call handleRequest on successor
    if (handleRequestInvoked) {
      succesor.handleRequest();
    }
  }

  protected boolean isHandleRequestInvoked() {
    return handleRequestInvoked;
  }
}
