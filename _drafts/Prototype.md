---
layout: page
title: Prototype
permalink: /patterns/Prototype/
tag: pattern
---

* [Story](#Story)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Clone itself.

Sheep Dolly is the first mammal to be cloned, so Dolly is a duplicate.




###  <a id="UML"></a>UML 
[![](/assets/img/prototype.png)](/assets/img/prototype.png)

###  <a id="Implementation"></a>Implementation 

#### *Prototype.java* 
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

#### *ConcretePrototype.java* 
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

#### *Client.java* 
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

###  <a id="Usage"></a>Usage 

#### *PrototypeTest.java* 
```java 
package com.hundredwordsgof.prototype;

import static org.junit.Assert.assertNotEquals;

import org.junit.Test;

import com.hundredwordsgof.prototype.Client;
import com.hundredwordsgof.prototype.ConcretePrototype;
import com.hundredwordsgof.prototype.Prototype;

/**
 * Test Prototype pattern.
 */
public class PrototypeTest {

	@Test
	public void testPrototype() throws CloneNotSupportedException{

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

