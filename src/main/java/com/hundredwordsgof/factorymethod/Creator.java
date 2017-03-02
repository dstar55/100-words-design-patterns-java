package com.hundredwordsgof.factorymethod;

/**
 * Creator class declares factory method
 */
abstract class Creator {

  abstract Product factoryMethod(String type);
}
