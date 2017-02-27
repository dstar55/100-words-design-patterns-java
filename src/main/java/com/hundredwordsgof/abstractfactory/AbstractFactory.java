package com.hundredwordsgof.abstractfactory;

/**
 * 
 * Abstract Factory, defines interface for creation of the abstract product
 * objects
 * 
 */
public interface AbstractFactory {

  AbstractProductA createProductA();

  AbstractProductB createProductB();
}
