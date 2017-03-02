package com.hundredwordsgof.templatemethod;

/**
 * 
 * Implements the primitive operations to carry out subclass-specific steps of
 * the algorithm.
 *
 */
public class ConcreteClass extends AbstractClass {

  public String primitiveOperation1() {
    return "Template";
  }

  public String primitiveOperation2() {
    return "Method";
  }
}
