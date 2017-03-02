package com.hundredwordsgof.prototype;

public class ConcretePrototype extends Prototype {

  /**
   * Implements Prototype, meaning clone method.
   */
  public Prototype copyMe() throws CloneNotSupportedException {
    return (Prototype) this.clone();
  }
}
