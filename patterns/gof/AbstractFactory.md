---
layout: page
title: Abstract Factory
permalink: /patterns/AbstractFactory/
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


Imagine that we are developing a framework for a GUI environment, were windows will be drawn on a display device and the user will 
interact with the GUI using a mouse and a keyboard.

The first version of the framework will support Windows OS, so Factory method is used for creation of the graphical abstractions 
like Frame, Window, ScrollBar, etc.


In the next version, the framework will be extended to Linux OS. So, how should we extend our factory method?


One way would be to introduce factory abstraction, where each OS will have dedicated factory for creation of the graphical abstractions. 
The proposed solution is an example of the Abstract Factory.

The Abstract Factory is one level higher in abstraction than the Factory Method. 
The Factory Method abstracts the way objects are created, while the Abstract Factory also abstracts the way factories are created, 
which in turn abstracts the way objects are created.


The Abstract Factory provides an interface for creating families of related objects, without specifying concrete classes.






###  <a id="Story"></a>Story 

This pattern is found in the cards stamping equipment, used in manufacturing of playing cards. 
A card stamping machine is an Abstract Factory which produces cards. 
The same machine is used to stamp French, Italian or German cards. 





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/abstractfactory.jpg "Poker Cards Back")  
###### Poker Cards Back&nbsp;(<a rel='license' href='https://creativecommons.org/share-your-work/public-domain/cc0/' target='_blank'>CC 0</a>)






###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/abstractfactory.png)](http://www.design-patterns-stories.com/assets/img/uml/abstractfactory.png)



###  <a id="Structure"></a>Structure 

The AbstractFactory defines the interface for creation of the abstract product objects. 
The AbstractProduct defines the interface for product objects. 
The ConcreteProduct class implements products based on AbstractProduct interfaces. 
The ConcreteFactory class implements factories based on AbstractFactory interfaces. 
The Client class uses AbstractFactory & AbstractProduct interfaces.




###  <a id="Implementation"></a>Implementation 

#### *AbstractProductA.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * AbstractProductA, define interface for ProductA objects
 * 
 */
abstract class AbstractProductA {

}
```

#### *ProductA1.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * ProductA1, implements AbstractProductA interface
 *
 */
public class ProductA1 extends AbstractProductA {

}
```

#### *ProductA2.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * ProductA2, implements AbstractProductA interface
 *
 */
public class ProductA2 extends AbstractProductA {

}
```

#### *AbstractProductB.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * AbstractProductB, define interface for ProductB objects
 * 
 */
abstract class AbstractProductB {

}
```

#### *ProductB1.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * ProductB1, implements AbstractProductB interface
 *
 */
public class ProductB1 extends AbstractProductB {

}
```

#### *ProductB2.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * ProductB2, implements AbstractProductB interface
 *
 */
public class ProductB2 extends AbstractProductB {

}
```

#### *AbstractFactory.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * Abstract Factory, defines interface for creation of the abstract product
 * objects
 * 
 */
public interface AbstractFactory {

  AbstractProductA createProductA();

  AbstractProductB createProductB();
}
```

#### *ConcreteFactory1.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * ConcreteFactory1, implements creation of the concrete Product1 objects
 *
 */
public class ConcreteFactory1 implements AbstractFactory {

  public AbstractProductA createProductA() {
    return new ProductA1();
  }

  public AbstractProductB createProductB() {
    return new ProductB1();
  }
}
```

#### *ConcreteFactory2.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * ConcreteFactory2, implements creation of the concrete Product2 objects
 *
 */
public class ConcreteFactory2 implements AbstractFactory {

  public AbstractProductA createProductA() {
    return new ProductA2();
  }

  public AbstractProductB createProductB() {
    return new ProductB2();
  }
}
```

###  <a id="Usage"></a>Usage 

#### *AbstractFactoryTest.java* 
```java 
package com.hundredwordsgof.abstractfactory;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the AbstractFactory pattern.
 */
public class AbstractFactoryTest {

  @Test
  public void testAbstractFactory() {

    AbstractFactory abstractFactory1 = new ConcreteFactory1();
    AbstractFactory abstractFactory2 = new ConcreteFactory2();

    assertEquals("com.hundredwordsgof.abstractfactory.ProductA1",
        abstractFactory1.createProductA().getClass().getName());
    assertEquals("com.hundredwordsgof.abstractfactory.ProductB1",
        abstractFactory1.createProductB().getClass().getName());

    assertEquals("com.hundredwordsgof.abstractfactory.ProductA2",
        abstractFactory2.createProductA().getClass().getName());
    assertEquals("com.hundredwordsgof.abstractfactory.ProductB2",
        abstractFactory2.createProductB().getClass().getName());
  }
}
```

