package com.hundredwordsgof.iterator;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the Iterator pattern.
 */
public class IteratorTest {

  @Test
  public void testIterator() throws Exception {

    Aggregate aggregate = new ConcreteAggregate();

    Iterator iterator = aggregate.createIterator();

    assertEquals("first", iterator.first());
    assertEquals("first", iterator.currentItem());
    assertEquals(false, iterator.isDone());

    assertEquals("second", iterator.next());
    assertEquals("second", iterator.currentItem());
    assertEquals(false, iterator.isDone());

    assertEquals("third", iterator.next());
    assertEquals("third", iterator.currentItem());
    assertEquals(false, iterator.isDone());

    assertEquals("fourth", iterator.next());
    assertEquals("fourth", iterator.currentItem());
    assertEquals(true, iterator.isDone());
  }
}
