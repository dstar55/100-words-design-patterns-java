package com.hundredwordsgof.prototype;

import static org.junit.Assert.assertNotEquals;
import org.junit.Test;

/**
 * Test Prototype pattern.
 */
public class PrototypeTest {

  @Test
  public void testPrototype() throws CloneNotSupportedException {

    // creates object of type Prototype
    Prototype prototype = new ConcretePrototype();
    // creates Client object(Prototype is "injected" via Constructor)
    Client client = new Client(prototype);

    // client creates new object(clone it self) of type Prototype
    Prototype prototypeClone = client.operation();

    // ensure that prototype and it's own clone are not same objects
    assertNotEquals(prototype, prototypeClone);
  }
}
