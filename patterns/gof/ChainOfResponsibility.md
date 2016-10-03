---
layout: page
title: Chain Of Responsibility
permalink: /ChainOfResponsibility/
tag: pattern
---



### Story 

The Chain of Responsibility allows an object to send a command without knowing which object will receive and handle it. 
The request is sent from one object to another making them parts of a chain and each object in this chain can handle the command, pass it on or do both. 

Service request to call center is example of the Chain of Responsibility. 
Request can be handled at front desk level, supervisor level or any higher level. 
Correct handler of request is only known during execution of the request when request is traversing at various levels. 





### UML 
![]({{site.baseurl}}/assets/img/chainofresponsibility.png)

#### ConcreteHandler1.java
```java 
package com.hundredwordsgof.chainofresponsibility;

/**
 * 
 * ConcreteHandler1 class, handles the request, can access to the next object in a chain and forward the request if necesary
 * 
 */
public class ConcreteHandler1 extends Handler {

	private boolean hanldeRequestInvoked = false;
	
	void handleRequest() {

		hanldeRequestInvoked = true;
		
		// if some condition call handleRequest on successor
		if(hanldeRequestInvoked){
			succesor.handleRequest();
		}
	}

	public boolean isHanldeRequestInvoked() {
		return hanldeRequestInvoked;
	}

	
}
```

#### ConcreteHandler2.java
```java 
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
```

#### Handler.java
```java 
package com.hundredwordsgof.chainofresponsibility;


/**
 * 
 * Handler interface, declares an interface for request handling 
 *
 */
abstract class Handler {

	protected Handler succesor;
	
	abstract void handleRequest();

	public void setSuccesor(Handler succesor) {
		this.succesor = succesor;
	}
	
}
```

