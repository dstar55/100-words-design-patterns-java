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
