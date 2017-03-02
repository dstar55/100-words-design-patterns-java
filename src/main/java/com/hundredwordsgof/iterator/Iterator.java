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
