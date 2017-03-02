package com.hundredwordsgof.bridge;

/**
 * 
 * ConcreteImplementatorB, implements Implementor interface
 *
 */
public class ConcreteImplementorB implements Implementor {

  public String implementation() {
    return this.getClass().getName();
  }
}
