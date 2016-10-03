---
layout: page
title: Memento
permalink: /Memento/
tag: pattern
---



### Story 

Helps to restore an object’s state to it previous state.

Transactions are operations on the database that occur in an atomic, consistent, durable, and isolated fashion. 
A transaction can contain multiple operations on the database; each operation can succeed or fail, however a transaction guarantees that if all operations succeed, 
the transaction would commit and would be final. 
And if any operation fails, then the transaction would fail and all operations would rollback and leave the database as if nothing has happened.

This mechanism of rolling back uses the memento design pattern. 



### UML 
![]({{site.baseurl}}/assets/img/memento.png)

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/memento/Caretaker.java
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

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/memento/Memento.java
```java 
package com.hundredwordsgof.memento;

/**
* 
* Memento stores internal state of the Originator object, protects against access by objects other than the Originator.
*
*/
public class Memento {

	private int state;

	public Memento(int state){
		this.state = state;
	}
	
	public int getState() {
		return state;
	}

	
}
```

#### ./100-words-design-patterns-java/src/main/java/com/hundredwordsgof/memento/Originator.java
```java 
package com.hundredwordsgof.memento;

/**
 * 
 * Originator creates a Memento containing a snapshot of its current internal state.
 * Originator use Memento to restore its internal state.
 * 
 *
 */
public class Originator {

	private int state;
	
	public void setMemento(Memento memento){
		this.state = memento.getState();
	}
	
	public Memento createMemento(){
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

