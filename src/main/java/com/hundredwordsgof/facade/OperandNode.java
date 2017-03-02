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
