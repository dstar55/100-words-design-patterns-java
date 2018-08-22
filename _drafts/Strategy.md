---
layout: page
title: Strategy
permalink: /patterns/Strategy/
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

Imagine that we need to implement a network load balancer. 
The Load balancer serves as the single point of contact for clients: it distributes incoming traffic across multiple targets, 
which increases the availability and capability of your application.


The question is: how will the load balancer distribute the incoming traffic? 
We can have various algorithms, like round robin, ip-hash, least connected, etc. 
New algorithms can be introduced over time. 
So, it is obvious that an algorithm for traffic distribution can be implemented in different ways.


A straight solution would be to implement a few algorithms and hide the invocation of the algorithm in an 'if/then' or in a 'switch' statement.


Is the proposed solution flexible enough?


Another solution would be to define a common interface for our algorithm and then encapsulate the behavior of an algorithm as an object which 
implements a common interface. 
During runtime we can select which object to use and many different behaviors can be implemented without 
creating huge 'if/then' or 'switch' statements.


This solution is a Strategy pattern. 

The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. 
The Strategy lets the algorithm vary independently from the clients that use it.






###  <a id="Story"></a>Story 

Select an algorithm at runtime.


The payment options in a Shopping Cart are an example of a Strategy. 
User can choose various payment options, such as Master Card, Amex or PayPal. 
Any of these payment options will pay for the items in the Shopping Cart, and they can be used interchangeably. 
The user may choose the Strategy based on his possibilities and preferences.






###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/strategy.jpg "Credit Card")  
###### Credit Card&nbsp;(<a rel='license' href='https://creativecommons.org/licenses/by/2.0/' target='_blank'>CC BY 2.0</a>)&nbsp;by&nbsp;<a xmlns:cc='http://creativecommons.org/ns#' rel='cc:attributionURL' property='cc:attributionName' href='https://www.flickr.com/people/mecklenburg/' target='_blank'>ThomasKohler</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/strategy.png)](http://www.design-patterns-stories.com/assets/img/uml/strategy.png)



###  <a id="Structure"></a>Structure 

The *Strategy* declares an interface common to all supported algorithms.  
The *ConcreteStrategy* implements the algorithm using the *Strategy* interface.   
The *Context* uses this interface to call the algorithm defined by a *ConcreteStrategy*.  




###  <a id="Implementation"></a>Implementation 

#### *Strategy.java* 
```java 
package com.hundredwordsgof.strategy;

/**
 * Declares an interface common to all supported algorithms. Context uses this
 * interface to call the algorithm defined by a ConcreteStrategy.
 * 
 */
public interface Strategy {

  String algorithmInterface();
}
```

#### *ConcreteStrategyA.java* 
```java 
package com.hundredwordsgof.strategy;

/**
 * Implements the algorithm defined in Strategy interface.
 *
 */
public class ConcreteStrategyA implements Strategy {

  public String algorithmInterface() {
    return "Go to airport with ConcreteStrategyA, take a taxi";
  }
}
```

#### *ConcreteStrategyB.java* 
```java 
package com.hundredwordsgof.strategy;

/**
 * Implements the algorithm defined in Strategy interface.
 *
 */
public class ConcreteStrategyB implements Strategy {

  public String algorithmInterface() {
    return "Go to airport with ConcreteStrategyB, take a bus";
  }
}
```

#### *ConcreteStrategyC.java* 
```java 
package com.hundredwordsgof.strategy;

/**
 * Implements the algorithm defined in Strategy interface.
 *
 */
public class ConcreteStrategyC implements Strategy {

  public String algorithmInterface() {
    return "Go to airport with ConcreteStrategyC, take a metro";
  }
}
```

#### *Context.java* 
```java 
package com.hundredwordsgof.strategy;

/**
 * Maintains a reference to a Strategy object. Invokes algorithm implemented in
 * ConcreteStrategy.
 *
 */
public class Context {

  private Strategy strategy;

  public Context(Strategy strategy) {
    this.strategy = strategy;
  }

  protected String contextInterface() {
    return this.strategy.algorithmInterface();
  }
}
```

###  <a id="Usage"></a>Usage 

#### *StrategyTest.java* 
```java 
package com.hundredwordsgof.strategy;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the Strategy pattern.
 */
public class StrategyTest {

  @Test
  public void testStrategy() {

    Context context = new Context(new ConcreteStrategyA());
    assertEquals("Go to airport with ConcreteStrategyA, take a taxi",
        context.contextInterface());

    context = new Context(new ConcreteStrategyB());
    assertEquals("Go to airport with ConcreteStrategyB, take a bus",
        context.contextInterface());

    context = new Context(new ConcreteStrategyC());
    assertEquals("Go to airport with ConcreteStrategyC, take a metro",
        context.contextInterface());
  }
}
```

