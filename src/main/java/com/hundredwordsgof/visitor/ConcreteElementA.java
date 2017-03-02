package com.hundredwordsgof.visitor;

/**
 * Implements accept operation.
 *
 */
public class ConcreteElementA implements Element {

  private int counter = 0;

  public void accept(Visitor visitor) {
    visitor.visitConcreteElementA(this);
  }

  public void operationA() {
    counter++;
  }

  protected int getCounter() {
    return counter;
  }
}
