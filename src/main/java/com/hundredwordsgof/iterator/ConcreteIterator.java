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
