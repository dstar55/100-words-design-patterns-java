package com.hundredwordsgof.prototype;

/**
 * Declares interface to copy it self.
 */
public abstract class Prototype implements Cloneable {

  /**
   * Copy method.
   * 
   * @return copy of the object
   * @throws CloneNotSupportedException
   *           exception
   */
  abstract Prototype copyMe() throws CloneNotSupportedException;

}
