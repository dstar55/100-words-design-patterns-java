---
layout: page
title: Command
permalink: /patterns/Command/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Issue requests to objects without knowing anything about the operation being requested or the receiver of the request.

When your car needs service you visit Car Service Center. On reception you explain a problem and you leave a car.
The person at reception encapsulates the problem in to order for Car Technician. The order is queued internaly.
Car Technician will receive a request and fix a problem.



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/command.png)](http://www.design-patterns-stories.com/assets/img/uml/command.png)

###  <a id="Implementation"></a>Implementation 

#### *Command.java* 
```java 
package com.hundredwordsgof.command;

/**
 * 
 * Command interface, declares an interface for executing an operation
 *
 */
public interface Command {

  void execute();
}
```

#### *ConcreteCommand.java* 
```java 
package com.hundredwordsgof.command;

/**
 * 
 * ConcreteCommand class, defines a binding between a Receiver object and an
 * operation
 *
 */
public class ConcreteCommand implements Command {

  private Receiver receiver;

  public ConcreteCommand(Receiver receiver) {
    this.receiver = receiver;
  }

  public void execute() {
    this.receiver.action();
  }
}
```

#### *Receiver.java* 
```java 
package com.hundredwordsgof.command;

/**
 * 
 * Receiver class, knows how to perform the operations associated with carrying
 * out a request
 *
 */
public class Receiver {

  private boolean operationPerfomed = false;

  public void action() {
    operationPerfomed = true;
  }

  protected boolean isOperationPerfomed() {
    return operationPerfomed;
  }
}
```

#### *Invoker.java* 
```java 
package com.hundredwordsgof.command;

/**
 * 
 * Invoker class, asks the command to carry out the request
 *
 */
public class Invoker {

  private Command command;

  public Invoker(Command command) {
    this.command = command;
  }

  public void execute() {
    command.execute();
  }
}
```

###  <a id="Usage"></a>Usage 

#### *CommandTest.java* 
```java 
package com.hundredwordsgof.command;

import static org.junit.Assert.*;
import org.junit.Test;

/**
 * Test implementation of the Test pattern.
 */
public class CommandTest {

  @Test
  public void testCommand() {

    Receiver receiver = new Receiver();
    Command command = new ConcreteCommand(receiver);
    Invoker invoker = new Invoker(command);

    // operation on receiver is not performed
    assertEquals(false, receiver.isOperationPerfomed());

    // this will invoke method action on receiver
    invoker.execute();

    // operation on receiver is performed
    assertEquals(true, receiver.isOperationPerfomed());
  }
}
```

