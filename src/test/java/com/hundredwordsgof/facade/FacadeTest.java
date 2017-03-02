package com.hundredwordsgof.facade;

import static org.junit.Assert.*;
import org.junit.Test;

/**
 * Test implementation of the Facade pattern.
 */
public class FacadeTest {

  @Test
  public void testFacade() throws Exception {

    // Compiler class is a facade, it can add two numbers with following
    // expression: 1 + 2
    // all other operations are not supported
    assertEquals(3, Compiler.compile("1 + 2"));

    try {
      // right operand is not a number
      Compiler.compile("1 + x");
      fail("Exception must be thrown");
    } catch (Exception e) {
    }

    try {
      // - expression is not supported
      Compiler.compile("1 - 1");
      fail("Exception must be thrown");
    } catch (Exception e) {
    }
  }
}
