package com.hundredwordsgof.visitor;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the Visitor pattern.
 */
public class VisitorTest {

  @Test
  public void testVisitor() {

    // Setup structure
    ObjectStructure objectStructure = new ObjectStructure();

    ConcreteElementA concreteElementA = new ConcreteElementA();
    ConcreteElementB concreteElementB = new ConcreteElementB();

    objectStructure.add(concreteElementA);
    objectStructure.add(concreteElementB);

    // Create visitor objects
    ConcreteVisitor1 v1 = new ConcreteVisitor1();
    ConcreteVisitor2 v2 = new ConcreteVisitor2();

    // Structure accepting visitors
    objectStructure.acceptAll(v1);
    assertEquals(1, concreteElementA.getCounter());
    assertEquals(1, concreteElementB.getCounter());

    objectStructure.acceptAll(v2);
    assertEquals(2, concreteElementA.getCounter());
    assertEquals(2, concreteElementB.getCounter());

    // lets remove second element from objectStructure
    Element element = objectStructure.getChild(1);
    objectStructure.remove(element);
    // now visit all elements on objectStructure
    objectStructure.acceptAll(v1);
    assertEquals(3, concreteElementA.getCounter());

    // this element was removed from objectStructure so counter should remain
    // the same as before last invocation of the acceptAll
    assertEquals(2, concreteElementB.getCounter());

  }
}
