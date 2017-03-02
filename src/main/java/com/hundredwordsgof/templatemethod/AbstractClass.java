package com.hundredwordsgof.templatemethod;

/**
 * Defines interfaces for primitive operations. Implements algorithm.
 * 
 *
 */
abstract class AbstractClass {

  /**
   * Template method, implementation of algorithm which consists of
   * primitiveOperations
   * 
   * @return result of the primitive operations
   */
  public String templateMethod() {
    return this.primitiveOperation1() + this.primitiveOperation2();
  }

  abstract String primitiveOperation1();

  abstract String primitiveOperation2();
}
