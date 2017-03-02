package com.hundredwordsgof.command;

/**
 * 
 * Invoker class, asks the command to carry out the request
 *
 */
public class Invoker {

  private Command command;

  public Invoker(Command command) {
    this.command = command;
  }

  public void execute() {
    command.execute();
  }
}
