package com.hundredwordsgof.strategy;

/**
 * Maintains a reference to a Strategy object.
 * Invokes algorithm implemented in ConcreteStrategy.
 *
 */
public class Context {

	private Strategy startegy;
	
	public Context(Strategy startegy){
		this.startegy = startegy;
	}

	public String contextInterface(){
		return this.startegy.algorithmInterface();
	}
}

