---
layout: page
title: Adapter
permalink: /patterns/Adapter/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Allows that interface of an existing class to be used from another interface.

Adapters are often used in daily life, for example eletrical adapter is a device that 
converts attributes of one electrical device or system to those of an otherwise incompatible device or system. 
Some modify power or signal attributes, while others merely adapt the physical form of one electrical connector to another.





###  <a id="Image"></a>Image 


![alt text](/assets/img/adapter.jpg "Adapter")  
###### <a href="https://commons.wikimedia.org/wiki/User:Lionel_Allorge">Lionel Allorge</a>, <a href="https://commons.wikimedia.org/wiki/File:Adaptateur_de_prise_française_en_prise_suisse_2.jpg">Adaptateur de prise française en prise suisse 2</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/legalcode">CC BY-SA 3.0</a>



###  <a id="UML"></a>UML 
[![](/assets/img/uml/adapter.png)](/assets/img/uml/adapter.png)

###  <a id="Implementation"></a>Implementation 

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

