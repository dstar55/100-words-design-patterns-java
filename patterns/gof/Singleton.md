---
layout: page
title: Singleton
permalink: /patterns/Singleton/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Singleton ensures that only one(single) object can be created from the class.

Men's 100 meters world record holder is a singleton.
There can be at most one active "Men's 100 meters world record holder" at any given time. 
Regardless of who that person is the title, "Men's 100 meters world record holder" is a global point of access that identifies the fastes person in the world.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/singleton.jpg "Usain Bolt, Men's 100 meters world record holder")  
###### Brick Lane Graffiti Usain Bolt&nbsp;(<a rel='license' href='https://creativecommons.org/licenses/by/2.0/' target='_blank'>CC BY 2.0</a>)&nbsp;by&nbsp;<a xmlns:cc='http://creativecommons.org/ns#' rel='cc:attributionURL' property='cc:attributionName' href='https://www.flickr.com/people/mdpettitt/' target='_blank'>Martin Pettitt</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/singleton.png)](http://www.design-patterns-stories.com/assets/img/uml/singleton.png)

###  <a id="Implementation"></a>Implementation 

#### *Singleton.java* 
```java 
package com.hundredwordsgof.singleton;

/**
 * Singleton class implements singleton pattern. Only one object can be
 * instantiated.
 * 
 */
public class Singleton {

  /**
   * Holds reference to single instance.
   */
  private static Singleton INSTANCE;

  /**
   * Overrides public Constructor.
   */
  private Singleton() {
  }

  /**
   * Creates the instance if it does not yet exist(lazy instantiation).
   * 
   * @return a reference to the single instance.
   */
  public static Singleton getInstance() {
    if (INSTANCE == null) {
      INSTANCE = new Singleton();
    }
    return INSTANCE;
  }
}
```

###  <a id="Usage"></a>Usage 

#### *SingletonTest.java* 
```java 
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
```

