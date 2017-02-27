---
layout: page
title: Adapter
permalink: /patterns/Adapter/
tag: pattern
---

* [Story](#Story)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Allows that interface of an existing class to be used from another interface.

Adapters are often used in daily life, for example eletrical adapter is a device that 
converts attributes of one electrical device or system to those of an otherwise incompatible device or system. 
Some modify power or signal attributes, while others merely adapt the physical form of one electrical connector to another.



###  <a id="UML"></a>UML 
[![](/assets/img/adapter.png)](/assets/img/adapter.png)

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

