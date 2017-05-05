---
layout: page
title: Factory Method
permalink: /patterns/FactoryMethod/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Defines an interface for creating objects, but lets subclasses decides which class to instantiate.
Plasticine is used for children's play. Plasticine is injected into predefined molds. The class of end product(ball, toy, sculpture, cake) is determined by the mold.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/factorymethod.jpg "Cake molds, Han people, metal - Museum of Vietnamese History - Ho Chi Minh City")  
###### Cake molds, Han people, metal - Museum of Vietnamese History - Ho Chi Minh City, By Daderot (Own work) [<a href="http://creativecommons.org/publicdomain/zero/1.0/deed.en">CC0</a>], <a href="https://commons.wikimedia.org/wiki/File%3ACake_molds%2C_Han_people%2C_metal_-_Museum_of_Vietnamese_History_-_Ho_Chi_Minh_City_-_DSC05796.JPG">via Wikimedia Commons</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/factorymethod.png)](http://www.design-patterns-stories.com/assets/img/uml/factorymethod.png)

###  <a id="Implementation"></a>Implementation 

#### *Product.java* 
```java 
package com.hundredwordsgof.factorymethod;

/**
 * 
 * Product interface, defines the interface of the objects which factory method
 * creates.
 *
 */
public interface Product {

}
```

#### *ConcreteProductA.java* 
```java 
package com.hundredwordsgof.factorymethod;

/**
 * 
 * ConcreteProductA class implements Product interface
 *
 */
public class ConcreteProductA implements Product {

}
```

#### *ConcreteProductB.java* 
```java 
package com.hundredwordsgof.factorymethod;

/**
 * 
 * ConcreteProductB class implements Product interface
 *
 */
public class ConcreteProductB implements Product {

}
```

#### *Creator.java* 
```java 
package com.hundredwordsgof.factorymethod;

/**
 * Creator class declares factory method
 */
abstract class Creator {

  abstract Product factoryMethod(String type);
}
```

#### *ConcreteCreator.java* 
```java 
package com.hundredwordsgof.factorymethod;

/**
 * 
 * ConcreteCreator class returns an instance of the ConcreteProduct
 *
 */
public class ConcreteCreator extends Creator {

  public Product factoryMethod(String type) {

    if (type.equals("A")) {
      return new ConcreteProductA();
    } else if (type.equals("B")) {
      return new ConcreteProductB();
    }

    return null;
  }
}
```

###  <a id="Usage"></a>Usage 

#### *FactoryMethodTest.java* 
```java 
package com.hundredwordsgof.factorymethod;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the FactoryMethod pattern.
 */
public class FactoryMethodTest {

  @Test
  public void testFactoryMethod() {

    Creator factory = new ConcreteCreator();

    Product productA = factory.factoryMethod("A");
    Product productB = factory.factoryMethod("B");

    assertEquals("com.hundredwordsgof.factorymethod.ConcreteProductA",
        productA.getClass().getName());
    assertEquals("com.hundredwordsgof.factorymethod.ConcreteProductB",
        productB.getClass().getName());

    assertEquals(null, factory.factoryMethod(""));
  }
}
```

