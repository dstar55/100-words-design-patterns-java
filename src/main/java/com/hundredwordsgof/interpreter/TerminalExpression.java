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
