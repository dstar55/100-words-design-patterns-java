package com.hundredwordsgof.abstractfactory;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the AbstractFactory pattern.
 */
public class AbstractFactoryTest {

  @Test
  public void testAbstractFactory() {

    AbstractFactory abstractFactory1 = new ConcreteFactory1();
    AbstractFactory abstractFactory2 = new ConcreteFactory2();

    assertEquals("com.hundredwordsgof.abstractfactory.ProductA1",
        abstractFactory1.createProductA().getClass().getName());
    assertEquals("com.hundredwordsgof.abstractfactory.ProductB1",
        abstractFactory1.createProductB().getClass().getName());

    assertEquals("com.hundredwordsgof.abstractfactory.ProductA2",
        abstractFactory2.createProductA().getClass().getName());
    assertEquals("com.hundredwordsgof.abstractfactory.ProductB2",
        abstractFactory2.createProductB().getClass().getName());
  }
}
