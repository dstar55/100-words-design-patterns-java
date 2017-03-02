package com.hundredwordsgof.templatemethod;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the Template Method pattern.
 */
public class TemplateTest {

  @Test
  public void testTemplate() {

    ConcreteClass template = new ConcreteClass();
    assertEquals("TemplateMethod", template.templateMethod());
  }
}
