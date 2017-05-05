---
layout: page
title: Composite
permalink: /patterns/Composite/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Compose objects into tree structures to represent part-whole hierarchies. 
Group of objects is to be treated in the same way as a single instance of an object. 

Lego brick represents Composite pattern. 
A brick is a basic object, but on a same time brick is a container which can hold other bricks in order to construct complex objects.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/composite.jpg "Composite")  
###### By Priwo (photo taken by de:Benutzer:Priwo) [Public domain], <a href="https://commons.wikimedia.org/wiki/File%3ALEGO-01.jpg">via Wikimedia Commons</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/composite.png)](http://www.design-patterns-stories.com/assets/img/uml/composite.png)

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

