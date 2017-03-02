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
