package com.hundredwordsgof.singleton;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import org.junit.Test;

/**
 * Test implementation of the Singleton pattern.
 */
public class SingletonTest {

  @Test
  public void testSingleton() {

    // invokes Singleton.getInstance() for first time,
    // object will be created
    Singleton singleton = Singleton.getInstance();
    assertNotNull(singleton);

    // invokes Singleton.getInstance() for second time,
    // reference to the same object will be returned
    Singleton secondSingleton = Singleton.getInstance();
    assertEquals(singleton, secondSingleton);
  }
}
