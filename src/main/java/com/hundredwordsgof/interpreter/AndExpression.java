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
