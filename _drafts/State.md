---
layout: page
title: State
permalink: /patterns/State/
tag: pattern
---

* [Motivation](#Motivation)
* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Structure](#Structure)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Motivation"></a>Motivation 

Imagine that we need to implement a state machine. 
We begin with a few states, and a few simple conditions for those states. 
Our initial State machine is implemented using if/else blocks, which are checking the current state and which perform the appropriate actions.


But, the number of states gradually increases over time. 
In addition, the conditions for reaching certain states become more complex. 
Our 'if/else' based state machine has more and more 'if/else' blocks and it becomes really difficult to maintain and debug such a code base.


Is there a more elegant way to implement the State Machine?


Another approach would be that, for every possible state, a separate class is implemented over a common  interface, with the state related behavior. 
The Context class will contain a reference to a state object, which represents its current state. 
Instead of acting on its own, the context will delegate the execution to the state object. 
To change the state of the context, one would pass another state object to the context.


This solution is an example of the State pattern.


The State pattern allows an object to alter its behavior when its internal state changes.






###  <a id="Story"></a>Story 

Behavior depends on its state.


Pregnancy is a time of great physical and emotional change for women. 
Everything from the size of her belly to the speed at which her heart beats will change over the nine months leading up to the childbirth. 
Partly as the result of hormonal fluctuations, and partly due to the physical strain of carrying extra body weight, 
pregnant women can expect to buy new bras, search for ways to alleviate swollen ankles, gasp for breath after climbing a few stairs, 
and marvel at how quickly their nails grow.






###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/state.jpg "Human Pregnancy")  
###### <a href="https://commons.wikimedia.org/wiki/File:Pregnant_graffiti.jpg">Pregnant graffiti</a> by, <a href="http://flickr.com/photos/19616008@N00">Petteri Sulonen from Helsinki, Finland</a>, <a href="https://creativecommons.org/licenses/by/2.0/legalcode">CC BY 2.0</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/state.png)](http://www.design-patterns-stories.com/assets/img/uml/state.png)



###  <a id="Structure"></a>Structure 

The *State* defines an interface for encapsulating the behavior associated with a particular state of the Context.  
The *ConcreteState* implements a behavior associated with the state of the *Context*.  
The *Context* class maintains an instance of a *ConcreteState* subclass which defines the current state.  




###  <a id="Implementation"></a>Implementation 

#### *State.java* 
```java 
package com.hundredwordsgof.state;

/**
 * The interface for encapsulating the behavior associated with a particular
 * state of the Context.
 *
 */
public interface State {

  void handle();
}
```

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

  protected boolean isHandleInvoked() {
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

  protected boolean isHandleInvoked() {
    return handleInvoked;
  }
}
```

#### *Context.java* 
```java 
package com.hundredwordsgof.state;

/**
 * Context maintains an instance of a ConcreteState subclass that defines the
 * current state.
 *
 */
public class Context {

  private State state;

  public void request() {
    state.handle();
  }

  public void setState(State state) {
    this.state = state;
  }
}
```

###  <a id="Usage"></a>Usage 

#### *StateTest.java* 
```java 
package com.hundredwordsgof.state;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the State pattern.
 */
public class StateTest {

  @Test
  public void testState() {

    State state1 = new ConcreteState1();
    State state2 = new ConcreteState2();

    assertEquals(false, ((ConcreteState1) state1).isHandleInvoked());
    assertEquals(false, ((ConcreteState2) state2).isHandleInvoked());

    Context context = new Context();
    context.setState(state1);
    context.request();

    assertEquals(true, ((ConcreteState1) state1).isHandleInvoked());

    context.setState(state2);
    context.request();

    assertEquals(true, ((ConcreteState2) state2).isHandleInvoked());
  }
}
```

