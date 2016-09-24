package com.hundredwordsgof.chainofresponsibility;

/**
 * 
 * ConcreteHandler1 class, handles the request, can access to the next object in a chain and forward the request if necesary
 * 
 */
public class ConcreteHandler2 extends Handler {

	private boolean hanldeRequestInvoked = false;
	
	void handleRequest() {
		hanldeRequestInvoked = true;
	}

	public boolean isHanldeRequestInvoked() {
		return hanldeRequestInvoked;
	}
	
}
