---
layout: page
title: Template Method
permalink: /patterns/TemplateMethod/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Defines a skeleton of an algorithm in an operation.
Algorithm will have common and specialized part.

Daily routine is example of the Template method.
Every day workers get up(common part), go to work(specialized part), go home and go to sleep.
There are workers with different professions like enginners, teachers, etc.
During work engineer will fix machines while teacher will teach childern how to read and write.
At the end of the day worker go home, have a dinner and go to sleep.



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/templatemethod.png)](http://www.design-patterns-stories.com/assets/img/uml/templatemethod.png)

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

