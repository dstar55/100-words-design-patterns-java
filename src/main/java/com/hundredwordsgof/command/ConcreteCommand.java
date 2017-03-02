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
