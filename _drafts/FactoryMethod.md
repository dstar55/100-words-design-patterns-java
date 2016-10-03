---
layout: page
title: Factory Method
permalink: /FactoryMethod/
tag: pattern
---



### Story 

Defines an interface for creating objects, but lets subclasses decides which class to instantiate.
Plasticine is used for children's play. Plasticine is injected into predefined molds. The class of end product(ball, toy, sculpture) is determined by the mold.



### UML 
![]({{site.baseurl}}/assets/img/factorymethod.png)

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
		
		if(type.equals("A")){
			return new ConcreteProductA();	
		}else if(type.equals("B")){
			return new ConcreteProductB();
		}
		
		return null;
	}

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
 *  Creator class declares factory method
 */
abstract class Creator {

	abstract Product factoryMethod(String type);
	
}
```

#### *Product.java* 
```java 
package com.hundredwordsgof.factorymethod;

/**
 * 
 * Product interface defines the interface of objects the factory method creates 
 *
 */
public interface Product {

}
```

