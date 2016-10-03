---
layout: page
title: Prototype
permalink: /Prototype/
tag: pattern
---



### Story 

Clone itself.

Sheep Dolly is the first mammal to be cloned, so Dolly is a duplicate.




### UML 
![]({{site.baseurl}}/assets/img/prototype.png)

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/prototype/Client.java
```java 
package com.hundredwordsgof.prototype;

/**
 * Creates a new object by asking a Prototype to clone itself(invokes copyMe() method.
 */
public class Client {

	private Prototype prototype;
	
	public Client(Prototype prototype){
		
		this.prototype = prototype;		
	}
	
	public Prototype operation() throws CloneNotSupportedException{
		return prototype.copyMe();
	}

}
``` 
#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/prototype/ConcretePrototype.java
```java 
package com.hundredwordsgof.prototype;

public class ConcretePrototype extends Prototype {

	/**
	 * Implements Prototype, meaning clone method.
	 */
	public Prototype copyMe() throws CloneNotSupportedException {
		return (Prototype)this.clone();
	}

}
``` 
#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/prototype/Prototype.java
```java 
package com.hundredwordsgof.prototype;

/**
 * Declares interface to copy it self.
 */
public abstract class Prototype implements Cloneable  {

	/**
	 * Copy method.
	 * @return copy of the object
	 * @throws CloneNotSupportedException exception
	 */
	abstract Prototype copyMe() throws CloneNotSupportedException;
	
}
``` 
