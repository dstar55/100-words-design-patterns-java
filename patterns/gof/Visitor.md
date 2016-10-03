---
layout: page
title: Visitor
permalink: /Visitor/
tag: pattern
---

* [Story](#Story)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Allows for one or more operations to be applied to a set of objects at runtime, decoupling the operations from object structure.

Shopping in supermarket is example of the Visitor pattern. 
You pick a products and put them in shopping cart. When you get to the checkout, the cashier acts as a visitor, taking the 
disparate set of elements, some with prices and others that needs to be weighted, in order to provide you with total.



###  <a id="UML"></a>UML 
![]({{site.baseurl}}/assets/img/visitor.png)

###  <a id="Implementation"></a>Implementation 
#### *ConcreteElementA.java* 
```java 
package com.hundredwordsgof.visitor;

/**
 * Implements accept operation.
 *
 */
public class ConcreteElementA implements Element {

	private int counter = 0;
	
	public void accept(Visitor visitor) {
		visitor.visitConcreteElementA(this);
	}

	public void operationA(){
		counter++;
	}

	public int getCounter() {
		return counter;
	}
	
	
}
```

#### *ConcreteElementB.java* 
```java 
package com.hundredwordsgof.visitor;

/**
 * Implements accept operation.
 *
 */
public class ConcreteElementB implements Element {

	private int counter = 0;
	
	public void accept(Visitor visitor) {
		
		visitor.visitConcreteElementB(this);
	}

	public void operationB(){
		counter++;
	}

	public int getCounter() {
		return counter;
	}
	
	
}
```

#### *ConcreteVisitor1.java* 
```java 
package com.hundredwordsgof.visitor;

/**
 * Implements operation declared by Visitor. 
 * Each operation implements a fragment of the algorithm defined for the corresponding class of object in the structure.
 *
 */
public class ConcreteVisitor1 implements Visitor {


	public void visitConcreteElementA(ConcreteElementA concreteElementA) {		
		concreteElementA.operationA();
	}


	public void visitConcreteElementB(ConcreteElementB concreteElementB) {		
		concreteElementB.operationB();
	}

}
```

#### *ConcreteVisitor2.java* 
```java 
package com.hundredwordsgof.visitor;

/**
 * Implements operation declared by Visitor. 
 * Each operation implements a fragment of the algorithm defined for the corresponding class of object in the structure.
 *
 */
public class ConcreteVisitor2 implements Visitor {


	public void visitConcreteElementA(ConcreteElementA concreteElementA) {
		concreteElementA.operationA();
	}


	public void visitConcreteElementB(ConcreteElementB concreteElementB) {
		concreteElementB.operationB();
	}

}
```

#### *Element.java* 
```java 
package com.hundredwordsgof.visitor;

/**
 * Defines an Accept operation that takes a visitor as an argument.
 * 
 */
public interface Element {

	void accept(Visitor visitor);
	
}
```

#### *ObjectStructure.java* 
```java 
package com.hundredwordsgof.visitor;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Holds objects in structure. 
 * Provides interface to allow visitors to visit its elements.
 * 
 */
public class ObjectStructure {
	
	private List<Element> children = new ArrayList<Element>();
	
	public void add(Element element){
		children.add(element);
	}
	
	public void remove(Element element){
		children.remove(element);
	}

	public Element getChild(int index){
		return children.get(index);
	}	
	

	void acceptAll(Visitor visitor) {
		for (Iterator iterator = children.iterator(); iterator.hasNext();) {
			Element element = (Element) iterator.next();
			element.accept(visitor);
		}
	}	
}
```

#### *Visitor.java* 
```java 
package com.hundredwordsgof.visitor;


/**
 * Declares a Visit operation for each class of ConcreteElement in the object structure
 * 
 *
 */
public interface Visitor {

	void visitConcreteElementA(ConcreteElementA concreteElementA);
	
	void visitConcreteElementB(ConcreteElementB concreteElementB);

}
```

###  <a id="Usage"></a>Usage 
usage 
