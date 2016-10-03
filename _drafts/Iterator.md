---
layout: page
title: Iterator
permalink: /Iterator/
tag: pattern
---



### Story 

Book is a set of written, printed sheets bound together into a volume.
You can browse through the book page by page, or quickly jump to interesting chapter.
Process of browsing is example of Iterator pattern.



### UML 
![]({{site.baseurl}}/assets/img/iterator.png)

#### *Aggregate.java* 
```java 
package com.hundredwordsgof.iterator;

/**
* 
* Aggregate defines an interface for creating an Iterator object.
*
*/
public interface Aggregate {

	Iterator createIterator();
	
}
```

#### *ConcreteAggregate.java* 
```java 
package com.hundredwordsgof.iterator;

/**
 * 
 * ConcreteAgregate implements the Iterator creation interface to return an instance of the proper ConcreteIterator.
 *
 */
public class ConcreteAggregate implements Aggregate {

	private final String records[] = { "first", "second", "third", "fourth" };
	
	public Iterator createIterator() {
		return new ConcreteIterator(this);
	}

	public String[] getRecords() {
		return records.clone();
	}

	
}
```

#### *ConcreteIterator.java* 
```java 
package com.hundredwordsgof.iterator;

/**
* 
* ConcreteIterator implements the Iterator interface, keeps track of the current position in the traversal of the aggregate.
*
*/
public class ConcreteIterator implements Iterator {
	
	private ConcreteAggregate concreteAggregate;
	private int index = -1;
	
	public ConcreteIterator(ConcreteAggregate concreteAggregate){
		this.concreteAggregate = concreteAggregate;
	}

	public Object first() {
		index = 0;
		return concreteAggregate.getRecords()[index];
	}

	public Object next() {
		index++;
		return concreteAggregate.getRecords()[index];
	}

	public boolean isDone() {

		if(concreteAggregate.getRecords().length == (index+1)){
			return true;
		}
		return false;
	}

	public Object currentItem() {
		return concreteAggregate.getRecords()[index];
	}
	

}
```

#### *Iterator.java* 
```java 
package com.hundredwordsgof.iterator;

/**
 * 
 * Iterator defines an interface for accessing and traversing elements.
 *
 */
public interface Iterator {

	Object first();
	
	Object next();
	
	boolean isDone();
	
	Object currentItem();
	
}
```

