---
layout: page
title: Visitor
permalink: /patterns/Visitor/
tag: pattern
---

* [Motivation](#Motivation)
* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Structure](#Structure)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Motivation"></a>Motivation 

Imagine that we need to implement a compiler. 
A compiler is a program which transforms code written in one programming language (the source language) into another programming 
language (the target language).

The compiler functionality is divided into two major blocks: a front-end and a back-end. 
The front-end block comprises of a sequence of several phases, with each stage taking input from its previous stage, 
modifying it and producing its own representation of the source program and passing it to the next phase. 
The front-end includes three main stages, which are called the lexical, the syntax and the semantic analysis.


The first phase takes the source code as a stream of characters and identifies distinct words (tokens), such as variable names, keywords and 
punctuators. 
The second phase determines the validity of syntactic organization of the program and produces the Abstract Syntax Tree (AST). 
The semantic analysis checks whether the AST follows the rules of a language (type checking, name resolution, etc.).


AST, which represents the program written in source code, is created during the second phase and is used in later phases of the compiling process 
for operations such as type-checking, code generation, code optimization, flow analysis, pretty-printing, code instrumentation, etc.


Most of these operations will need to treat nodes that represent assignment statements differently from nodes that represent variables or 
arithmetic expressions. 
Distributing all these operations across the various node classes leads to a system that's hard to understand, maintain and change.


It would be better if each new operation could be added separately, and if the node classes were independent of the operations that apply to them. 
If we package related operations in a separate object, called a visitor, and pass it to elements of the AST as it is traversed, 
then when an element of the AST "accepts" the visitor, it sends a request to the visitor that encodes the element's class.


The solution in the above example is a Visitor design pattern.

The Visitor allows one or more operations to be applied to a set of objects at runtime, decoupling the operations from the object structure.






###  <a id="Story"></a>Story 

Shopping in a supermarket is an example of the Visitor pattern. You pick products and put them in a shopping cart. 
When you get to the checkout, the cashier acts as a visitor, taking the disparate set of elements, some with prices and others that need to be 
weighted, in order to provide you with the total to be paid.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/visitor.jpg "Cashier in Supermarket")  
###### Cashier in Supermarket, CC0 Public Domain



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/visitor.png)](http://www.design-patterns-stories.com/assets/img/uml/visitor.png)



###  <a id="Structure"></a>Structure 

The Visitor declares a Visit operation for each class of ConcreteElements in the object structure. 
The ConcreteVisitor implements each operation declared by the Visitor. 
Each operation implements a fragment of the algorithm defined for the corresponding class of objects in the structure.  
The Element defines an Accept operation that takes a visitor as an argument. 
The ConcreteElement implements an Accept operation that takes a visitor as an argument. 
The ObjectStructure provides a composition or collection of the elements and allows the visitor to visit its elements.




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

