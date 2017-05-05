---
layout: page
title: State
permalink: /patterns/State/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Behavior depends on its state.

Pregnancy is time of great physical and emotional change for women. 
Everything from the size of her belly to the speed at which her heart beats will change over the nine months leading up to childbirth. 
Partly the result of hormonal fluctuations and partly the physical strain of carrying extra body weight, pregnant women can expect to buy new bras, 
search for ways to alleviate swollen ankles, gasp for breath after climbing a few stairs, and marvel at how quickly their nails grow.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/state.jpg "Human Pregnancy")  
###### <a href="http://flickr.com/photos/19616008@N00">Petteri Sulonen from Helsinki, Finland</a>, <a href="https://commons.wikimedia.org/wiki/File:Pregnant_graffiti.jpg">Pregnant graffiti</a>, <a href="https://creativecommons.org/licenses/by/2.0/legalcode">CC BY 2.0</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/state.png)](http://www.design-patterns-stories.com/assets/img/uml/state.png)

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

