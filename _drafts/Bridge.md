---
layout: page
title: Bridge
permalink: /patterns/Bridge/
tag: pattern
---

* [Motivation](#Motivation)
* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Motivation"></a>Motivation 

Let's say that that we want to develop an audio player on our Windows OS. We define the base class, Audio, which has two subclasses – MP3Audio and 
WavAudio. The first version of the player on Windows is running well, but after some time we want to implement the same player on Linux OS.


How do we tackle this situation?


If we incorporate the OS specifics in our hierarchy, we will end up with 4 class combinations, such as WindowsMP3Audio, LinuxMP3Audio, 
WindowsWavAudio and LinuxWavAudio. Adding more codec types and more operating systems will make the hierarchy even larger.


The appropriate solution would be to extract our structure into two separate hierarchies.


The original audio structure classes will remain the same,  and they will contain a reference to an object of the new hierarchy, the OS hierarchy. 
This way we will extract the OS specifics into a class of its own, with two child classes, Windows and Linux. 
The Audio class will get a reference field to one of the OS classes. 
Using that reference, it will be able to delegate work to OS objects when needed. 
This reference will serve as a bridge between the Audio and OS hierarchies.


The explained solution is an example of the Bridge pattern.


The bridge pattern decouples an abstraction from its implementation, so that the two can vary independently.






###  <a id="Story"></a>Story 

A steering wheel is an example of the Bridge. 
The purpose of a steering wheel is to transmit driver's input to the steered wheels in order to dynamically change the direction of the vehicle. 
There are different implementations of steering wheels used in cars, buses, trucks, tractors and racing cars.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/bridge.jpg "1924 Stanley 740 Interior")  
###### 1924 Stanley 740 Interior, By Liftarn (Own work) [Public domain], <a href="https://commons.wikimedia.org/wiki/File%3A1924Stanley740-interior.jpg">via Wikimedia Commons</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/bridge.png)](http://www.design-patterns-stories.com/assets/img/uml/bridge.png)

###  <a id="Implementation"></a>Implementation 

#### *Implementor.java* 
```java 
package com.hundredwordsgof.bridge;

/**
 * 
 * Implementor, defines interface for implementation
 *
 */
public interface Implementor {
  String implementation();
}
```

#### *ConcreteImplementorA.java* 
```java 
package com.hundredwordsgof.bridge;

/**
 * 
 * ConcreteImplementatorA, implements Implementor interface
 *
 */
public class ConcreteImplementorA implements Implementor {

  public String implementation() {
    return this.getClass().getName();
  }
}
```

#### *ConcreteImplementorB.java* 
```java 
package com.hundredwordsgof.bridge;

/**
 * 
 * ConcreteImplementatorB, implements Implementor interface
 *
 */
public class ConcreteImplementorB implements Implementor {

  public String implementation() {
    return this.getClass().getName();
  }
}
```

#### *Abstraction.java* 
```java 
package com.hundredwordsgof.bridge;

/**
 * 
 * Abstraction, defines abstraction interface, maintains a reference to object
 * of type Implementator
 * 
 */
abstract class Abstraction {

  protected Implementor implementor;

  public Abstraction(Implementor implementor) {
    this.implementor = implementor;
  }

  abstract String operation();
}
```

#### *RefinedAbstraction.java* 
```java 
package com.hundredwordsgof.bridge;

/**
 * 
 * Refined Abstraction, extends the interface defined by Abstraction
 *
 */
public class RefinedAbstraction extends Abstraction {

  public RefinedAbstraction(Implementor implementor) {
    super(implementor);
  }

  public String operation() {
    return this.implementor.implementation();
  }
}
```

###  <a id="Usage"></a>Usage 

#### *BridgeTest.java* 
```java 
package com.hundredwordsgof.bridge;

import static org.junit.Assert.*;
import org.junit.Test;

/**
 * Test implementation of the Bridge pattern.
 */
public class BridgeTest {

  @Test
  public void testBuilder() {

    // creates refined abstraction with concreteimplementorA
    RefinedAbstraction refinedAbstractionA = new RefinedAbstraction(
        new ConcreteImplementorA());
    // invokes operation
    assertEquals("com.hundredwordsgof.bridge.ConcreteImplementorA",
        refinedAbstractionA.operation());

    // creates refined abstraction with concreteimplementorB
    RefinedAbstraction refinedAbstractionB = new RefinedAbstraction(
        new ConcreteImplementorB());
    // invokes operation
    assertEquals("com.hundredwordsgof.bridge.ConcreteImplementorB",
        refinedAbstractionB.operation());
  }
}
```

