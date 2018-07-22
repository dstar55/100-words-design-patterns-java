---
layout: page
title: Proxy
permalink: /patterns/Proxy/
tag: pattern
---

* [Motivation](#Motivation)
* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Motivation"></a>Motivation 

Imagine that we are implementing a Viewer application, which will show a Microsoft Word document in read only mode.

The Viewer must open and load document quickly, but the problem is that during loading of the document, 
we don't know if there are any "heavy" objects inside a document. 
A heavy object can be an image which is injected in a Word document on, let's say, page 10 of the document.

So, a straight solution where we simply load everything that is inside the document can be slow.


Another solution would be that heavy objects are loaded on demand: in our example, 
an image will be loaded when the user is on the page 10 of the document. 
Meanwhile, the heavy object will be presented by another, "lighter" object, which acts as original.


That solution is a Proxy.


The Proxy pattern provides a surrogate or a placeholder for another object to control access to it.






###  <a id="Story"></a>Story 

An Envoy Extraordinary is a Proxy. 
He is an accredited messenger, agent, or representative, who is sent by one government to represent it in dealings with another government.






###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/proxy.jpg "The Envoy Extraordinary")  
###### Burmese ambassador, The Envoy Extraordinary and Minister Plenipotentiary, By John Watkins (Kenwoon Mengyee) [Public domain or Public domain], <a href="https://commons.wikimedia.org/wiki/File%3AKinwun_Mingyi.jpg">via Wikimedia Commons</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/proxy.png)](http://www.design-patterns-stories.com/assets/img/uml/proxy.png)

###  <a id="Implementation"></a>Implementation 

#### *Subject.java* 
```java 
package com.hundredwordsgof.proxy;

/**
 * Subject interface defines common interface for RealSubject and Proxy
 * 
 */
public interface Subject {

  void doOperation();
}
```

#### *RealSubject.java* 
```java 
package com.hundredwordsgof.proxy;

/**
 * RealSubject class is a real object which is represented by Proxy
 * 
 */
public class RealSubject implements Subject {

  public void doOperation() {
  }
}
```

#### *Proxy.java* 
```java 
package com.hundredwordsgof.proxy;

/**
 * Proxy class keep reference on a real subject, define interface which
 * represents Subject, so he can: - act as a surogate - controll acces to real
 * subject - can be responisble for creation and maintainence of the real
 * subject
 * 
 */
public class Proxy implements Subject {

  private RealSubject realSubject;

  public void doOperation() {
    this.realSubject = new RealSubject();
    this.realSubject.doOperation();
  }

  public RealSubject getRealSubject() {
    return realSubject;
  }
}
```

###  <a id="Usage"></a>Usage 

#### *ProxyTest.java* 
```java 
package com.hundredwordsgof.proxy;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

import org.junit.Test;

/**
 * Test implementation of the Proxy pattern.
 */
public class ProxyTest {

  @Test
  public void testProxy() {

    Proxy proxy = new Proxy();

    // realSubject is not created yet, therefore we expect null
    assertEquals(null, proxy.getRealSubject());

    proxy.doOperation();

    assertNotNull(proxy.getRealSubject());
  }
}
```

