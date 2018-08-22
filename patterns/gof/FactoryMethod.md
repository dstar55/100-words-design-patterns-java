---
layout: page
title: Factory Method
permalink: /patterns/FactoryMethod/
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

Imagine that we need to develop a reporting library. 
Two basic abstractions in this library are the Engine and the Report classes. 
Both classes are abstract, and clients have to extend them in order to realize their application specific implementations.


The Engine class is responsible for managing Reports and will create them as required. 
Report subclasses which Engine should instantiate are application specific and Engine only knows when a new report should be created, 
but not what type of Report to create. 
This leads us to a situation in which our library should instantiate classes, but it only knows about abstract classes, which it cannot instantiate.


So, how can we solve this?


If we encapsulate the knowledge of which Report subclasses to create and move this knowledge outside of the library, then 
Engine subclass will be able to create Report objects. This solution is the Factory Method pattern.


The Factory Method defines an interface for creating objects, but lets subclasses decide which class to instantiate.






###  <a id="Story"></a>Story 

Plasticine is used as a toy for children. Plasticine is injected into predefined molds. 
The class of end product (ball, toy, sculpture, cake) is determined by the mold.






###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/factorymethod.jpg "Cake molds, Han people, metal - Museum of Vietnamese History - Ho Chi Minh City")  
###### Cake molds, Han people, metal - Museum of Vietnamese History - Ho Chi Minh City, By Daderot (Own work) [<a href="http://creativecommons.org/publicdomain/zero/1.0/deed.en">CC0</a>], <a href="https://commons.wikimedia.org/wiki/File%3ACake_molds%2C_Han_people%2C_metal_-_Museum_of_Vietnamese_History_-_Ho_Chi_Minh_City_-_DSC05796.JPG">via Wikimedia Commons</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/factorymethod.png)](http://www.design-patterns-stories.com/assets/img/uml/factorymethod.png)



###  <a id="Structure"></a>Structure 

The *Product* interface defines the interface of objects the factory method creates.    
The *ConcreteProduct* class implements the *Product* interface.   
The *Creator* abstract class declares the factory method interface.   
The *ConcreteCreator* class implements the *Creator's* factory method and returns an instance of the *ConcreteProduct*.  




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

