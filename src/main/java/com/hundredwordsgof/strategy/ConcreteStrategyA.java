package com.hundredwordsgof.strategy;

/**
 * Implements the algorithm defined in Strategy interface.
 *
 */
public class ConcreteStrategyA implements Strategy {

  public String algorithmInterface() {
    return "Go to airport with ConcreteStrategyA, take a taxi";
  }
}
