package com.hundredwordsgof.visitor;

/**
 * Implements accept operation.
 *
 */
public class ConcreteElementB implements Element {

	private int counter = 0;
	
	public void accept(Visitor visitor) {
		
		visitor.visitConcreteElementB(this);
	}

	public void operationB(){
		counter++;
	}

	public int getCounter() {
		return counter;
	}
	
	
}
