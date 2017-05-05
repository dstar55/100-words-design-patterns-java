---
layout: page
title: Mediator
permalink: /patterns/Mediator/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Defines an object that controls how a set of objects interact.

Radio Taxi is an example of the Mediator pattern.
Taxi drivers communicate with the Mediator(Radio Taxi Call Center), rather than with each other. 

When customer needs a taxi, he calls Radio Taxi Call Center. 
All taxis have a GPS unit which tells where the taxi is present right now, also there is a central information system which tells which taxi is available to serve the customer. 
The call center will contact the available taxi nearest to customer’s location and send them to serve the customer.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/mediator.jpg "Call Center Taxis Libres")  
###### Call Center Taxis Libres,By Jquemba (Own work) [Public domain], via Wikimedia Commons 



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/mediator.png)](http://www.design-patterns-stories.com/assets/img/uml/mediator.png)

###  <a id="Implementation"></a>Implementation 

#### *Colleague.java* 
```java 
package com.hundredwordsgof.mediator;

/**
 * Colleague defines an interface for communication with another Colleague via
 * mediator.
 *
 */
abstract class Colleague {

  protected Mediator mediator;

  private String receivedMessage;

  public Colleague(Mediator mediator) {
    this.mediator = mediator;
  }

  abstract void notifyColleague(String message);

  abstract void receive(String message);

  protected String getReceivedMessage() {
    return this.receivedMessage;
  }

  protected void setReceivedMessage(String receivedMessage) {
    this.receivedMessage = receivedMessage;
  }
}
```

#### *ConcreteColleague1.java* 
```java 
package com.hundredwordsgof.mediator;

/**
 * ConcreteColleague1 implements Colleague interface.
 *
 */
public class ConcreteColleague1 extends Colleague {

  public ConcreteColleague1(Mediator mediator) {
    super(mediator);
  }

  public void notifyColleague(String message) {
    this.mediator.notifyColleague(this, message);
  }

  public void receive(String message) {
    this.setReceivedMessage(message);
  }
}
```

#### *ConcreteColleague2.java* 
```java 
package com.hundredwordsgof.mediator;

/**
 * ConcreteColleague2 implements Colleague interface.
 *
 */
public class ConcreteColleague2 extends Colleague {

  public ConcreteColleague2(Mediator mediator) {
    super(mediator);
  }

  public void notifyColleague(String message) {
    this.mediator.notifyColleague(this, message);
  }

  public void receive(String message) {
    this.setReceivedMessage(message);
  }
}
```

#### *Mediator.java* 
```java 
package com.hundredwordsgof.mediator;

/**
 * Mediator defines an interface for communicating with Colleague objects.
 *
 */
public interface Mediator {

  void notifyColleague(Colleague colleague, String message);
}
```

#### *ConcreteMediator.java* 
```java 
package com.hundredwordsgof.mediator;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * ConcreteMediator implements Mediator, coordinates between Colleague objects.
 *
 */
public class ConcreteMediator implements Mediator {

  private List<Colleague> colleagues;

  public ConcreteMediator() {
    colleagues = new ArrayList<Colleague>();
  }

  public void addColleague(Colleague colleague) {
    colleagues.add(colleague);
  }

  public void notifyColleague(Colleague colleague, String message) {

    for (Iterator iterator = colleagues.iterator(); iterator.hasNext();) {
      Colleague receiverColleague = (Colleague) iterator.next();

      if (colleague != receiverColleague) {
        receiverColleague.receive(message);
      }
    }
  }
}
```

###  <a id="Usage"></a>Usage 

#### *MediatorTest.java* 
```java 
package com.hundredwordsgof.mediator;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

/**
 * Test implementation of the Mediator pattern.
 */
public class MediatorTest {

  @Test
  public void testMediator() {

    ConcreteMediator mediator = new ConcreteMediator();

    Colleague colleague1 = new ConcreteColleague1(mediator);
    Colleague colleague2 = new ConcreteColleague2(mediator);

    mediator.addColleague(colleague1);
    mediator.addColleague(colleague2);

    colleague1.notifyColleague("Hello from ConcreteColleague1");
    colleague2.notifyColleague("Hello from ConcreteColleague2");

    assertEquals("Hello from ConcreteColleague2",
        ((ConcreteColleague1) colleague1).getReceivedMessage());
    assertEquals("Hello from ConcreteColleague1",
        ((ConcreteColleague2) colleague2).getReceivedMessage());
  }
}
```

