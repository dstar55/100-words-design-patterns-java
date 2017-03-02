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
