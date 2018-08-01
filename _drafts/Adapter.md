---
layout: page
title: Adapter
permalink: /patterns/Adapter/
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

Imagine that we need to develop a graphical editor which should be able to draw various graphical shapes like line, circle, rectangle and text. 
All of our graphical elements are subclass of the base class Shape. So, we will have LineShape, CircleShape, RectangeShape and TextShape.


The implementation of the TextShape is not easy. 
We need to implement a lot of complex functionalities, such as text buffering, text bolding, text coloring, undo, redo, 
'what you see is what you get', etc. We have found an open source text library which implements pretty much all of the text functionality 
which we are looking for.


Why not adapt an existing text library, so that we can reuse already implemented functionality for our graphical editor? 
But, in order to use the existing text library, we must adapt interfaces from the existing text library to our interfaces.


The process of adaptation of the existing interfaces is an example of the Adapter pattern.


The adapter allows us to access the interface of an existing class from another interface.






###  <a id="Story"></a>Story 

Adapters are often used in daily life, for example, an electrical adapter is a device that converts attributes of one electrical device or 
system to those of an otherwise incompatible device or system. 
Some modify power or signal attributes, while others merely adapt the physical form of one electrical connector to another.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/adapter.jpg "Adapter")  
###### <a href="https://commons.wikimedia.org/wiki/User:Lionel_Allorge">Lionel Allorge</a>, <a href="https://commons.wikimedia.org/wiki/File:Adaptateur_de_prise_française_en_prise_suisse_2.jpg">Adaptateur de prise française en prise suisse 2</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/legalcode">CC BY-SA 3.0</a>



###  <a id="UML"></a>UML
#### Class Adapter
[![](http://www.design-patterns-stories.com/assets/img/uml/classadapter.png)](http://www.design-patterns-stories.com/assets/img/uml/classadapter.png)

#### Object Adapter
[![](http://www.design-patterns-stories.com/assets/img/uml/objectadapter.png)](http://www.design-patterns-stories.com/assets/img/uml/objectadapter.png)



###  <a id="Structure"></a>Structure 

We can have two implementations, the *Class* adapter and the *Object* adapter.


The *Class* adapter extends the *Adaptee* class.   
The *Object* adapter injects *Adaptee* object into the *Adapter* class.


The target interface defines the domain-specific interface used by the *Client*.   
The *Client* class uses the target interface.  
The *Adaptee* class defines an existing interface where adaption will be applied.  
The *Adapter* class adapts interface *Adaptee* to the *Target*.




###  <a id="Implementation"></a>Implementation 

#### Class Adapter
#### *Target.java* 
```java 
package com.hundredwordsgof.adapter.clazz;

/**
 * 
 * Target interface, defines domain-specific interface to which Adaptee will be adapted 
 *
 */
public interface Target {

	String request();	
}
```

#### *Adaptee.java* 
```java 
package com.hundredwordsgof.adapter.clazz;

/**
 * 
 * Adaptee class, interface which will be adapted 
 *
 */
public class Adaptee {

	public String specialRequest(){
		return "specialRequest";
	}
}
```

#### *Adapter.java* 
```java 
package com.hundredwordsgof.adapter.clazz;

/**
 * 
 * Adapter class, adapts Adaptee to the Target interface
 *
 */
public class Adapter extends Adaptee implements Target {
	
	public String request() {
		return this.specialRequest();
	}
}
```

#### Object Adapter
#### *Target.java* 
```java 
package com.hundredwordsgof.adapter.object;

/**
 * 
 * Target interface, defines domain-specific interface to which Adaptee will be adapted 
 *
 */
public interface Target {

	String request();	
}
```

#### *Adaptee.java* 
```java 
package com.hundredwordsgof.adapter.object;

/**
 * 
 * Adaptee class, interface which will be adapted 
 *
 */
public class Adaptee {

	public String specialRequest(){
		return "specialRequest";
	}
}
```

#### *Adapter.java* 
```java 
package com.hundredwordsgof.adapter.object;

/**
 * 
 * Adapter class, adapts Adaptee to the Target interface
 *
 */
public class Adapter implements Target {

  private Adaptee adaptee;

  public Adapter(Adaptee adaptee) {
    this.adaptee = adaptee;
  }

  public String request() {
    return adaptee.specialRequest();
  }
}
```

###  <a id="Usage"></a>Usage 

#### *ClazzAdapterTest.java* 
```java 
package com.hundredwordsgof.adapter;

import static org.junit.Assert.*;
import org.junit.Test;
import com.hundredwordsgof.adapter.clazz.Adapter;
import com.hundredwordsgof.adapter.clazz.Target;

/**
 * Test implementation of the Adapter(object) pattern.
 */
public class ClazzAdapterTest {

  @Test
  public void testAdapter() {

    // creates Adapter
    Target target = new Adapter();

    assertEquals("specialRequest", target.request());
  }
}
```

#### *ObjectAdapterTest.java* 
```java 
package com.hundredwordsgof.adapter;

import static org.junit.Assert.assertEquals;
import org.junit.Test;
import com.hundredwordsgof.adapter.object.Adaptee;
import com.hundredwordsgof.adapter.object.Adapter;
import com.hundredwordsgof.adapter.object.Target;

/**
 * Test implementation of the Adapter(object) pattern.
 */
public class ObjectAdapterTest {

  @Test
  public void testAdapter() {

    // creates Adaptee
    Adaptee adaptee = new Adaptee();

    // creates Adapter
    Target target = new Adapter(adaptee);

    assertEquals("specialRequest", target.request());
  }
}
```

