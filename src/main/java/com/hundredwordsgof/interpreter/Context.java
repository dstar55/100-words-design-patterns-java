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
