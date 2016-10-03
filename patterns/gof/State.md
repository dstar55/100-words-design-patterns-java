---
layout: page
title: State
permalink: /State/
tag: pattern
---



### Story 

Behavior depends on its state.

Pregnancy is time of great physical and emotional change for women. 
Everything from the size of her belly to the speed at which her heart beats will change over the nine months leading up to childbirth. 
Partly the result of hormonal fluctuations and partly the physical strain of carrying extra body weight, pregnant women can expect to buy new bras, 
search for ways to alleviate swollen ankles, gasp for breath after climbing a few stairs, and marvel at how quickly their nails grow.



### UML 
![]({{site.baseurl}}/assets/img/state.png)

#### *ConcreteState1.java* 
```java 
package com.hundredwordsgof.state;

/** 
 * ConcreteState1 implements a behavior associated with a state of the Context.
 *
 */
public class ConcreteState1 implements State {

	private boolean handleInvoked = false;
	
	public void handle() {
		this.handleInvoked = true;
	}

	public boolean isHandleInvoked() {
		return handleInvoked;
	}

}
```

#### *ConcreteState2.java* 
```java 
package com.hundredwordsgof.state;

/** 
 * ConcreteState2 implements a behavior associated with a state of the Context.
 *
 */
public class ConcreteState2 implements State {

	private boolean handleInvoked = false;
	
	public void handle() {
		this.handleInvoked = true;		
	}

	public boolean isHandleInvoked() {
		return handleInvoked;
	}
	
}
```

#### *Context.java* 
```java 
package com.hundredwordsgof.state;

/** 
 * Context maintains an instance of a ConcreteState subclass that defines the current state.
 *
 */
public class Context {

	private State state;
	
	public void request(){
		state.handle();
	}

	public void setState(State state) {
		this.state = state;
	}
	
	
}
```

#### *State.java* 
```java 
package com.hundredwordsgof.state;

/**
 * The interface for encapsulating the behavior associated with a particular state of the Context.
 *
 */
public interface State {

	void handle();
	
}
```

