---
layout: page
title: Abstract Factory
permalink: /AbstractFactory/
tag: pattern
---



### Story 

Provides an interface for creating families of related objects, without specifying concrete classes. 

This pattern is found in the cards stamping equipment used in the 
manufacture in order to produce playing cards. 
Cards stamping machine is an Abstract Factory which produces a cards. 
The same machine is used to stamp French, Italian or German cards. 




### UML 
![]({{site.baseurl}}/assets/img/abstractfactory.png)

#### *AbstractFactory.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * Abstract Factory, defines interface for creation of the abstract product objects
 *
 */
public interface AbstractFactory {

	AbstractProductA createProductA();
	
	AbstractProductB createProductB();
	
}
```

#### *AbstractProductA.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * AbstractProductA, define interface for ProductA objects
 *
 */
abstract class AbstractProductA {

}
```

#### *AbstractProductB.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * AbstractProductB, define interface for ProductB objects
 *
 */
abstract class AbstractProductB {

}
```

#### *ConcreteFactory1.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * ConcreteFactory1, implements creation of the concrete Product1 objects
 *
 */
public class ConcreteFactory1 implements AbstractFactory {

	
	public AbstractProductA createProductA() {
		return new ProductA1();
	}

	
	public AbstractProductB createProductB() {
		return new ProductB1();
	}

}
```

#### *ConcreteFactory2.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * ConcreteFactory2, implements creation of the concrete Product2 objects
 *
 */
public class ConcreteFactory2 implements AbstractFactory {

	
	public AbstractProductA createProductA() {
		return new ProductA2();
	}

	
	public AbstractProductB createProductB() {
		return new ProductB2();
	}

}
```

#### *ProductA1.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * ProductA1, implements AbstractProductA interface
 *
 */
public class ProductA1 extends AbstractProductA {

}
```

#### *ProductA2.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * ProductA2, implements AbstractProductA interface
 *
 */
public class ProductA2 extends AbstractProductA {

}
```

#### *ProductB1.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * ProductB1, implements AbstractProductB interface
 *
 */
public class ProductB1 extends AbstractProductB {

}
```

#### *ProductB2.java* 
```java 
package com.hundredwordsgof.abstractfactory;

/**
 * 
 * ProductB2, implements AbstractProductB interface
 *
 */
public class ProductB2 extends AbstractProductB {

}
```

