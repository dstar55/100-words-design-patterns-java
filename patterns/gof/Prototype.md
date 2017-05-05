---
layout: page
title: Prototype
permalink: /patterns/Prototype/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Clone itself.

Sheep Dolly is the first mammal to be cloned, so Dolly is a duplicate.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/prototype.jpg "Sheep Dolly")  
###### Geni, <a href="https://commons.wikimedia.org/wiki/File:Dolly_the_sheep_2016.JPG">Dolly the sheep 2016</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0/legalcode">CC BY-SA 4.0</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/prototype.png)](http://www.design-patterns-stories.com/assets/img/uml/prototype.png)

###  <a id="Implementation"></a>Implementation 

#### *Prototype.java* 
```java 
package com.hundredwordsgof.prototype;

/**
 * Declares interface to copy it self.
 */
public abstract class Prototype implements Cloneable {

  /**
   * Copy method.
   * 
   * @return copy of the object
   * @throws CloneNotSupportedException
   *           exception
   */
  abstract Prototype copyMe() throws CloneNotSupportedException;

}
```

#### *ConcretePrototype.java* 
```java 
package com.hundredwordsgof.prototype;

public class ConcretePrototype extends Prototype {

  /**
   * Implements Prototype, meaning clone method.
   */
  public Prototype copyMe() throws CloneNotSupportedException {
    return (Prototype) this.clone();
  }
}
```

#### *Client.java* 
```java 
package com.hundredwordsgof.prototype;

/**
 * Creates a new object by asking a Prototype to clone itself.
 */
public class Client {

  private Prototype prototype;

  public Client(Prototype prototype) {

    this.prototype = prototype;
  }

  public Prototype operation() throws CloneNotSupportedException {
    return prototype.copyMe();
  }
}
```

###  <a id="Usage"></a>Usage 

#### *PrototypeTest.java* 
```java 
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
```

