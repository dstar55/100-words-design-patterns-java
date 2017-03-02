package com.hundredwordsgof.visitor;

/**
 * Defines an Accept operation that takes a visitor as an argument.
 * 
 */
public interface Element {

  void accept(Visitor visitor);
}
