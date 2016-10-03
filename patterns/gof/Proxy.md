---
layout: page
title: Proxy
permalink: /Proxy/
tag: pattern
---

* [Story](#Story)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Provide a surrogate or placeholder for another object to control access to it.

Envoy Extraordinary is a Proxy. 
He is an accredited messenger, agent, or representative who is sent by one government to represent it in dealing with another government.




###  <a id="UML"></a>UML 
![]({{site.baseurl}}/assets/img/proxy.png)

#### *Proxy.java* 
```java 
package com.hundredwordsgof.proxy;

/**
 * Proxy class keep reference on a real subject, define interface which represents Subject, so he can:
 * - act as a surogate  
 * - controll acces to real subject 
 * - can be responisble for creation and maintainence of the real subject
 * 
 */
public class Proxy implements Subject {

	private RealSubject realSubject;
		
	public void doOperation() {
		
		this.realSubject = new RealSubject();		
		this.realSubject.doOperation();
		
	}

	public RealSubject getRealSubject() {
		return realSubject;
	}

	
}
```

#### *RealSubject.java* 
```java 
package com.hundredwordsgof.proxy;

/**
 * RealSubject class is a real object which is represented by Proxy 
 * 
 */
public class RealSubject implements Subject {

	public void doOperation() {
	}

}
```

#### *Subject.java* 
```java 
package com.hundredwordsgof.proxy;

/**
 * Subject interface defines common interface for RealSubject and Proxy
 * 
 */
public interface Subject {

	void doOperation();
	
}
```

