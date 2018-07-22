---
layout: page
title: Iterator
permalink: /patterns/Iterator/
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

In computer science, a data structure is a particular way of organizing and storing data, so that it can be accessed and modified efficiently. 
More precisely, a data structure is a collection of data values, the relationships among them, and the functions or operations 
which can be applied to the data.


There are numerous types of data structures, such as linked lists, arrays, vectors, maps, etc. 
Each collection of the data structure has its own structure and its own way of accessing elements of the collection.


In practice, it is not convenient to access each type of collection in a different way, so it would be nice to have a common interface for 
element-by-element access to a collection, independent of the collection’s shape.


The Iterator pattern lets you do all this. 
The key idea is to take the responsibility for access and traversal out of the aggregate object and put it into an Iterator object which 
defines a standard traversal protocol.

So, an Iterator pattern provides a way of accessing the elements of an aggregate object sequentially, without exposing its underlying representation.





###  <a id="Story"></a>Story 

A book is a set of written, printed sheets bound together into a volume. 
You can browse through the book page by page, or quickly jump to an interesting chapter. 
The process of browsing is an example of the Iterator pattern.






###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/iterator.jpg "Iterate book page by page")  
###### Open Book by Dave Dugdale, on Flickr&quot;&nbsp;(<a rel='license' href='https://creativecommons.org/licenses/by-sa/2.0/' target='_blank'>CC BY-SA 2.0</a>)&nbsp;by&nbsp; <a xmlns:cc='http://creativecommons.org/ns#' rel='cc:attributionURL' property='cc:attributionName' href='https://www.flickr.com/people/davedugdale/' target='_blank'>Dave Dugdale</a>




###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/iterator.png)](http://www.design-patterns-stories.com/assets/img/uml/iterator.png)



###  <a id="Structure"></a>Structure 

The Iterator defines an interface for accessing and traversing elements. 
The ConcreteIterator implements the Iterator interface, keeps track of the current position in the traversal of the aggregate. 
The Aggregate defines an interface for creating an Iterator object. 
The ConcreteAgregate class implements the Iterator creation interface to return an instance of the proper ConcreteIterator.




###  <a id="Implementation"></a>Implementation 

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

#### *ConcreteIterator.java* 
```java 
package com.hundredwordsgof.iterator;

/**
 * 
 * ConcreteIterator implements the Iterator interface. Keeps track of the
 * current position in the traversal of the aggregate.
 *
 */
public class ConcreteIterator implements Iterator {

  private ConcreteAggregate concreteAggregate;
  private int index = -1;

  public ConcreteIterator(ConcreteAggregate concreteAggregate) {
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

    if (concreteAggregate.getRecords().length == (index + 1)) {
      return true;
    }
    return false;
  }

  public Object currentItem() {
    return concreteAggregate.getRecords()[index];
  }
}
```

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
 * ConcreteAgregate implements the Iterator creation interface to return an
 * instance of the proper ConcreteIterator.
 *
 */
public class ConcreteAggregate implements Aggregate {

  private final String records[] = { "first", "second", "third", "fourth" };

  public Iterator createIterator() {
    return new ConcreteIterator(this);
  }

  protected String[] getRecords() {
    return records;
  }
}
```

###  <a id="Usage"></a>Usage 

#### *IteratorTest.java* 
```java 
package com.hundredwordsgof.iterator;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the Iterator pattern.
 */
public class IteratorTest {

  @Test
  public void testIterator() throws Exception {

    Aggregate aggregate = new ConcreteAggregate();

    Iterator iterator = aggregate.createIterator();

    assertEquals("first", iterator.first());
    assertEquals("first", iterator.currentItem());
    assertEquals(false, iterator.isDone());

    assertEquals("second", iterator.next());
    assertEquals("second", iterator.currentItem());
    assertEquals(false, iterator.isDone());

    assertEquals("third", iterator.next());
    assertEquals("third", iterator.currentItem());
    assertEquals(false, iterator.isDone());

    assertEquals("fourth", iterator.next());
    assertEquals("fourth", iterator.currentItem());
    assertEquals(true, iterator.isDone());
  }
}
```

