---
layout: page
title: Facade
permalink: /patterns/Facade/
tag: pattern
---

* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Story"></a>Story 

Facade hides the complexity of the system and provides an interface to the client from where the client can access the system.

You want to organize a marriage reception with dinner for 100 people. 
So in order to organize such event, you need to find and decorate a hall where the event will happen, 
then you need to find a music, organize flowers, send invitations and so on and so on.

If this is to much for you than you can find event manager which will organize event for you. 

This is a typical example for Facade. 





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/facade.jpg "Wedding Event Management")  
###### By WeMaxx1248 (Own work) [<a href="http://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a>], <a href="https://commons.wikimedia.org/wiki/File%3AEvent_management_in_pune.jpg">via Wikimedia Commons</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/facade.png)](http://www.design-patterns-stories.com/assets/img/uml/facade.png)

###  <a id="Implementation"></a>Implementation 

#### *Compiler.java* 
```java 
package com.hundredwordsgof.facade;

import java.util.List;

/**
 * 
 * Compiler has subclasses like Tokenizer, Parser, Generator, etc. Client which
 * use a compiler do not deal with subclasses in order to compile. Compiler
 * class represents a facade. Facade hides low-level functionality from client.
 *
 */
public class Compiler {

  public static int compile(String input) throws Exception {

    Parser parser = new Parser();
    List<String> tokens = Tokenizer.tokenize(input);
    Node expression = parser.parse(tokens);
    int result = Generator.generate(expression);

    return result;
  }
}
```

#### *Tokenizer.java* 
```java 
package com.hundredwordsgof.facade;

import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/**
 * Tokenizer, tokenize input string into tokens.
 *
 */
public class Tokenizer {

  public static List<String> tokenize(String source) {

    ArrayList<String> tokens = new ArrayList<String>();

    StringTokenizer stringTokenizer = new StringTokenizer(source);
    while (stringTokenizer.hasMoreElements()) {
      tokens.add((String) stringTokenizer.nextElement());
    }
    return tokens;
  }
}
```

#### *Generator.java* 
```java 
package com.hundredwordsgof.facade;

/**
 *
 * Generator, supposed to generate binary code, but in this case acts as a
 * calculator which adds two numbers.
 *
 */
public class Generator {

  public static int generate(Node expression) throws Exception {

    // TODO check expression
    if (expression instanceof ExpressionNode) {
      ExpressionNode expressionNode = (ExpressionNode) expression;

      OperandNode rightOperandNode = (OperandNode) expressionNode.getRight();
      OperandNode leftOperandNode = (OperandNode) expressionNode.getLeft();

      int result = rightOperandNode.getValue() + leftOperandNode.getValue();

      return result;

    } else {
      throw new Exception("Error in generator");
    }
  }
}
```

#### *Node.java* 
```java 
package com.hundredwordsgof.facade;

/**
 * Node, represents Node in Abstract Syntax Tree.
 *
 */
public class Node {
	 
}
```

#### *ExpressionNode.java* 
```java 
package com.hundredwordsgof.facade;

/**
 * ExpressionNode, represents ExpressionNode in Abstract Syntax Tree.
 *
 */
public class ExpressionNode extends Node {

  private char operator;
  private Node left;
  private Node right;

  public char getOperator() {
    return operator;
  }

  public void setOperator(char operator) {
    this.operator = operator;
  }

  public Node getLeft() {
    return left;
  }

  public void setLeft(Node left) {
    this.left = left;
  }

  public Node getRight() {
    return right;
  }

  public void setRight(Node right) {
    this.right = right;
  }
}
```

#### *OperandNode.java* 
```java 
package com.hundredwordsgof.facade;

/**
 * OperandNode, represents OperandNode in Abstract Syntax Tree.
 *
 */
public class OperandNode extends Node {

  private int value;

  public int getValue() {
    return value;
  }

  public void setValue(int value) {
    this.value = value;
  }
}
```

#### *Parser.java* 
```java 
package com.hundredwordsgof.facade;

import java.util.List;
import java.util.Stack;

/**
 * 
 * Parser parses simple expression which adds two numbers, for example: 1 + 2
 * Note: due to scope error handling is not implemented.
 *
 */
public class Parser {

  private Stack<String> expressionStack = new Stack<String>();
  private Stack<String> operandStack = new Stack<String>();

  public Node parse(List<String> tokens) {

    for (String token : tokens) {
      if (isTokenExpression(token)) {
        expressionStack.push(token);
      } else if (isTokenOperand(token)) {
        operandStack.push(token);
      }
    }

    ExpressionNode expressionNode = new ExpressionNode();

    // create Abstract Syntax Tree
    while (!expressionStack.empty()) {

      String expression = (String) expressionStack.pop();
      expressionNode.setOperator(expression.charAt(0));

      String rightOperand = (String) operandStack.pop();
      OperandNode rightOperandNode = new OperandNode();
      rightOperandNode.setValue(Integer.parseInt(rightOperand));

      String leftOperand = (String) operandStack.pop();
      OperandNode leftOperandNode = new OperandNode();
      leftOperandNode.setValue(Integer.parseInt(leftOperand));

      expressionNode.setRight(rightOperandNode);
      expressionNode.setLeft(leftOperandNode);

    }

    return expressionNode;
  }

  private boolean isTokenExpression(String token) {

    if (token.equals("+")) {
      return true;
    }
    return false;
  }

  // operand is supposed to be number
  private boolean isTokenOperand(String token) {
    for (char c : token.toCharArray()) {
      if (!Character.isDigit(c))
        return false;
    }
    return true;
  }
}
```

###  <a id="Usage"></a>Usage 

#### *FacadeTest.java* 
```java 
package com.hundredwordsgof.facade;

import static org.junit.Assert.*;
import org.junit.Test;

/**
 * Test implementation of the Facade pattern.
 */
public class FacadeTest {

  @Test
  public void testFacade() throws Exception {

    // Compiler class is a facade, it can add two numbers with following
    // expression: 1 + 2
    // all other operations are not supported
    assertEquals(3, Compiler.compile("1 + 2"));

    try {
      // right operand is not a number
      Compiler.compile("1 + x");
      fail("Exception must be thrown");
    } catch (Exception e) {
    }

    try {
      // - expression is not supported
      Compiler.compile("1 - 1");
      fail("Exception must be thrown");
    } catch (Exception e) {
    }
  }
}
```

