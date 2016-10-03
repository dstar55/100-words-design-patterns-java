---
layout: page
title: Flyweight
permalink: /Flyweight/
tag: pattern
---

* [Story](#Story)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Remove duplicates.

Flyweight pattern is used to reduce memory by loading only the data necessary to perform action.
Database normalization is flyweight. Normalisation, is the process of organizing the columns (attributes) and tables (relations) of a relational database to minimize data redundancy.



###  <a id="UML"></a>UML 
![]({{site.baseurl}}/assets/img/flyweight.png)

###  <a id="Implementation"></a>Implementation 

#### *ConcreteFlyweight.java* 
```java 
package com.hundredwordsgof.flyweight;

/**
 * 
 * ConcreteFlyweight,implements Flyweight, and add storage for intrisnic state 
 *
 */
public class ConcreteFlyweight implements Flyweight{

	private Object intrinsicState;

	public ConcreteFlyweight(Object intrinsicState){
		this.intrinsicState = intrinsicState;
	}
	
	// Using extrinsicState as context and does NOT modify intrinsic state.
	public void operation(Object extrinsicState) {
	}

	
	/**
	 * @return intrinsic state
	 */
	public Object getIntrinsicState() {
		return intrinsicState;
	}

	
}
```

#### *Flyweight.java* 
```java 
package com.hundredwordsgof.flyweight;

/**
 * 
 * Flyweight, interface through flyweight can recieve and act on extrinic state
 *
 */
public interface Flyweight {

	void operation(Object extrinsicState);
	
}
```

#### *FlyweightFactory.java* 
```java 
package com.hundredwordsgof.flyweight;

import java.util.HashMap;
import java.util.Map;

/**
 * 
 * FlyweightFactory, creates and manages the flyweight objects
 *
 */
public class FlyweightFactory {

	private static Map<String, Flyweight> flyweights=new HashMap<String, Flyweight>();
	/*static
	{
		flyweights.put("firstKey", new ConcreteFlyweight("firstValue"));
		flyweights.put("secondKey", new ConcreteFlyweight("secondValue"));

	}*/
	
	
	/**
	 * Returns Flyweight object. 
	 * Just for sake of example following logic is applied, if key starts with phrase:unshared than UnsharedConcreteFlyweight object is created.
	 * Otherwise ConcreteFlyweight object is created.
	 * 
	 * @param key
	 * @return Flyweight
	 * 
	 */
	public static Flyweight getFlyweight(String key, String value){
		
		if(key.startsWith("unshared")){			
			flyweights.put(key, new UnsharedConcreteFlyweight(value));
		}else{		
			if(!flyweights.containsKey(key)){
				flyweights.put(key, new ConcreteFlyweight(value));				
			}						
		}
		
		return (Flyweight)flyweights.get(key);
	}
}
```

#### *UnsharedConcreteFlyweight.java* 
```java 
package com.hundredwordsgof.flyweight;

/**
 * 
 * UnsharedConcreteFlyweight, defines objects which are not shared
 *
 */
public class UnsharedConcreteFlyweight implements Flyweight{

	private Object state;

	public UnsharedConcreteFlyweight(Object state){
		this.state = state;
	}
	
	public void operation(Object extrinsicState) {

	}

	public Object getState() {
		return state;
	}
	
}
```

###  <a id="Usage"></a>Usage 

usage 

