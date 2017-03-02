package com.hundredwordsgof.singleton;

/**
 * Singleton class implements singleton pattern. Only one object can be
 * instantiated.
 * 
 */
public class Singleton {

  /**
   * Holds reference to single instance.
   */
  private static Singleton INSTANCE;

  /**
   * Overrides public Constructor.
   */
  private Singleton() {
  }

  /**
   * Creates the instance if it does not yet exist(lazy instantiation).
   * 
   * @return a reference to the single instance.
   */
  public static Singleton getInstance() {
    if (INSTANCE == null) {
      INSTANCE = new Singleton();
    }
    return INSTANCE;
  }
}
