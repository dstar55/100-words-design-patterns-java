package com.hundredwordsgof.builder;

/**
 * ConcreteBuilder class, constructs and assembles parts of the Product by
 * implementing the Builder interface
 */
public class ConcreteBuilder extends Builder {

  private Product product;

  public Builder createProduct() {
    this.product = new Product();
    return this;
  }

  public Builder buildPart1(String part) {
    product.setPart1(part);
    return this;
  }

  public Builder buildPart2(String part) {
    product.setPart2(part);
    return this;
  }

  public Product getResult() {
    return product;
  }
}
