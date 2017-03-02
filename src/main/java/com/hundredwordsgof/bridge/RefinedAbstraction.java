package com.hundredwordsgof.bridge;

/**
 * 
 * Refined Abstraction, extends the interface defined by Abstraction
 *
 */
public class RefinedAbstraction extends Abstraction {

  public RefinedAbstraction(Implementor implementor) {
    super(implementor);
  }

  public String operation() {
    return this.implementor.implementation();
  }
}
