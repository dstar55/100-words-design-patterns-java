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
