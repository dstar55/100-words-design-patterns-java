package com.hundredwordsgof.adapter.clazz;

/**
 * 
 * Adapter class, adapts Adaptee to the Target interface
 *
 */
public class Adapter extends Adaptee implements Target {
	
	public String request() {
		return this.specialRequest();
	}
}
