package com.hundredwordsgof.flyweight;

/**
 * 
 * ConcreteFlyweight,implements Flyweight, and add storage for intrisnic state.
 * Adding a comment to (try) to kick off a build on Travis CI
 *
 */
public class ConcreteFlyweight implements Flyweight {

  private Object intrinsicState;

  public ConcreteFlyweight(Object intrinsicState) {
    this.intrinsicState = intrinsicState;
  }

  // Using extrinsicState as context and does NOT modify intrinsic state.
  public void operation(Object extrinsicState) {
  }

  /**
   * @return intrinsic state
   */
  public Object getIntrinsicState() {
    return intrinsicState;
  }
}
