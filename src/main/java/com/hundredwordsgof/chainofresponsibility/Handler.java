package com.hundredwordsgof.chainofresponsibility;

/**
 * 
 * Handler interface, declares an interface for request handling
 *
 */
abstract class Handler {

  protected Handler succesor;

  abstract void handleRequest();

  public void setSuccesor(Handler succesor) {
    this.succesor = succesor;
  }
}
