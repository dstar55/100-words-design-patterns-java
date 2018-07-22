---
layout: page
title: Decorator
permalink: /patterns/Decorator/
tag: pattern
---

* [Motivation](#Motivation)
* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Motivation"></a>Motivation 

Suppose that we are working on a user interface toolkit and we want to be able to add borders and scroll bars to the windows. 
If we use inheritance, we will extend Window class with new classes, such as WindowVerticalScrollBar, WindowHorizontalScrollBar, WindowBorder, etc.


The solution with the inheritance is not flexible, since we will end up with too many subclasses. 
Such a hierarchy is difficult to maintain, difficult to extend and difficult to use.

But, if we enclose a window in an object which can add new features, such as scroll bar and border dynamically, 
we will have a much more flexible solution. The "enclosed" object is a decorator.


The Decorator pattern attaches additional responsibilities to an object dynamically.


Decorator pattern, attaches additional responsibilities to an object dynamically.





###  <a id="Story"></a>Story 

The spoilers that are added to a car are examples of the Decorator. 
The spoilers do not change the car itself, but add additional functionality which is to 'spoil' unfavorable air movement across a body of a vehicle in motion, usually described as turbulence or drag.






###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/decorator.jpg "013 Porsche 911 Carrera S (8233337583)")  
######  <a href="https://commons.wikimedia.org/wiki/File:2013_Porsche_911_Carrera_S_(8233337583).jpg">2013 Porsche 911 Carrera S (8233337583)</a>, by <a href="http://www.flickr.com/people/15779944@N00">steve lyon</a> from los angeles, ca, usa,<a href="https://creativecommons.org/licenses/by-sa/2.0/legalcode">CC BY-SA 2.0</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/decorator.png)](http://www.design-patterns-stories.com/assets/img/uml/decorator.png)

###  <a id="Implementation"></a>Implementation 

#### *Component.java* 
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

#### *ConcreteComponent.java* 
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

#### *Decorator.java* 
```java 
package com.hundredwordsgof.decorator;

/**
 * 
 * Decorator, keep reference to Component object
 *
 */
abstract class Decorator implements Component {

  protected Component component;

  public abstract void operation();

  public void setComponent(Component component) {
    this.component = component;
  }
}
```

#### *ConcreteDecoratorA.java* 
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

#### *ConcreteDecoratorB.java* 
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

  protected boolean isBehaviorMethodInvoked() {
    return behaviorMethodInvoked;
  }
}
```

###  <a id="Usage"></a>Usage 

#### *DecoratorTest.java* 
```java 
package com.hundredwordsgof.decorator;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test Decorator pattern.
 */
public class DecoratorTest {

  @Test
  public void testDecorator() {

    Component component = new ConcreteComponent();

    Decorator decoratorA = new ConcreteDecoratorA();
    decoratorA.setComponent(component);
    decoratorA.operation();

    assertEquals(true, ((ConcreteDecoratorA) decoratorA).isState());

    Decorator decoratorB = new ConcreteDecoratorB();
    decoratorB.setComponent(component);

    assertEquals(false,
        ((ConcreteDecoratorB) decoratorB).isBehaviorMethodInvoked());

    decoratorB.operation();

    assertEquals(true,
        ((ConcreteDecoratorB) decoratorB).isBehaviorMethodInvoked());
  }
}
```

