package com.hundredwordsgof.bridge;

/**
 * 
 * Abstraction, defines abstraction interface, maintains a reference to object
 * of type Implementator
 * 
 */
abstract class Abstraction {

  protected Implementor implementor;

  public Abstraction(Implementor implementor) {
    this.implementor = implementor;
  }

  abstract String operation();
}
