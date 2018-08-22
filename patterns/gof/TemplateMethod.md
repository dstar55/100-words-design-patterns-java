---
layout: page
title: Template Method
permalink: /patterns/TemplateMethod/
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

Imagine that we need to implement an application which performs various operations on a database. We decide to use JDBC, which is a standard Java interface for accessing a relational database. 
Using JDBC for database operations (for example, a read operation via select SQL statement), the user must execute following steps:

* connect to database   
* execute SQL statement   
* process data which are gathered from database   
* close database connection   
* handle errors if something goes wrong   

If we implement such a database operation several times for various read operations, we will find out that we are repeating some steps. 
We can also see that some steps are always the same, i.e. 'connect to database', 'close database connection', 'handle errors'. 
The remaining steps, such as 'execute SQL statement' and 'process data obtained from the database' are different for each read operation. 
So, let's call those steps which are the same 'invariant' and remaining steps 'variant'.


We now implement invariant steps inside an abstract base class, while the variant steps are either given a default implementation, or no 
implementation at all. The variant steps represent "hooks", or "placeholders", that may, or must, be supplied by the component's client in a 
concrete derived class.


The solution in the above example is the Template Method design pattern.


The Template Method defines a skeleton of an algorithm in an operation. Algorithm will have a common part and a specialized part.





###  <a id="Story"></a>Story 

Daily routine is example of the Template Method. 
Every day people get up (common part), go to work (common part), do their job (specialized part), go home (common part) and go to sleep (common part). 
There are people with different professions, such as engineers, teachers, etc. During work, an engineer will fix machines, 
while teacher will teach children how to read and write. 
At the end of the day they go home, have dinner and go to sleep.



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/templatemethod.png)](http://www.design-patterns-stories.com/assets/img/uml/templatemethod.png)



###  <a id="Structure"></a>Structure 

The *AbstractClass* defines abstract primitive operations that concrete subclasses should implement.  
The *ConcreteClass* implements the abstract primitive operations to carry out subclass-specific steps of the algorithm.




###  <a id="Implementation"></a>Implementation 

#### *AbstractClass.java* 
```java 
package com.hundredwordsgof.templatemethod;

/**
 * Defines interfaces for primitive operations. Implements algorithm.
 * 
 *
 */
abstract class AbstractClass {

  /**
   * Template method, implementation of algorithm which consists of
   * primitiveOperations
   * 
   * @return result of the primitive operations
   */
  public String templateMethod() {
    return this.primitiveOperation1() + this.primitiveOperation2();
  }

  abstract String primitiveOperation1();

  abstract String primitiveOperation2();
}
```

#### *ConcreteClass.java* 
```java 
package com.hundredwordsgof.templatemethod;

/**
 * 
 * Implements the primitive operations to carry out subclass-specific steps of
 * the algorithm.
 *
 */
public class ConcreteClass extends AbstractClass {

  public String primitiveOperation1() {
    return "Template";
  }

  public String primitiveOperation2() {
    return "Method";
  }
}
```

###  <a id="Usage"></a>Usage 

#### *TemplateTest.java* 
```java 
package com.hundredwordsgof.templatemethod;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the Template Method pattern.
 */
public class TemplateTest {

  @Test
  public void testTemplate() {

    ConcreteClass template = new ConcreteClass();
    assertEquals("TemplateMethod", template.templateMethod());
  }
}
```

