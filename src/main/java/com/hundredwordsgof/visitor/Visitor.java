package com.hundredwordsgof.visitor;

/**
 * Declares a Visit operation for each class of ConcreteElement in the object
 * structure
 * 
 */
public interface Visitor {

  void visitConcreteElementA(ConcreteElementA concreteElementA);

  void visitConcreteElementB(ConcreteElementB concreteElementB);
}
