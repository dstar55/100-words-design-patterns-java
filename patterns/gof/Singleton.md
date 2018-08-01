---
layout: page
title: Singleton
permalink: /patterns/Singleton/
tag: pattern
---

* [Motivation](#Motivation)
* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Structure](#Structure)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Motivation"></a>Motivation 

Objects reside inside heap memory, and we can instantiate as many objects as the physical space in the heap memory will allow. 
But, in some cases, we can have a situation when only one instance of a class can be instantiated.
So, imagine that we are developing a program which is playing audio files. Inside that program, we need to have a class which handles audio output. 
A computer usually has one audio output, so no more than one sound can be played at a time. 
Therefore, a class that handles the computer audio device should have exactly one instance.

How can we ensure that only one instance is created?
Each java class has default public constructor, which can be invoked from any part of the code.
If we implement a class where default constructor has scope 'private', 
then only the methods from that class can invoke that constructor, meaning that we can't instantiate that class from other classes. 
This is a basis of the Singleton pattern.

The Singleton ensures that only one (single) object can be created from the class.






###  <a id="Story"></a>Story 

Men's 100 meters world record holder is a singleton. 
There can be only one active "Men's 100 meters world record holder" at any given time. 
Regardless of the actual person who holds this title, "Men's 100 meters world record holder" is a global point of access that 
identifies the fastest person in the world.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/singleton.jpg "Usain Bolt, Men's 100 meters world record holder")  
###### Brick Lane Graffiti Usain Bolt&nbsp;(<a rel='license' href='https://creativecommons.org/licenses/by/2.0/' target='_blank'>CC BY 2.0</a>)&nbsp;by&nbsp;<a xmlns:cc='http://creativecommons.org/ns#' rel='cc:attributionURL' property='cc:attributionName' href='https://www.flickr.com/people/mdpettitt/' target='_blank'>Martin Pettitt</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/singleton.png)](http://www.design-patterns-stories.com/assets/img/uml/singleton.png)



###  <a id="Structure"></a>Structure 

The fact that every class has a public constructor in Java can be used in order to implement a *Singleton*. 
The public constructor will be overridden with a new constructor which does nothing, but the scope of the constructor is private, 
so other classes can't instantiate class objects.


The object is created in the method *getInstance()*, and since an object is created when method *getInstance()* is invoked for first time, 
we are talking about lazy instantiation technique.


This technique ensures that singleton instances are created only when needed.


This implementation may have issues in multithreaded environment, but in such situation we have synchronize method getInstance(), 
or a block inside that method.





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

