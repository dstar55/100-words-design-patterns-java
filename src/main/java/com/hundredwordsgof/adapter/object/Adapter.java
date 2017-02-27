package com.hundredwordsgof.adapter.object;

/**
 * 
 * Adapter class, adapts Adaptee to the Target interface
 *
 */
public class Adapter implements Target {

  private Adaptee adaptee;

  public Adapter(Adaptee adaptee) {
    this.adaptee = adaptee;
  }

  public String request() {
    return adaptee.specialRequest();
  }
}
