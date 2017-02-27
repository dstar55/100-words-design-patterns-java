package com.hundredwordsgof.abstractfactory;

/**
 * 
 * ConcreteFactory1, implements creation of the concrete Product1 objects
 *
 */
public class ConcreteFactory1 implements AbstractFactory {

  public AbstractProductA createProductA() {
    return new ProductA1();
  }

  public AbstractProductB createProductB() {
    return new ProductB1();
  }
}
