---
layout: page
title: Chain Of Responsibility
permalink: /patterns/ChainOfResponsibility/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

The Chain of Responsibility allows an object to send a command without knowing which object will receive and handle it. 
The request is sent from one object to another making them parts of a chain and each object in this chain can handle the command, pass it on or do both. 

Service request to call center is example of the Chain of Responsibility. 
Request can be handled at front desk level, supervisor level or any higher level. 
Correct handler of request is only known during execution of the request when request is traversing at various levels. 





###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/chainofresponsibility.png)](http://www.design-patterns-stories.com/assets/img/uml/chainofresponsibility.png)

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

