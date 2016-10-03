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

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/factorymethod/ConcreteCreator.java
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
#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/factorymethod/ConcreteProductA.java
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
#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/factorymethod/ConcreteProductB.java
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
#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/factorymethod/Creator.java
```java 
package com.hundredwordsgof.factorymethod;


/**
 *  Creator class declares factory method
 */
abstract class Creator {

	abstract Product factoryMethod(String type);
	
}
``` 
#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/factorymethod/Product.java
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
