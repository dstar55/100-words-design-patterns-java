---
layout: page
title: Iterator
permalink: /patterns/Iterator/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Book is a set of written, printed sheets bound together into a volume.
You can browse through the book page by page, or quickly jump to interesting chapter.
Process of browsing is example of Iterator pattern.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/iterator.jpg "Iterate book page by page")  
###### Open Book by Dave Dugdale, on Flickr&quot;&nbsp;(<a rel='license' href='https://creativecommons.org/licenses/by-sa/2.0/' target='_blank'>CC BY-SA 2.0</a>)&nbsp;by&nbsp; <a xmlns:cc='http://creativecommons.org/ns#' rel='cc:attributionURL' property='cc:attributionName' href='https://www.flickr.com/people/davedugdale/' target='_blank'>Dave Dugdale</a>




###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/iterator.png)](http://www.design-patterns-stories.com/assets/img/uml/iterator.png)

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

