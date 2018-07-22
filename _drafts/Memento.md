---
layout: page
title: Memento
permalink: /patterns/Memento/
tag: pattern
---

* [Motivation](#Motivation)
* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Motivation"></a>Motivation 

ModerModern cars have brakes on all four wheels, operated by a hydraulic system. 
The brakes may be disc type or drum type.


The front brakes play a greater part in stopping the car than the rear ones, because braking throws the car weight forward on to the front wheels.


Many cars therefore have disc brakes, which are generally more efficient, at the front, and drum brakes at the rear.


Imagine a scenario in which we need to replace the drum brakes at the rear by ourselves? 
How  do we ensure that the new drum brake has all the necessary pieces in their proper places? 
One solution might be to use the Memento.


The drums are removed from both sides, exposing both the right and left brakes. 
Only one side is disassembled and the other serves as a Memento of how the brake parts fit together. 
The other side is disassembled only after the job has been completed on one side. 
When the second side is disassembled, the first side acts as the Memento.


Thus we have an example of the Memento design pattern. 
Memento design pattern helps to restore an object’s state to it previous state.






###  <a id="Story"></a>Story 

Transactions are operations on the database which occur in an atomic, consistent, durable, and isolated fashion. 
A transaction can contain multiple operations on the database; each operation can succeed or fail – however, a transaction guarantees that, 
if all operations succeed, the transaction would commit and would be final. 
And if any operation fails, then the transaction would fail and all operations would roll back and leave the database in its original state, 
as if nothing has happened.

This rollback mechanism uses the Memento design pattern.
 





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/memento.jpg "States of transaction")  
###### States of transaction 



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/memento.png)](http://www.design-patterns-stories.com/assets/img/uml/memento.png)

###  <a id="Implementation"></a>Implementation 

#### *Memento.java* 
```java 
package com.hundredwordsgof.memento;

/**
 * 
 * Memento stores internal state of the Originator object, protects against
 * access by objects other than the Originator.
 *
 */
public class Memento {

  private int state;

  public Memento(int state) {
    this.state = state;
  }

  public int getState() {
    return state;
  }
}
```

#### *Originator.java* 
```java 
package com.hundredwordsgof.memento;

/**
 * 
 * Originator creates a Memento containing a snapshot of its current internal
 * state. Originator use Memento to restore its internal state.
 * 
 */
public class Originator {

  private int state;

  public void setMemento(Memento memento) {
    this.state = memento.getState();
  }

  public Memento createMemento() {
    return new Memento(this.state);
  }

  public int getState() {
    return state;
  }

  public void setState(int state) {
    this.state = state;
  }

}
```

#### *Caretaker.java* 
```java 
package com.hundredwordsgof.memento;

/**
 * 
 * Caretaker responsible for the Memento's safekeeping.
 *
 */
public class Caretaker {

  private Memento memento;

  public Memento getMemento() {
    return memento;
  }

  public void setMemento(Memento memento) {
    this.memento = memento;
  }
}
```

###  <a id="Usage"></a>Usage 

#### *MementoTest.java* 
```java 
package com.hundredwordsgof.memento;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the Memento pattern.
 */
public class MementoTest {

  @Test
  public void testVisitor() {

    // init state of the Originator
    Originator originator = new Originator();
    originator.setState(1);

    assertEquals(1, originator.getState());

    // Caretaker stores current state of the Originator
    Caretaker caretaker = new Caretaker();
    caretaker.setMemento(originator.createMemento());

    // change a Originator's state
    originator.setState(2);
    assertEquals(2, originator.getState());

    // undo Originator's initial state
    originator.setMemento(caretaker.getMemento());
    assertEquals(1, originator.getState());
  }
}
```

