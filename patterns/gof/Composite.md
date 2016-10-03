---
layout: page
title: Composite
permalink: /Composite/
tag: pattern
---



### Story 

Compose objects into tree structures to represent part-whole hierarchies. 
Group of objects is to be treated in the same way as a single instance of an object. 

Lego brick represents Composite pattern. 
A brick is a basic object, but on a same time brick is a container which can hold other bricks in order to construct complex objects.




### UML 
![]({{site.baseurl}}/assets/img/composite.png)

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/composite/Component.java
```java 
package com.hundredwordsgof.composite;

/**
 * 
 * Component declares the interface for objects in the composition 
 *
 */
abstract class Component {

	abstract void operation();
	
	
}
``` 
#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/composite/Composite.java
```java 
package com.hundredwordsgof.composite;

import java.util.ArrayList;
import java.util.List;

/**
 * 
 * Composite class  defines behavior for components having children, stores child components, 
 * implements child-related operations in the Component interface
 * 
 */
public class Composite extends Component {

	private List<Component> children = new ArrayList<Component>();
	
	public void operation() {

		for (Component component : children) {
			component.operation();
		}
	}

	public void add(Component component){
		children.add(component);
	}
	
	public void remove(Component component){
		children.remove(component);
	}

	public Component getChild(int index){
		return children.get(index);
	}	
}
``` 
#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/composite/Leaf.java
```java 
package com.hundredwordsgof.composite;

/**
 * 
 * Leaf class represents leaf objects in the composition
 *
 */
public class Leaf extends Component {

	void operation() {
		
	}

}
``` 
