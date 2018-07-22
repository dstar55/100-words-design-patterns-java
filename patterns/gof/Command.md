---
layout: page
title: Command
permalink: /patterns/Command/
tag: pattern
---

* [Motivation](#Motivation)
* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Motivation"></a>Motivation 

Imagine that we are developing a graphical editor. The user can add new text, delete or update existing text.

What to do in a case when user does something wrong? The user should be able to return back to the state of the text before the wrong action has 
been executed.


How to implement such behavior?


One solution would be to hold a list of the text states. 
If the text is long and if we store a lot of states of such a long text, we can run out of memory, 
so this solution is not appropriate for our particular scenario.


What if we consider an idea where the current state of text is a result of execution of a sequence of operations? 
These operations can be undone, with the effect that the text reverts to a previous state. 
The operations that have been undone become redoable, so that later model states can be reached again if necessary. 
So, we will no longer invoke operations on the text directly, but we will create Command objects, which invoke the operations. 
Each text operation will have the appropriate Command object.

This solution is a Command pattern. 
The Command pattern issues requests to objects without knowing anything about the operation being requested or about the receiver of the request.





###  <a id="Story"></a>Story 

When your car needs servicing, you visit a Car Service Center. Upon arrival, you explain the problem and you leave the car. 
The person at reception summarizes the problem and enters it into an order for the Car Technician. 
The order is queued internally. The Car Technician will receive the request and fix the problem.



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

