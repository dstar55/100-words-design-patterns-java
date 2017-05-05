---
layout: page
title: Flyweight
permalink: /patterns/Flyweight/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Remove duplicates.

Flyweight pattern is used to reduce memory by loading only the data necessary to perform action.
Database normalization is flyweight. Normalisation, is the process of organizing the columns (attributes) and tables (relations) of a relational database to minimize data redundancy.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/flyweight.jpg "Database Normalization")  
###### By 04hutts (Own work) [Public domain], <a href="https://commons.wikimedia.org/wiki/File%3ANormalFormDiagram.png">via Wikimedia Commons</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/flyweight.png)](http://www.design-patterns-stories.com/assets/img/uml/flyweight.png)

###  <a id="Implementation"></a>Implementation 

#### *Flyweight.java* 
```java 
package com.hundredwordsgof.flyweight;

/**
 * 
 * Flyweight, interface through flyweight can receive and act on extrinsic
 * state.
 *
 */
public interface Flyweight {

  void operation(Object extrinsicState);
}
```

#### *ConcreteFlyweight.java* 
```java 
package com.hundredwordsgof.flyweight;

/**
 * 
 * ConcreteFlyweight,implements Flyweight, and add storage for intrisnic state.
 *
 */
public class ConcreteFlyweight implements Flyweight {

  private Object intrinsicState;

  public ConcreteFlyweight(Object intrinsicState) {
    this.intrinsicState = intrinsicState;
  }

  // Using extrinsicState as context and does NOT modify intrinsic state.
  public void operation(Object extrinsicState) {
  }

  /**
   * @return intrinsic state
   */
  public Object getIntrinsicState() {
    return intrinsicState;
  }
}
```

#### *UnsharedConcreteFlyweight.java* 
```java 
package com.hundredwordsgof.flyweight;

/**
 * UnsharedConcreteFlyweight, defines objects which are not shared.
 *
 */
public class UnsharedConcreteFlyweight implements Flyweight {

  private Object state;

  public UnsharedConcreteFlyweight(Object state) {
    this.state = state;
  }

  public void operation(Object extrinsicState) {

  }

  public Object getState() {
    return state;
  }
}
```

#### *FlyweightFactory.java* 
```java 
package com.hundredwordsgof.flyweight;

import java.util.HashMap;
import java.util.Map;

/**
 * 
 * FlyweightFactory, creates and manages the flyweight objects.
 *
 */
public class FlyweightFactory {

  private static Map<String, Flyweight> flyweights = new HashMap<String, Flyweight>();

  /**
   * Returns Flyweight object. Just for sake of example following logic is
   * applied, if key starts with phrase:unshared than UnsharedConcreteFlyweight
   * object is created. Otherwise ConcreteFlyweight object is created.
   * 
   * @param key
   * @return Flyweight
   * 
   */
  public static Flyweight getFlyweight(String key, String value) {

    if (key.startsWith("unshared")) {
      flyweights.put(key, new UnsharedConcreteFlyweight(value));
    } else {
      if (!flyweights.containsKey(key)) {
        flyweights.put(key, new ConcreteFlyweight(value));
      }
    }

    return (Flyweight) flyweights.get(key);
  }
}
```

###  <a id="Usage"></a>Usage 

#### *FlyweightTest.java* 
```java 
package com.hundredwordsgof.flyweight;

import static org.junit.Assert.*;
import org.junit.Test;

/**
 * Test Flyweight pattern.
 */
public class FlyweightTest {

  @Test
  public void testFlyweight() {

    Flyweight flyweight1 = FlyweightFactory.getFlyweight("key1", "value1");
    Flyweight flyweight2 = FlyweightFactory.getFlyweight("key2", "value2");
    Flyweight flyweight3 = FlyweightFactory.getFlyweight("key1", "value3");

    Flyweight unsharedFlyweight1 = FlyweightFactory.getFlyweight("unsharedKey1",
        "value1");
    Flyweight unsharedFlyweight2 = FlyweightFactory.getFlyweight("unsharedKey2",
        "value2");
    Flyweight unsharedFlyweight3 = FlyweightFactory.getFlyweight("unsharedKey1",
        "value3");

    assertNotEquals(flyweight1, flyweight2);
    assertEquals(flyweight1, flyweight3);
    assertNotEquals(flyweight2, flyweight3);

    assertNotEquals(unsharedFlyweight1, unsharedFlyweight2);
    assertNotEquals(unsharedFlyweight1, unsharedFlyweight3);
    assertNotEquals(unsharedFlyweight2, unsharedFlyweight3);

    if (flyweight1 instanceof com.hundredwordsgof.flyweight.ConcreteFlyweight) {
      assertEquals("value1",
          ((com.hundredwordsgof.flyweight.ConcreteFlyweight) flyweight1)
              .getIntrinsicState());
    }

    if (flyweight2 instanceof com.hundredwordsgof.flyweight.ConcreteFlyweight) {
      assertEquals("value2",
          ((com.hundredwordsgof.flyweight.ConcreteFlyweight) flyweight2)
              .getIntrinsicState());
    }

    if (flyweight3 instanceof com.hundredwordsgof.flyweight.ConcreteFlyweight) {
      assertEquals("value1",
          ((com.hundredwordsgof.flyweight.ConcreteFlyweight) flyweight3)
              .getIntrinsicState());
    }

    if (unsharedFlyweight1 instanceof com.hundredwordsgof.flyweight.UnsharedConcreteFlyweight) {
      assertEquals("value1",
          ((com.hundredwordsgof.flyweight.UnsharedConcreteFlyweight) unsharedFlyweight1)
              .getState());
    }

    if (unsharedFlyweight2 instanceof com.hundredwordsgof.flyweight.UnsharedConcreteFlyweight) {
      assertEquals("value2",
          ((com.hundredwordsgof.flyweight.UnsharedConcreteFlyweight) unsharedFlyweight2)
              .getState());
    }

    if (unsharedFlyweight3 instanceof com.hundredwordsgof.flyweight.UnsharedConcreteFlyweight) {
      assertEquals("value3",
          ((com.hundredwordsgof.flyweight.UnsharedConcreteFlyweight) unsharedFlyweight3)
              .getState());
    }
  }
}
```

