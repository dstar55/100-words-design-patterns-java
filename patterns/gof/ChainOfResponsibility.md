---
layout: page
title: Chain Of Responsibility
permalink: /patterns/ChainOfResponsibility/
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

Imagine that you just have bought a new wireless router from the local Internet Service Provider. 
You unpack a router from the box, plug the necessary cables and you switch on your new wireless router. 
But, the router is not able to establish an Internet connection. 
After checking the technical manuals and playing with router settings, you finally give up and you call the ISP operator's call center.


The first thing you hear is a machine voice of the auto responder. 
It suggests dozen of possible solutions to various problems, but none of those are related to your particular problem. 
After a while, the machine connects you to the live operator. After a short discussion, the operator realizes that he cannot help you either. 
So, he connects you to an engineer, who finally fixes your problem.


That was an example of the Chain of Responsibility.


In essence, we pass an object along a "chain" of potential handlers for that object until one of the handlers handles the request.
The Chain of Responsibility allows an object to send a command without knowing which object will receive and handle it. 
The request is sent from one object to another, making them parts of a chain and each object in this chain can handle the command, 
pass it on or do both.






###  <a id="Story"></a>Story 

A King and his army is an example of the Chain of Responsibility. 
The King gives orders to his army. The closest element to react would be the commander, 
then the officer and then the soldier and those three elements would form a Chain of Responsibility.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/chainofresponsibility.jpg "Zulu Soldiers of King Panda’s Army, 1847")  
###### By George French Angas, 1822-1886 (Bibliothèque numérique mondiale), Zulu Soldiers of King Panda’s Army, 1847 [Public domain], <a href="https://commons.wikimedia.org/wiki/File%3AZulu_soldiers_of_the_army_of_King_Umpande_(Panda)%2C_1847.png">via Wikimedia Commons</a>




###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/chainofresponsibility.png)](http://www.design-patterns-stories.com/assets/img/uml/chainofresponsibility.png)



###  <a id="Structure"></a>Structure 

A *Handler* defines interface for request handling.  
The *ConcreteHandler* handles the request, can access the next object in the chain and forward the request if necessary.  
A client initiates requests to the *ConcreteHandler*.  




###  <a id="Implementation"></a>Implementation 

#### *Handler.java* 
```java 
package com.hundredwordsgof.chainofresponsibility;

/**
 * 
 * Handler interface, declares an interface for request handling
 *
 */
abstract class Handler {

  protected Handler succesor;

  abstract void handleRequest();

  public void setSuccesor(Handler succesor) {
    this.succesor = succesor;
  }
}
```

#### *ConcreteHandler1.java* 
```java 
package com.hundredwordsgof.chainofresponsibility;

/**
 * 
 * ConcreteHandler1 class, handles the request, can access to the next object in
 * a chain and forward the request if necessary.
 * 
 */
public class ConcreteHandler1 extends Handler {

  private boolean handleRequestInvoked = false;

  void handleRequest() {

    handleRequestInvoked = true;

    // if some condition call handleRequest on successor
    if (handleRequestInvoked) {
      succesor.handleRequest();
    }
  }

  protected boolean isHandleRequestInvoked() {
    return handleRequestInvoked;
  }
}
```

#### *ConcreteHandler2.java* 
```java 
package com.hundredwordsgof.chainofresponsibility;

/**
 * 
 * ConcreteHandler2 class, handles the request, can access to the next object in
 * a chain and forward the request if necessary.
 * 
 */
public class ConcreteHandler2 extends Handler {

  private boolean handleRequestInvoked = false;

  void handleRequest() {
    handleRequestInvoked = true;
  }

  protected boolean isHandleRequestInvoked() {
    return handleRequestInvoked;
  }
}
```

###  <a id="Usage"></a>Usage 

#### *ChainOfResponsabilityTest.java* 
```java 
package com.hundredwordsgof.chainofresponsibility;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the ChainOfResponsability pattern.
 */
public class ChainOfResponsabilityTest {

  @Test
  public void testChainOfResponsability() throws Exception {

    // create two handlers
    Handler concreteHandler1 = new ConcreteHandler1();
    Handler concreteHandler2 = new ConcreteHandler2();
    // connect handler in chain
    concreteHandler1.setSuccesor(concreteHandler2);

    // handleRequest on handlers is not invoked
    assertEquals(false,
        ((ConcreteHandler1) concreteHandler1).isHandleRequestInvoked());
    assertEquals(false,
        ((ConcreteHandler2) concreteHandler2).isHandleRequestInvoked());

    concreteHandler1.handleRequest();

    // handleRequest on handlers is invoked
    assertEquals(true,
        ((ConcreteHandler1) concreteHandler1).isHandleRequestInvoked());
    assertEquals(true,
        ((ConcreteHandler2) concreteHandler2).isHandleRequestInvoked());
  }
}
```

