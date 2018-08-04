---
layout: page
title: Mediator
permalink: /patterns/Mediator/
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

Imagine that we need to develop a flight simulator. Our flight simulator will have base artifacts, like airport and aircraft. 
An aircraft can take off from the airport, fly in the sky and land on the airport.


Imagine a scenario when one particular aircraft is landing on the airport: how can that aircraft be sure that the other aircrafts are not 
trying to land on the same airport at the same time? It is obvious that our aircraft can't talk to each and every aircraft which is currently 
approaching the airport.


A better approach would be to introduce a mediator, which is a "man in the middle", meaning that all the aircrafts will communicate only with the mediator. 
The task of ensuring the safe operations of the aircrafts belongs to air traffic controllers, who are mediators. 
They must coordinate the movements of all the aircrafts, keep them at safe distances from each other, direct them during takeoff and landing, 
direct them around bad weather and ensure that the air traffic flows smoothly with minimal delays.


The example above is a Mediator pattern. The Mediator pattern defines an object that controls how a set of objects interacts.






###  <a id="Story"></a>Story 

A Radio Taxi is an example of the Mediator pattern. 
The taxi drivers communicate with the Mediator (Radio Taxi Call Center), rather than with each other.


When a customer needs a taxi, he calls the Radio Taxi Call Center. 
All taxis have GPS units, which tell the Radio Taxi Call Center the taxis' current locations; there is also a central information system, 
which tells which taxi is currently available to serve the customer. 
The call center will contact the available taxi nearest to customer’s location and send it to serve the customer.






###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/mediator.jpg "Call Center Taxis Libres")  
###### Call Center Taxis Libres,By Jquemba (Own work) [Public domain], via Wikimedia Commons 



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/mediator.png)](http://www.design-patterns-stories.com/assets/img/uml/mediator.png)



###  <a id="Structure"></a>Structure 

A *Colleague* defines an interface for communication with another *Colleague* via the *Mediator*. 
For the *ConcreteColleague* class, each *Colleague* class knows its *Mediator* object, and each *Colleague* communicates with its mediator 
whenever it would have otherwise communicated with another colleague. 
The *Mediator* defines an interface for communicating with *Colleague* objects. 
The *ConcreteMediator* implements cooperative behavior by coordinating the *Colleague* objects.




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

