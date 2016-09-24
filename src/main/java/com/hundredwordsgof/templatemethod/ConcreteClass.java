package com.hundredwordsgof.templatemethod;

/**
 * 
 * Implements the primitive operations to carry out subclass-specific steps of the algorithm.
 *
 */
public class ConcreteClass extends AbstractClass{

	String primitiveOperation1() {
		return "Template";
	}


	String primitiveOperation2() {
		return "Method";
	}

}
