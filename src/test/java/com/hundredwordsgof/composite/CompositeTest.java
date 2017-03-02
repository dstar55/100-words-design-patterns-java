package com.hundredwordsgof.composite;

import static org.junit.Assert.*;
import org.junit.Test;

/**
 * Test implementation of the Builder pattern.
 */
public class CompositeTest {

  @Test
  public void testComposite() {

    Component leaf1 = new Leaf();
    Component leaf2 = new Leaf();
    Component leaf3 = new Leaf();

    Composite composite = new Composite();
    composite.add(leaf1);
    composite.add(leaf2);
    composite.add(leaf3);

    composite.operation();

    assertEquals(leaf1, composite.getChild(0));
    assertEquals(leaf2, composite.getChild(1));
    assertEquals(leaf3, composite.getChild(2));

    composite.remove(leaf1);

    assertEquals(leaf2, composite.getChild(0));
    assertEquals(leaf3, composite.getChild(1));
  }
}
