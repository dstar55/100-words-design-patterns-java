package com.hundredwordsgof.bridge;

/**
 * 
 * ConcreteImplementatorA, implements Implementor interface
 *
 */
public class ConcreteImplementorA implements Implementor {

  public String implementation() {
    return this.getClass().getName();
  }
}
