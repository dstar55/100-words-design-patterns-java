---
layout: page
title: Visitor
permalink: /patterns/Visitor/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Allows for one or more operations to be applied to a set of objects at runtime, decoupling the operations from object structure.

Shopping in supermarket is example of the Visitor pattern. 
You pick a products and put them in shopping cart. When you get to the checkout, the cashier acts as a visitor, taking the 
disparate set of elements, some with prices and others that needs to be weighted, in order to provide you with total.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/visitor.jpg "Cashier in Supermarket")  
###### Cashier in Supermarket, CC0 Public Domain



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/visitor.png)](http://www.design-patterns-stories.com/assets/img/uml/visitor.png)

###  <a id="Implementation"></a>Implementation 

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

  public void operationA() {
    counter++;
  }

  protected int getCounter() {
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

  public void operationB() {
    counter++;
  }

  protected int getCounter() {
    return counter;
  }
}
```

#### *Visitor.java* 
```java 
package com.hundredwordsgof.visitor;

/**
 * Declares a Visit operation for each class of ConcreteElement in the object
 * structure
 * 
 */
public interface Visitor {

  void visitConcreteElementA(ConcreteElementA concreteElementA);

  void visitConcreteElementB(ConcreteElementB concreteElementB);
}
```

#### *ConcreteVisitor1.java* 
```java 
package com.hundredwordsgof.visitor;

/**
 * Implements operation declared by Visitor. Each operation implements a
 * fragment of the algorithm defined for the corresponding class of object in
 * the structure.
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
 * Implements operation declared by Visitor. Each operation implements a
 * fragment of the algorithm defined for the corresponding class of object in
 * the structure.
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

#### *ObjectStructure.java* 
```java 
package com.hundredwordsgof.visitor;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Holds objects in structure. Provides interface to allow visitors to visit its
 * elements.
 * 
 */
public class ObjectStructure {

  private List<Element> children = new ArrayList<Element>();

  public void add(Element element) {
    children.add(element);
  }

  public void remove(Element element) {
    children.remove(element);
  }

  public Element getChild(int index) {
    return children.get(index);
  }

  public void acceptAll(Visitor visitor) {
    for (Iterator iterator = children.iterator(); iterator.hasNext();) {
      Element element = (Element) iterator.next();
      element.accept(visitor);
    }
  }
}
```

###  <a id="Usage"></a>Usage 

#### *VisitorTest.java* 
```java 
package com.hundredwordsgof.visitor;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the Visitor pattern.
 */
public class VisitorTest {

  @Test
  public void testVisitor() {

    // Setup structure
    ObjectStructure objectStructure = new ObjectStructure();

    ConcreteElementA concreteElementA = new ConcreteElementA();
    ConcreteElementB concreteElementB = new ConcreteElementB();

    objectStructure.add(concreteElementA);
    objectStructure.add(concreteElementB);

    // Create visitor objects
    ConcreteVisitor1 v1 = new ConcreteVisitor1();
    ConcreteVisitor2 v2 = new ConcreteVisitor2();

    // Structure accepting visitors
    objectStructure.acceptAll(v1);
    assertEquals(1, concreteElementA.getCounter());
    assertEquals(1, concreteElementB.getCounter());

    objectStructure.acceptAll(v2);
    assertEquals(2, concreteElementA.getCounter());
    assertEquals(2, concreteElementB.getCounter());

    // lets remove second element from objectStructure
    Element element = objectStructure.getChild(1);
    objectStructure.remove(element);
    // now visit all elements on objectStructure
    objectStructure.acceptAll(v1);
    assertEquals(3, concreteElementA.getCounter());

    // this element was removed from objectStructure so counter should remain
    // the same as before last invocation of the acceptAll
    assertEquals(2, concreteElementB.getCounter());

  }
}
```

