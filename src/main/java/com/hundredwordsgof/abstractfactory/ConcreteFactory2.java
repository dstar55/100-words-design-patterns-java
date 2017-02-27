package com.hundredwordsgof.abstractfactory;

/**
 * 
 * ConcreteFactory2, implements creation of the concrete Product2 objects
 *
 */
public class ConcreteFactory2 implements AbstractFactory {

  public AbstractProductA createProductA() {
    return new ProductA2();
  }

  public AbstractProductB createProductB() {
    return new ProductB2();
  }
}
