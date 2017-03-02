package com.hundredwordsgof.builder;

/**
 * Builder, declares interface for creating parts of a Product object
 * 
 */
abstract class Builder {

  public abstract Builder createProduct();

  public abstract Builder buildPart1(String part);

  public abstract Builder buildPart2(String part);
}
