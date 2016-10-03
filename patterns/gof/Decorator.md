---
layout: page
title: Decorator
permalink: /Decorator/
tag: pattern
---



### Story 

Attach additional responsibilities to an object dynamically. 

The spoilers that are added to a car are examples of the Decorator.
The spoilers do not change the car itself, but adds additional functionality which is to 'spoil' unfavorable air movement across a body of a vehicle in motion, usually described as turbulence or drag.  



### UML 
![]({{site.baseurl}}/assets/img/decorator.png)

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/decorator/Component.java
```java 
package com.hundredwordsgof.decorator;

/**
 * 
 * Component, defines interface for new features which will be added dynamicaly
 *
 */
public interface Component {

	void operation();
	
}
``` 
#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/decorator/ConcreteComponent.java
```java 
package com.hundredwordsgof.decorator;

/**
 * 
 * ConcreteComponent, define object where new features can be added
 *
 */
public class ConcreteComponent implements Component {


	public void operation() {
	}

}
``` 
#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/decorator/ConcreteDecoratorA.java
```java 
package com.hundredwordsgof.decorator;

/**
 * 
 * ConcreteDecoratorA, add features to component
 *
 */
public class ConcreteDecoratorA extends Decorator {

	private boolean state;
	
	public void operation() {

		state = true;
		this.component.operation();
		
	}

	public boolean isState() {
		return state;
	}

	
}
``` 
#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/decorator/ConcreteDecoratorB.java
```java 
package com.hundredwordsgof.decorator;

/**
 * 
 * ConcreteDecoratorB, add features to component
 *
 */
public class ConcreteDecoratorB extends Decorator {

	private boolean behaviorMethodInvoked = false;
	
	public void operation() {
		this.component.operation();
		addedBehavior();
	}

	private void addedBehavior() {
		behaviorMethodInvoked = true;
	}

	public boolean isBehaviorMethodInvoked() {
		return behaviorMethodInvoked;
	}

	
}
``` 
#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/decorator/Decorator.java
```java 
package com.hundredwordsgof.decorator;

/**
 * 
 * Decorator, keep reference to Component object
 *
 */
abstract class Decorator implements Component{

	protected Component component;
	
	public abstract void operation();

	public void setComponent(Component component) {
		this.component = component;
	}

	
}
``` 
