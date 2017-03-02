package com.hundredwordsgof.builder;

import static org.junit.Assert.*;
import org.junit.Test;

/**
 * Test implementation of the Builder pattern.
 */
public class BuilderTest {

  @Test
  public void testBuilder() {

    // creates object of type ConcreteBuilder
    ConcreteBuilder builder = new ConcreteBuilder();
    // creates object of type Director
    Director director = new Director(builder);
    // Director constructs a Product
    director.construct();
    // get Product from builder
    Product product = builder.getResult();

    assertEquals(product.getPart1(), "part1");
    assertEquals(product.getPart2(), "part2");
  }
}
