package com.hundredwordsgof.decorator;

/**
 * 
 * Decorator, keep reference to Component object
 *
 */
abstract class Decorator implements Component {

  protected Component component;

  public abstract void operation();

  public void setComponent(Component component) {
    this.component = component;
  }
}
