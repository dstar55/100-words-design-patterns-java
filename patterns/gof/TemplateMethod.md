---
layout: page
title: Template Method
permalink: /TemplateMethod/
tag: pattern
---



### Story 

Defines a skeleton of an algorithm in an operation.
Algorithm will have common and specialized part.

Daily routine is example of the Template method.
Every day workers get up(common part), go to work(specialized part), go home and go to sleep.
There are workers with different professions like enginners, teachers, etc.
During work engineer will fix machines while teacher will teach childern how to read and write.
At the end of the day worker go home, have a dinner and go to sleep.



### UML 
![]({{site.baseurl}}/assets/img/templatemethod.png)

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/templatemethod/AbstractClass.java
```java 
package com.hundredwordsgof.templatemethod;

/**
 * Defines interfaces for primitive operations. Implements algorithm.
 * 
 *
 */
abstract class AbstractClass {

	/**
	 * Template method, implementation of algorithm which consists of primitiveOperations
	 * 
	 * @return result of the primitive operations 
	 */
	public String templateMethod(){
		
		return this.primitiveOperation1() + this.primitiveOperation2();
		
	}
	
	abstract String primitiveOperation1();
	
	abstract String primitiveOperation2();
}
```

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/templatemethod/ConcreteClass.java
```java 
package com.hundredwordsgof.templatemethod;

/**
 * 
 * Implements the primitive operations to carry out subclass-specific steps of the algorithm.
 *
 */
public class ConcreteClass extends AbstractClass{

	String primitiveOperation1() {
		return "Template";
	}


	String primitiveOperation2() {
		return "Method";
	}

}
```

