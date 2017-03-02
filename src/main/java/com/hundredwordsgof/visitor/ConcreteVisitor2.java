package com.hundredwordsgof.visitor;

/**
 * Implements operation declared by Visitor. Each operation implements a
 * fragment of the algorithm defined for the corresponding class of object in
 * the structure.
 *
 */
public class ConcreteVisitor2 implements Visitor {

  public void visitConcreteElementA(ConcreteElementA concreteElementA) {
    concreteElementA.operationA();
  }

  public void visitConcreteElementB(ConcreteElementB concreteElementB) {
    concreteElementB.operationB();
  }
}
