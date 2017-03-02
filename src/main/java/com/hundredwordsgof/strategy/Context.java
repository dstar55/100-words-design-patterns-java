package com.hundredwordsgof.strategy;

/**
 * Maintains a reference to a Strategy object. Invokes algorithm implemented in
 * ConcreteStrategy.
 *
 */
public class Context {

  private Strategy strategy;

  public Context(Strategy strategy) {
    this.strategy = strategy;
  }

  protected String contextInterface() {
    return this.strategy.algorithmInterface();
  }
}
