package com.hundredwordsgof.flyweight;

/**
 * 
 * Flyweight, interface through flyweight can recieve and act on extrinic state
 *
 */
public interface Flyweight {

	void operation(Object extrinsicState);
	
}
