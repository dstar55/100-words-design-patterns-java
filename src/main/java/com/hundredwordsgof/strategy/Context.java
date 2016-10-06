package com.hundredwordsgof.strategy;

/**
 * Maintains a reference to a Strategy object.
 * Invokes algorithm implemented in ConcreteStrategy.
 *
 */
public class Context {

	private Strategy strategy;
	
	public Context(Strategy startegy){
		this.strategy = startegy;
	}

	protected String contextInterface(){
		return this.strategy.algorithmInterface();
	}
}

