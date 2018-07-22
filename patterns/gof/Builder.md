---
layout: page
title: Builder
permalink: /patterns/Builder/
tag: pattern
---

* [Motivation](#Motivation)
* [Story](#Story)
* [Image](#Image)
* [UML](#UML)
* [Structure](#Structure)
* [Implementation](#Implementation)
* [Usage](#Usage)


###  <a id="Motivation"></a>Motivation 

The Builder, as the name suggests, builds complex objects from simple ones, step-by-step.


Let’s say we order a child meal at a fast food restaurant. What is it comprised of? Well, a burger, a cold drink, fries and a toy. 
In fact, a child meal consist of a main item, a side item, a drink and a toy.


Every time a child meal is ordered, the service boy will take a burger, fries, a cold drink and a toy. 
Now suppose that there are 3 types of burgers available – Cheese, Beef and Chicken, 2 types of cold drinks available – Cola and 
Orange, and 2 types of toys available – a car and a doll.


So, the order might be a combination of one of these, but the process of building a child meal will be the same. 
One burger, one cold drink, fries and one toy. All these items are placed in a paper bag, which is given to the customer. 
The process of producing a child meal is an example of the Builder pattern.


The Builder pattern separates construction of a complex object from its representation, so that the same construction process can create different representations.





###  <a id="Story"></a>Story 

This pattern is used by PC shops to construct PCs. 
PC is a combination of various parts, such as a CPU, a motherboard, memory, storage, power supply, video card, etc. 
To build a PC, the same construction process is used, even if we have different variations for each part. 
Whether a customer picks a classical hard disk or SSD for storage, the construction process is the same.





###  <a id="Image"></a>Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/builder.jpg "The Antec P180, a popular computer case, suitable for use as a silent PC")  
###### The Antec P180, By DonES (Own work) [<a href="http://www.gnu.org/copyleft/fdl.html">GFDL</a> or <a href="http://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA-3.0</a>], <a href="https://commons.wikimedia.org/wiki/File%3ASilent_PC-Antec_P180.JPG">via Wikimedia Commons</a>



###  <a id="UML"></a>UML
[![](http://www.design-patterns-stories.com/assets/img/uml/builder.png)](http://www.design-patterns-stories.com/assets/img/uml/builder.png)



###  <a id="Structure"></a>Structure 

The Product class represents a complex object. 
The Builder specifies an abstract interface for creating parts of a Product object.  
The ConcreteBuilder class constructs and assembles parts of the product, implementing the Builder interface.   
The Director class constructs an object using the Builder interface.

  


###  <a id="Implementation"></a>Implementation 

#### *Builder.java* 
```java 
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
```

#### *ConcreteBuilder.java* 
```java 
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
```

#### *Product.java* 
```java 
package com.hundredwordsgof.builder;

/**
 * Product class, represents complex object
 */
public class Product {

  private String part1;

  private String part2;

  public void setPart1(String part1) {
    this.part1 = part1;
  }

  public void setPart2(String part2) {
    this.part2 = part2;
  }

  public String getPart1() {
    return part1;
  }

  public String getPart2() {
    return part2;
  }
}
```

#### *Director.java* 
```java 
package com.hundredwordsgof.builder;

/**
 * 
 * Director class, constructs an object using the Builder interface
 *
 */
public class Director {

  private Builder builder;

  public Director(Builder builder) {
    this.builder = builder;
  }

  public void construct() {
    builder.createProduct().buildPart1("part1").buildPart2("part2");
  }
}
```

###  <a id="Usage"></a>Usage 

#### *BuilderTest.java* 
```java 
package com.hundredwordsgof.builder;

import static org.junit.Assert.*;
import org.junit.Test;

/**
 * Test implementation of the Builder pattern.
 */
public class BuilderTest {

  @Test
  public void testBuilder() {

    // creates object of type ConcreteBuilder
    ConcreteBuilder builder = new ConcreteBuilder();
    // creates object of type Director
    Director director = new Director(builder);
    // Director constructs a Product
    director.construct();
    // get Product from builder
    Product product = builder.getResult();

    assertEquals(product.getPart1(), "part1");
    assertEquals(product.getPart2(), "part2");
  }
}
```

