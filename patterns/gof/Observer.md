---
layout: page
title: Observer
permalink: /Observer/
tag: pattern
---



### Story 

Keep me updated.

Newslettter subscription demonstrate Observer pattern.
A newsletter is a regularly distributed publication that is generally about one main topic of interest to its subscribers. 
Subscribers can subscribers or unsubscribers to the newsletters.



### UML 
![]({{site.baseurl}}/assets/img/observer.png)

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/observer/ConcreteObserver.java
```java 
package com.hundredwordsgof.observer;

/**
 * ConcreteObserver maintains a reference to a ConcreteSubject object, stores state that should stay consistent with the subject's, 
 * implements the Observer updating interface to keep its state consistent with the subject's.
 *
 */
public class ConcreteObserver implements Observer{

	private int observerState;
	
	private ConcreteSubject subject;
	
	public ConcreteObserver(ConcreteSubject subject){
		this.subject = subject;
	}
	
	public void update() {
		observerState = subject.getState();
	}

	public int getObserverState() {
		return observerState;
	}

	
}
```

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/observer/ConcreteSubject.java
```java 
package com.hundredwordsgof.observer;


/**
 * ConcreteSubject stores state of interest to ConcreteObserver objects, sends a notification to its observers when its state changes.
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

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/observer/Observer.java
```java 
package com.hundredwordsgof.observer;

/**
 * Observer defines an updating interface for objects that should be notified of changes in a subject.
 *
 */
public interface Observer {

	void update();
	
}
```

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/observer/Subject.java
```java 
package com.hundredwordsgof.observer;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Subject knows its observers. Any number of Observer objects may observe a subject.
 *
 */
abstract class Subject {

	private List<Observer> observers = new ArrayList<Observer>(); 

	public void attach(Observer observer){
		observers.add(observer);
	}
	
	public void dettach(Observer observer){
		observers.remove(observer);
	}
	
	public void notifyObervers(){
		for (Iterator iterator = observers.iterator(); iterator.hasNext();) {
			Observer observer = (Observer) iterator.next();
			observer.update();
		}
	}
}
```

