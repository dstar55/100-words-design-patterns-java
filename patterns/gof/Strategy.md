---
layout: page
title: Strategy
permalink: /Strategy/
tag: pattern
---

* [Story](#Story)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Select an algorithm at runtime.

Payment options in a Shopping Cart is an example of Strategy.
User can choose various payment options like Master Card, Amex or PayPal.
Any of these payment options will pay items in Shopping Cart, and they can be used interchangeably. 
The user must choose the Strategy based on his possibilities, preferences.



###  <a id="UML"></a>UML 
![]({{site.baseurl}}/assets/img/strategy.png)

###  <a id="Implementation"></a>Implementation 

#### *ConcreteStrategyA.java* 
```java 
package com.hundredwordsgof.strategy;

/**
 * Implements the algorithm defined in Strategy interface. 
 *
 */
public class ConcreteStrategyA implements Strategy{


	public String algorithmInterface() {
		return "Go to airport with ConcreteStrategyA, take a taxi";
	}

}
```

#### *ConcreteStrategyB.java* 
```java 
package com.hundredwordsgof.strategy;

/**
 * Implements the algorithm defined in Strategy interface. 
 *
 */
public class ConcreteStrategyB implements Strategy{


	public String algorithmInterface() {
		return "Go to airport with ConcreteStrategyB, take a bus";
	}

}
```

#### *ConcreteStrategyC.java* 
```java 
package com.hundredwordsgof.strategy;

/**
 * Implements the algorithm defined in Strategy interface. 
 *
 */
public class ConcreteStrategyC implements Strategy{


	public String algorithmInterface() {
		return "Go to airport with ConcreteStrategyC, take a metro";
	}

}
```

#### *Context.java* 
```java 
package com.hundredwordsgof.strategy;

/**
 * Maintains a reference to a Strategy object.
 * Invokes algorithm implemented in ConcreteStrategy.
 *
 */
public class Context {

	private Strategy startegy;
	
	public Context(Strategy startegy){
		this.startegy = startegy;
	}

	public String contextInterface(){
		return this.startegy.algorithmInterface();
	}
}

```

#### *Strategy.java* 
```java 
package com.hundredwordsgof.strategy;

/**
 * Declares an interface common to all supported algorithms. 
 * Context uses this interface to call the algorithm defined by a ConcreteStrategy. 
 * 
 *
 */
public interface Strategy {

	String algorithmInterface();
	
}

```

###  <a id="Usage"></a>Usage 

usage 

