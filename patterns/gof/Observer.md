---
layout: page
title: Observer
permalink: /patterns/Observer/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Keep me updated.

Newslettter subscription demonstrate Observer pattern.
A newsletter is a regularly distributed publication that is generally about one main topic of interest to its subscribers. 
Subscribers can subscribe or unsubscribe to the newsletters.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/observer.jpg "Newsletter")  
###### <a href="https://commons.wikimedia.org/wiki/User:Stevie_Benton_(WMUK)">Stevie Benton</a>, <a href="https://commons.wikimedia.org/wiki/File:Newsletter-banner-v2.jpg">Newsletter-banner-v2</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/legalcode">CC BY-SA 3.0</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/observer.png)](http://www.design-patterns-stories.com/assets/img/uml/observer.png)

###  <a id="Implementation"></a>Implementation 

#### *Observer.java* 
```java 
package com.hundredwordsgof.observer;

/**
 * Observer defines an updating interface for objects that should be notified of
 * changes in a subject.
 *
 */
public interface Observer {

  void update();
}
```

#### *ConcreteObserver.java* 
```java 
package com.hundredwordsgof.observer;

/**
 * ConcreteObserver maintains a reference to a ConcreteSubject object, stores
 * state that should stay consistent with the subject's, implements the Observer
 * updating interface to keep its state consistent with the subject's.
 *
 */
public class ConcreteObserver implements Observer {

  private int observerState;

  private ConcreteSubject subject;

  public ConcreteObserver(ConcreteSubject subject) {
    this.subject = subject;
  }

  public void update() {
    observerState = subject.getState();
  }

  protected int getObserverState() {
    return observerState;
  }
}
```

#### *Subject.java* 
```java 
package com.hundredwordsgof.observer;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Subject knows its observers. Any number of Observer objects may observe a
 * subject.
 *
 */
abstract class Subject {

  private List<Observer> observers = new ArrayList<Observer>();

  public void attach(Observer observer) {
    observers.add(observer);
  }

  public void dettach(Observer observer) {
    observers.remove(observer);
  }

  public void notifyObervers() {
    for (Iterator iterator = observers.iterator(); iterator.hasNext();) {
      Observer observer = (Observer) iterator.next();
      observer.update();
    }
  }
}
```

#### *ConcreteSubject.java* 
```java 
package com.hundredwordsgof.observer;

/**
 * ConcreteSubject stores state of interest to ConcreteObserver objects, sends a
 * notification to its observers when its state changes.
 *
 */
public class ConcreteSubject extends Subject {

  private int state;

  public int getState() {
    return state;
  }

  public void setState(int state) {
    this.state = state;
    this.notifyObervers();
  }
}
```

###  <a id="Usage"></a>Usage 

#### *ObserverTest.java* 
```java 
package com.hundredwordsgof.observer;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test Observer pattern.
 */
public class ObserverTest {

  @Test
  public void testObserver() throws CloneNotSupportedException {

    ConcreteSubject subject = new ConcreteSubject();

    Observer observer = new ConcreteObserver(subject);
    subject.attach(observer);
    subject.setState(1);

    // changes via subject.setState is propagated towards observer
    assertEquals(1, ((ConcreteObserver) observer).getObserverState());

    subject.dettach(observer);
    subject.setState(0);

    // observer is detached so changes are not propageted
    assertEquals(1, ((ConcreteObserver) observer).getObserverState());
  }
}
```

