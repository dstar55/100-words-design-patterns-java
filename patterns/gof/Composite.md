---
layout: page
title: Composite
permalink: /patterns/Composite/
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

Imagine that we need to develop a graphical framework which should speed up the development of business applications, 
where the user works with data using graphical forms. 
A graphical form is made up of the basic graphical elements, such as label, text, input field, button, list, etc.


In order to draw something on the screen, each graphical element should implement a common interface with the draw method. 
But, in addition to the draw interface, some graphical elements must act as containers for other graphical elements. 
So, for example, a form is a container for labels, input fields and buttons.


It seems that a tree structure can be the basis for such a graphical framework, but the problem is that we must treat a leaf node and an internal 
node the same way. This problem can be solved by using the Composite pattern.


The Composite pattern composes objects into tree structures to represent part-whole hierarchies. 
A group of objects is to be treated the same way as a single instance of an object.






###  <a id="Story"></a>Story 

Lego brick represents a Composite pattern. 
A brick is a basic object, but at the same time, a brick is a container which can hold other bricks in order to construct complex objects.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/composite.jpg "Lego Bricks")  
###### Lego Bricks, By Priwo (photo taken by de:Benutzer:Priwo) [Public domain], <a href="https://commons.wikimedia.org/wiki/File%3ALEGO-01.jpg">via Wikimedia Commons</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/composite.png)](http://www.design-patterns-stories.com/assets/img/uml/composite.png)



###  <a id="Structure"></a>Structure 

The *Component* abstract class declares the interface for objects in the composition, implements default behavior for the interface common to 
all classes as appropriate, and declares an interface for accessing and managing its child components.  
The *Leaf* class represents leaf objects in the composition.  
The *Composite* class defines behavior for components having children, stores the child components and implements the child-related operations in the 
*Component* interface.  
The *Client* class uses the *Composite* interface.




###  <a id="Implementation"></a>Implementation 

#### *Component.java* 
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

#### *Leaf.java* 
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

#### *Composite.java* 
```java 
package com.hundredwordsgof.composite;

import java.util.ArrayList;
import java.util.List;

/**
 * 
 * Composite class defines behavior for components having children, stores child
 * components, implements child-related operations in the Component interface
 * 
 */
public class Composite extends Component {

  private List<Component> children = new ArrayList<Component>();

  public void operation() {

    for (Component component : children) {
      component.operation();
    }
  }

  public void add(Component component) {
    children.add(component);
  }

  public void remove(Component component) {
    children.remove(component);
  }

  public Component getChild(int index) {
    return children.get(index);
  }
}
```

###  <a id="Usage"></a>Usage 

#### *CompositeTest.java* 
```java 
package com.hundredwordsgof.composite;

import static org.junit.Assert.*;
import org.junit.Test;

/**
 * Test implementation of the Builder pattern.
 */
public class CompositeTest {

  @Test
  public void testComposite() {

    Component leaf1 = new Leaf();
    Component leaf2 = new Leaf();
    Component leaf3 = new Leaf();

    Composite composite = new Composite();
    composite.add(leaf1);
    composite.add(leaf2);
    composite.add(leaf3);

    composite.operation();

    assertEquals(leaf1, composite.getChild(0));
    assertEquals(leaf2, composite.getChild(1));
    assertEquals(leaf3, composite.getChild(2));

    composite.remove(leaf1);

    assertEquals(leaf2, composite.getChild(0));
    assertEquals(leaf3, composite.getChild(1));
  }
}
```

