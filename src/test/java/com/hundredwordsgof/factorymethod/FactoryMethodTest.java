package com.hundredwordsgof.factorymethod;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the FactoryMethod pattern.
 */
public class FactoryMethodTest {

  @Test
  public void testFactoryMethod() {

    Creator factory = new ConcreteCreator();

    Product productA = factory.factoryMethod("A");
    Product productB = factory.factoryMethod("B");

    assertEquals("com.hundredwordsgof.factorymethod.ConcreteProductA",
        productA.getClass().getName());
    assertEquals("com.hundredwordsgof.factorymethod.ConcreteProductB",
        productB.getClass().getName());

    assertEquals(null, factory.factoryMethod(""));
  }
}
