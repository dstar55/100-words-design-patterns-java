---
layout: page
title: Strategy
permalink: /patterns/Strategy/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Select an algorithm at runtime.

Payment options in a Shopping Cart is an example of Strategy.
User can choose various payment options like Master Card, Amex or PayPal.
Any of these payment options will pay items in Shopping Cart, and they can be used interchangeably. 
The user must choose the Strategy based on his possibilities, preferences.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/strategy.jpg "Credit Card")  
###### Credit Card&nbsp;(<a rel='license' href='https://creativecommons.org/licenses/by/2.0/' target='_blank'>CC BY 2.0</a>)&nbsp;by&nbsp;<a xmlns:cc='http://creativecommons.org/ns#' rel='cc:attributionURL' property='cc:attributionName' href='https://www.flickr.com/people/mecklenburg/' target='_blank'>ThomasKohler</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/strategy.png)](http://www.design-patterns-stories.com/assets/img/uml/strategy.png)

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

