---
layout: page
title: Singleton
permalink: /Singleton/
tag: pattern
---

* [Story](#Story)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###<a id="Story"></a>Story 

Singleton ensures that only one(single) object can be created from the class.

Men's 100 meters world record holder is a singleton.
There can be at most one active "Men's 100 meters world record holder" at any given time. 
Regardless of who that person is the title, "Men's 100 meters world record holder" is a global point of access that identifies the faster person in the world.



### <a id="UML"></a>UML 
![]({{site.baseurl}}/assets/img/singleton.png)

### <a id="Implementation"></a>Implementation

##### *Singleton.java* 
```java 
package com.hundredwordsgof.singleton;

/**
 * Singleton class implements singleton pattern.
 * Only one object can be instantiated.
 * 
 */
public class Singleton {

	/** 
	 * Holds reference to single instance. 
	 */	
	private static Singleton INSTANCE;
	
	
	/** 
	 * Overrides public Constructor. 
	 */
	private Singleton(){		
	}
	
	
	/**
	 * Creates the instance if it does not yet exist(lazy instantiation).
	 * @return a reference to the single instance.
	 */	
	public static Singleton getInstance(){
		if(INSTANCE == null){
			INSTANCE = new Singleton();
		}
		return INSTANCE;
	}
}
```

### <a id="Usage"></a>Usage

usage
