---
layout: page
title: Interpreter
permalink: /patterns/Interpreter/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

A person who translates orally from one language into another.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/interpreter.jpg "Polish Sign Language - letter C")  
######  Polish Sign Language - letter C, By Tomt87 (Own work) [CC BY-SA 4.0 (http://creativecommons.org/licenses/by-sa/4.0)], via Wikimedia Commons




###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/interpreter.png)](http://www.design-patterns-stories.com/assets/img/uml/interpreter.png)

###  <a id="Implementation"></a>Implementation 

#### *AbstractExpression.java* 
```java 
package com.hundredwordsgof.interpreter;

/**
 * 
 * AbstractExpresion defines interface for interpretation. Interface must be
 * used by TerminalEpression and NonTerminalEpression.
 *
 */
public abstract class AbstractExpression {

  abstract void interpret(Context context);

}
```

#### *AndExpression.java* 
```java 
package com.hundredwordsgof.interpreter;

import java.util.List;

/**
 * 
 * AndExpression implements AbstractExpression for logical AND grammar
 * expression.
 *
 */
public class AndExpression extends AbstractExpression {

  private AbstractExpression firstAbstractExpression;
  private AbstractExpression secondAbstractExpression;

  public AndExpression(AbstractExpression firstAbstractExpression,
      AbstractExpression secondAbstractExpression) {
    this.firstAbstractExpression = firstAbstractExpression;
    this.secondAbstractExpression = secondAbstractExpression;
  }

  public void interpret(Context context) {

    firstAbstractExpression.interpret(context);
    secondAbstractExpression.interpret(context);

    List<Boolean> operands = context.getOperands();

    Boolean firstOperand = operands.get(0);
    Boolean secondOperand = operands.get(1);

    Boolean result = firstOperand && secondOperand;
    context.setResult(result);

  }
}
```

#### *OrExpression.java* 
```java 
package com.hundredwordsgof.interpreter;

import java.util.List;

/**
 * 
 * OrExpression implements AbstractExpression for logical OR grammar expression.
 *
 */
public class OrExpression extends AbstractExpression {

  private AbstractExpression firstAbstractExpression;
  private AbstractExpression secondAbstractExpression;

  public OrExpression(AbstractExpression firstAbstractExpression,
      AbstractExpression secondAbstractExpression) {
    this.firstAbstractExpression = firstAbstractExpression;
    this.secondAbstractExpression = secondAbstractExpression;
  }

  public void interpret(Context context) {

    firstAbstractExpression.interpret(context);
    secondAbstractExpression.interpret(context);

    List<Boolean> operands = context.getOperands();

    Boolean firstOperand = operands.get(0);
    Boolean secondOperand = operands.get(1);

    Boolean result = firstOperand || secondOperand;
    context.setResult(result);
  }
}
```

#### *TerminalExpression.java* 
```java 
package com.hundredwordsgof.interpreter;

/**
 * 
 * TerminalExpresion implements AbstractExpression for literal symbol in
 * grammar.
 *
 */
public class TerminalExpression extends AbstractExpression {

  private boolean data;

  public TerminalExpression(boolean data) {
    this.data = data;
  }

  public void interpret(Context context) {
    // add operand to context
    context.addOperand(this.data);
  }
}
```

#### *Context.java* 
```java 
package com.hundredwordsgof.interpreter;

import java.util.ArrayList;
import java.util.List;

/**
 * 
 * Context contains global informations for Interpreter.
 *
 */
public class Context {

  // holds a list of operands which are in fact TerminalExpressions
  private List<Boolean> operands = new ArrayList<Boolean>();

  // holds result of expression
  private Boolean result = null;

  public List<Boolean> getOperands() {
    return operands;
  }

  public void addOperand(Boolean operand) {
    operands.add(operand);
  }

  public boolean isResult() {
    return result;
  }

  public void setResult(Boolean result) {
    this.result = result;
  }
}
```

###  <a id="Usage"></a>Usage 

#### *InterpreterTest.java* 
```java 
package com.hundredwordsgof.interpreter;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test implementation of the Interpreter pattern.
 */
public class InterpreterTest {

  @Test
  public void testAnd1Expression() throws Exception {

    Context context = new Context();

    // interpret false & false expression
    TerminalExpression firstTerminalExpression = new TerminalExpression(false);
    TerminalExpression secondTerminalExpression = new TerminalExpression(false);

    AndExpression andExpression = new AndExpression(firstTerminalExpression,
        secondTerminalExpression);

    andExpression.interpret(context);

    // expected result, false
    assertEquals(false, context.isResult());
  }

  @Test
  public void testAnd2Expression() throws Exception {

    Context context = new Context();

    // interpret false & true expression
    TerminalExpression firstTerminalExpression = new TerminalExpression(false);
    TerminalExpression secondTerminalExpression = new TerminalExpression(true);

    AndExpression andExpression = new AndExpression(firstTerminalExpression,
        secondTerminalExpression);

    andExpression.interpret(context);

    // expected result, false
    assertEquals(false, context.isResult());
  }

  @Test
  public void testAnd3Expression() throws Exception {

    Context context = new Context();

    // interpret true & false expression
    TerminalExpression firstTerminalExpression = new TerminalExpression(true);
    TerminalExpression secondTerminalExpression = new TerminalExpression(false);

    AndExpression andExpression = new AndExpression(firstTerminalExpression,
        secondTerminalExpression);

    andExpression.interpret(context);

    // expected result, false
    assertEquals(false, context.isResult());
  }

  @Test
  public void testAnd4Expression() throws Exception {

    Context context = new Context();

    // interpret true & true expression
    TerminalExpression firstTerminalExpression = new TerminalExpression(true);
    TerminalExpression secondTerminalExpression = new TerminalExpression(true);

    AndExpression andExpression = new AndExpression(firstTerminalExpression,
        secondTerminalExpression);

    andExpression.interpret(context);

    // expected result, true
    assertEquals(true, context.isResult());
  }

  @Test
  public void testOr1Expression() throws Exception {

    Context context = new Context();

    // interpret false & false expression
    TerminalExpression firstTerminalExpression = new TerminalExpression(false);
    TerminalExpression secondTerminalExpression = new TerminalExpression(false);

    OrExpression orExpression = new OrExpression(firstTerminalExpression,
        secondTerminalExpression);

    orExpression.interpret(context);

    // expected result, false
    assertEquals(false, context.isResult());
  }

  @Test
  public void testOr2Expression() throws Exception {

    Context context = new Context();

    // interpret false & true expression
    TerminalExpression firstTerminalExpression = new TerminalExpression(false);
    TerminalExpression secondTerminalExpression = new TerminalExpression(true);

    OrExpression orExpression = new OrExpression(firstTerminalExpression,
        secondTerminalExpression);

    orExpression.interpret(context);

    // expected result, true
    assertEquals(true, context.isResult());
  }

  @Test
  public void testOr3Expression() throws Exception {

    Context context = new Context();

    // interpret true & false expression
    TerminalExpression firstTerminalExpression = new TerminalExpression(true);
    TerminalExpression secondTerminalExpression = new TerminalExpression(false);

    OrExpression orExpression = new OrExpression(firstTerminalExpression,
        secondTerminalExpression);

    orExpression.interpret(context);

    // expected result, false
    assertEquals(true, context.isResult());
  }

  @Test
  public void testOr4Expression() throws Exception {

    Context context = new Context();

    // interpret true & true expression
    TerminalExpression firstTerminalExpression = new TerminalExpression(true);
    TerminalExpression secondTerminalExpression = new TerminalExpression(true);

    OrExpression orExpression = new OrExpression(firstTerminalExpression,
        secondTerminalExpression);

    orExpression.interpret(context);

    // expected result, true
    assertEquals(true, context.isResult());
  }
}
```

