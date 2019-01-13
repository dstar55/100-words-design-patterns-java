[![Build Status](https://travis-ci.org/dstar55/100-words-design-patterns-java.svg?branch=master)](https://travis-ci.org/dstar55)
[![Coverage Status](https://coveralls.io/repos/github/dstar55/100-words-design-patterns-java/badge.svg?branch=master)](https://coveralls.io/github/dstar55/100-words-design-patterns-java?branch=master) 
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9814c4f9d59b4a6fa12ff122d6331b0a)](https://www.codacy.com/app/dstar55/100-words-design-patterns-java?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dstar55/100-words-design-patterns-java&amp;utm_campaign=Badge_Grade)
[![GitPitch](https://gitpitch.com/assets/badge.svg)](https://gitpitch.com/dstar55/100-words-design-patterns-java/master?grs=github&t=white)
[![License](http://img.shields.io/:license-mit-blue.svg)](http://gus.mit-license.org/)

Official Website: [Design Patterns Stories ](http://www.design-patterns-stories.com)

# 100 words GoF Design Patterns in Java

## Introduction

Idea: describe GoF Design Patterns on a simple way. 
Each pattern will be described with following structure:
* Story(less than 100 words)
* Implementation in Java

### GoF Design Patterns

#### Creational Patterns
* [Singleton](#Singleton)
* [Prototype](#Prototype)
* [Builder](#Builder)
* [Factory Method](#FactoryMethod)
* [Abstract Factory](#AbstractFactory)

#### Structural Patterns
* [Adapter](#Adapter)
* [Bridge](#Bridge)
* [Composite](#Composite)
* [Decorator](#Decorator)
* [Facade](#Facade)
* [Flyweight](#Flyweight)
* [Proxy](#Proxy)

#### Behavioral Patterns
* [Chain Of Responsibility](#ChainOfResponsibility)
* [Command](#Command)
* [Interpreter](#Interpreter)
* [Iterator](#Iterator)
* [Mediator](#Mediator)
* [Memento](#Memento)
* [Observer](#Observer)
* [State](#State)
* [Strategy](#Strategy)
* [Template Method](#TemplateMethod)
* [Visitor](#Visitor)

##### <a id="Singleton"></a>Singleton

* Motivation

Objects reside inside heap memory, and we can instantiate as many objects as the physical space in the heap memory will allow. 
But, in some cases, we can have a situation when only one instance of a class can be instantiated.
So, imagine that we are developing a program which is playing audio files. Inside that program, we need to have a class which handles audio output. 
A computer usually has one audio output, so no more than one sound can be played at a time. 
Therefore, a class that handles the computer audio device should have exactly one instance.

How can we ensure that only one instance is created?
Each java class has default public constructor, which can be invoked from any part of the code.
If we implement a class where default constructor has scope 'private', 
then only the methods from that class can invoke that constructor, meaning that we can't instantiate that class from other classes. 
This is a basis of the Singleton pattern.

The Singleton ensures that only one (single) object can be created from the class.


* Story

Men's 100 meters world record holder is a singleton. 
There can be only one active "Men's 100 meters world record holder" at any given time. 
Regardless of the actual person who holds this title, "Men's 100 meters world record holder" is a global point of access that 
identifies the fastest person in the world.

* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/singleton.jpg "Usain Bolt, Men's 100 meters world record holder")  
###### Brick Lane Graffiti Usain Bolt&nbsp;(<a rel='license' href='https://creativecommons.org/licenses/by/2.0/' target='_blank'>CC BY 2.0</a>)&nbsp;by&nbsp;<a xmlns:cc='http://creativecommons.org/ns#' rel='cc:attributionURL' property='cc:attributionName' href='https://www.flickr.com/people/mdpettitt/' target='_blank'>Martin Pettitt</a>

* Implementation


UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/singleton.png "UML Singleton")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to singleton folder:

```
$  cd /src/main/java/com/hundredwordsgof/singleton
```

* Structure

The fact that every class has a public constructor in Java can be used in order to implement a *Singleton*. 
The public constructor will be overridden with a new constructor which does nothing, but the scope of the constructor is private, 
so other classes can't instantiate class objects.


The object is created in the method *getInstance()*, and since an object is created when method *getInstance()* is invoked for first time, 
we are talking about lazy instantiation technique.


This technique ensures that singleton instances are created only when needed.


This implementation may have issues in multi-threaded environment, but in such situation we have to synchronize method getInstance(), 
or put that method inside synchronize block.

In addition to lazy initialization technique, we can have eager initialization technique, where instance is created during class loading.
Eager initialization can be implemented using variable static initialization or static block where exception can be handled.


* Known uses

  * [java.lang.Runtime#getRuntime()](https://docs.oracle.com/javase/8/docs/api/java/lang/Runtime.html#getRuntime--)
  * [java.awt.Desktop#getDesktop()](https://docs.oracle.com/javase/8/docs/api/java/awt/Desktop.html#getDesktop--)
  * [java.lang.System#getSecurityManager()](https://docs.oracle.com/javase/8/docs/api/java/lang/System.html#getSecurityManager--)


##### <a id="Prototype"></a>Prototype
* Motivation

In Singleton pattern we saw how to tackle the situation when we should instantiate a single object of a class. 
However, we may have a situation when, during runtime, we want to copy an object which already exists in memory, particularly if the object is complex.


So, imagine that we are developing software which can work with spreadsheets. A spreadsheet consist of cells, and a cell is a complex object with lot of attributes, such as borders, content, format, color, etc. Now, if we want to split a cell, we can develop a method which will copy each attribute of that object. This method can became very complex, so we should consider a more elegant solution.
It would be nice if we could copy an object with a single method, for example *cloneMe()*.

Such solution is a Prototype pattern.

* Story

The Clone itself.


Dolly the sheep was the first mammal to be cloned, so Dolly is a duplicate.


* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/prototype.jpg "Sheep Dolly")  
###### <a href="https://commons.wikimedia.org/wiki/File:Dolly_the_sheep_2016.JPG">Dolly the sheep 2016</a>, By Geni,<a href="https://creativecommons.org/licenses/by-sa/4.0/legalcode">CC BY-SA 4.0</a>

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/prototype.png "UML Prototype")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to prototype folder:

```
$  cd /src/main/java/com/hundredwordsgof/prototype
```

* Structure

The *Prototype* interface defines the *copyMe()* method.   
The *ConcretePrototype* implements a *Prototype* interface using *java.lang.Object.clone()* method.


The prototype can be used to implement a copy constructor (deep or shallow).


* Known uses

  * [java.lang.Object#clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)
  * [java.lang.Cloneable](https://docs.oracle.com/javase/7/docs/api/java/lang/Cloneable.html)


##### <a id="Builder"></a>Builder

* Motivation

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

* Story

This pattern is used by PC shops to construct PCs. 
PC is a combination of various parts, such as a CPU, a motherboard, memory, storage, power supply, video card, etc. 
To build a PC, the same construction process is used, even if we have different variations for each part. 
Whether a customer picks a classical hard disk or SSD for storage, the construction process is the same.

* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/builder.jpg "The Antec P180, a popular computer case, suitable for use as a silent PC")  
###### The Antec P180, By DonES (Own work) [<a href="http://www.gnu.org/copyleft/fdl.html">GFDL</a> or <a href="http://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA-3.0</a>], <a href="https://commons.wikimedia.org/wiki/File%3ASilent_PC-Antec_P180.JPG">via Wikimedia Commons</a>

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/builder.png "UML Prototype")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to builder folder:

```
$  cd /src/main/java/com/hundredwordsgof/builder
```

* Structure

The *Product* class represents a complex object.   
The *Builder* specifies an abstract interface for creating parts of a *Product* object.     
The *ConcreteBuilder* class constructs and assembles parts of the product, implementing the *Builder* interface.    
The *Director* class constructs an object using the *Builder* interface.

  
* Known uses

  * [java.lang.StringBuilder.append()](https://docs.oracle.com/javase/8/docs/api/java/lang/StringBuilder.html#append-boolean-)
  * [java.lang.StringBuffer.append()](https://docs.oracle.com/javase/8/docs/api/java/lang/StringBuffer.html#append-boolean-)
  * [java.lang.Appendable](https://docs.oracle.com/javase/8/docs/api/java/lang/Appendable.html)
  * [javax.swing.GroupLayout.group.addComponent()](https://docs.oracle.com/javase/8/docs/api/javax/swing/GroupLayout.Group.html#addComponent-java.awt.Component-)
  * [java.nio.ByteBuffer.put()](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html#put-byte-)
  * [java.nio.CharBuffer.put()](https://docs.oracle.com/javase/8/docs/api/java/nio/CharBuffer.html#put-byte-)
  * [java.nio.ShortBuffer.put()](https://docs.oracle.com/javase/8/docs/api/java/nio/ShortBuffer.html#put-byte-)
  * [java.nio.IntBuffer.put()](https://docs.oracle.com/javase/8/docs/api/java/nio/IntBuffer.html#put-byte-)
  * [java.nio.LongBuffer.put()](https://docs.oracle.com/javase/8/docs/api/java/nio/LongBuffer.html#put-byte-)
  * [java.nio.FloatBuffer.put()](https://docs.oracle.com/javase/8/docs/api/java/nio/FloatBuffer.html#put-byte-)
  * [java.nio.DoubleBuffer.put()](https://docs.oracle.com/javase/8/docs/api/java/nio/DoubleBuffer.html#put-byte-)
  


##### <a id="FactoryMethod"></a>Factory Method

* Motivation

Imagine that we need to develop a reporting library. 
Two basic abstractions in this library are the Engine and the Report classes. 
Both classes are abstract, and clients have to extend them in order to realize their application specific implementations.


The Engine class is responsible for managing Reports and will create them as required. 
Report subclasses which Engine should instantiate are application specific and Engine only knows when a new report should be created, 
but not what type of Report to create. 
This leads us to a situation in which our library should instantiate classes, but it only knows about abstract classes, which it cannot instantiate.


So, how can we solve this?


If we encapsulate the knowledge of which Report subclasses to create and move this knowledge outside of the library, then 
Engine subclass will be able to create Report objects. This solution is the Factory Method pattern.


The Factory Method defines an interface for creating objects, but lets subclasses decide which class to instantiate.


* Story

Plasticine is used as a toy for children. Plasticine is injected into predefined molds. 
The class of end product (ball, toy, sculpture, cake) is determined by the mold.


* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/factorymethod.jpg "Cake molds, Han people, metal - Museum of Vietnamese History - Ho Chi Minh City")  
###### Cake molds, Han people, metal - Museum of Vietnamese History - Ho Chi Minh City, By Daderot (Own work) [<a href="http://creativecommons.org/publicdomain/zero/1.0/deed.en">CC0</a>], <a href="https://commons.wikimedia.org/wiki/File%3ACake_molds%2C_Han_people%2C_metal_-_Museum_of_Vietnamese_History_-_Ho_Chi_Minh_City_-_DSC05796.JPG">via Wikimedia Commons</a>

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/factorymethod.png "UML Factory Method")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to factorymethod folder:

```
$  cd /src/main/java/com/hundredwordsgof/factorymethod
```

* Structure

The *Product* interface defines the interface of objects the factory method creates.    
The *ConcreteProduct* class implements the *Product* interface.   
The *Creator* abstract class declares the factory method interface.   
The *ConcreteCreator* class implements the *Creator's* factory method and returns an instance of the *ConcreteProduct*.  


* Known uses

  * [java.util.Calendar#getInstance()](https://docs.oracle.com/javase/8/docs/api/java/util/Calendar.html#getInstance--)
  * [java.util.ResourceBundle#getBundle()](https://docs.oracle.com/javase/8/docs/api/java/util/ResourceBundle.html#getBundle-java.lang.String-)
  * [java.nio.charset.Charset#forName()](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/Charset.html#forName-java.lang.String-)
  * [java.net.URLStreamHandlerFactory#createURLStreamHandler(String)](https://docs.oracle.com/javase/8/docs/api/java/net/URLStreamHandlerFactory.html)
  * [java.util.EnumSet#of()](https://docs.oracle.com/javase/8/docs/api/java/util/EnumSet.html#of(E))


##### <a id="AbstractFactory"></a>Abstract Factory

* Motivation


Imagine that we are developing a framework for a GUI environment, were windows will be drawn on a display device and the user will 
interact with the GUI using a mouse and a keyboard.

The first version of the framework will support Windows OS, so Factory method is used for creation of the graphical abstractions 
like Frame, Window, ScrollBar, etc.


In the next version, the framework will be extended to Linux OS. So, how should we extend our factory method?


One way would be to introduce factory abstraction, where each OS will have dedicated factory for creation of the graphical abstractions. 
The proposed solution is an example of the Abstract Factory.

The Abstract Factory is one level higher in abstraction than the Factory Method. 
The Factory Method abstracts the way objects are created, while the Abstract Factory also abstracts the way factories are created, 
which in turn abstracts the way objects are created.


The Abstract Factory provides an interface for creating families of related objects, without specifying concrete classes.


* Story

This pattern is found in the cards stamping equipment, used in manufacturing of playing cards. 
A card stamping machine is an Abstract Factory which produces cards. 
The same machine is used to stamp French, Italian or German cards. 

* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/abstractfactory.jpg "Poker Cards Back")  
###### Poker Cards Back&nbsp;(<a rel='license' href='https://creativecommons.org/share-your-work/public-domain/cc0/' target='_blank'>CC 0</a>)




* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/abstractfactory.png "UML Abstract Factory")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to abstractfactory folder:

```
$  cd /src/main/java/com/hundredwordsgof/abstractfactory
```

* Structure

The *AbstractFactory* defines the interface for creation of the abstract product objects.  
The *AbstractProduct* defines the interface for product objects.  
The *ConcreteProduct* class implements products based on *AbstractProduct* interfaces.   
The *ConcreteFactory* class implements factories based on *AbstractFactory* interfaces.   
The *Client* class uses *AbstractFactory* & *AbstractProduct* interfaces.  


* Known uses

  * [javax.xml.parsers.DocumentBuilderFactory#newInstance()](https://docs.oracle.com/javase/8/docs/api/javax/xml/parsers/DocumentBuilderFactory.html#newInstance--)
  * [javax.xml.transform.TransformerFactory#newInstance()](https://docs.oracle.com/javase/8/docs/api/javax/xml/transform/TransformerFactory.html#newInstance--)
  * [javax.xml.xpath.XPathFactory#newInstance()](https://docs.oracle.com/javase/8/docs/api/javax/xml/xpath/XPathFactory.html#newInstance--)

##### <a id="Adapter"></a>Adapter

* Motivation

Imagine that we need to develop a graphical editor which should be able to draw various graphical shapes like line, circle, rectangle and text. 
All of our graphical elements are subclass of the base class Shape. So, we will have LineShape, CircleShape, RectangeShape and TextShape.


The implementation of the TextShape is not easy. 
We need to implement a lot of complex functionalities, such as text buffering, text bolding, text coloring, undo, redo, 
'what you see is what you get', etc. We have found an open source text library which implements pretty much all of the text functionality 
which we are looking for.


Why not adapt an existing text library, so that we can reuse already implemented functionality for our graphical editor? 
But, in order to use the existing text library, we must adapt interfaces from the existing text library to our interfaces.


The process of adaptation of the existing interfaces is an example of the Adapter pattern.


The adapter allows us to access the interface of an existing class from another interface.


* Story

Adapters are often used in daily life, for example, an electrical adapter is a device that converts attributes of one electrical device or 
system to those of an otherwise incompatible device or system. 
Some modify power or signal attributes, while others merely adapt the physical form of one electrical connector to another.

* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/adapter.jpg "Adapter")  
###### <a href="https://commons.wikimedia.org/wiki/User:Lionel_Allorge">Lionel Allorge</a>, <a href="https://commons.wikimedia.org/wiki/File:Adaptateur_de_prise_française_en_prise_suisse_2.jpg">Adaptateur de prise française en prise suisse 2</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/legalcode">CC BY-SA 3.0</a>

* Implementation

UML: 
Class Adapter

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/classadapter.png "UML Class Adapter")

Object Adapter: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/objectadapter.png "UML Object Adapter")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to adapter folder:

```
$  cd /src/main/java/com/hundredwordsgof/adapter
```

* Structure

We can have two implementations, the *Class* adapter and the *Object* adapter.


The *Class* adapter extends the *Adaptee* class.   
The *Object* adapter injects *Adaptee* object into the *Adapter* class.


The target interface defines the domain-specific interface used by the *Client*.   
The *Client* class uses the target interface.  
The *Adaptee* class defines an existing interface where adaption will be applied.  
The *Adapter* class adapts interface *Adaptee* to the *Target*.


* Known uses

  * [java.util.Arrays#asList()](https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html#asList-T...-)
  * [java.util.Collections#list()](https://docs.oracle.com/javase/8/docs/api/java/util/Collections.html#list-java.util.Enumeration-)
  * [java.util.Collections#enumeration()](https://docs.oracle.com/javase/8/docs/api/java/util/Collections.html#enumeration-java.util.Collection-)
  * [java.io.InputStreamReader(InputStream)](https://docs.oracle.com/javase/8/docs/api/java/io/InputStreamReader.html#InputStreamReader-java.io.InputStream-)
  * [java.io.OutputStreamWriter(OutputStream)](https://docs.oracle.com/javase/8/docs/api/java/io/OutputStreamWriter.html#OutputStreamWriter-java.io.OutputStream-)
  * [javax.xml.bind.annotation.adapters.XmlAdapter#marshal()](https://docs.oracle.com/javase/8/docs/api/javax/xml/bind/annotation/adapters/XmlAdapter.html#marshal-BoundType-)
  * [javax.xml.bind.annotation.adapters.XmlAdapter#unmarshal()](https://docs.oracle.com/javase/8/docs/api/javax/xml/bind/annotation/adapters/XmlAdapter.html#unmarshal-ValueType-)

##### <a id="Bridge"></a>Bridge

* Motivation

Let's say that that we want to develop an audio player on our Windows OS. We define the base class, Audio, which has two subclasses – MP3Audio and 
WavAudio. The first version of the player on Windows is running well, but after some time we want to implement the same player on Linux OS.


How do we tackle this situation?


If we incorporate the OS specifics in our hierarchy, we will end up with 4 class combinations, such as WindowsMP3Audio, LinuxMP3Audio, 
WindowsWavAudio and LinuxWavAudio. Adding more codec types and more operating systems will make the hierarchy even larger.


The appropriate solution would be to extract our structure into two separate hierarchies.


The original audio structure classes will remain the same,  and they will contain a reference to an object of the new hierarchy, the OS hierarchy. 
This way we will extract the OS specifics into a class of its own, with two child classes, Windows and Linux. 
The Audio class will get a reference field to one of the OS classes. 
Using that reference, it will be able to delegate work to OS objects when needed. 
This reference will serve as a bridge between the Audio and OS hierarchies.


The explained solution is an example of the Bridge pattern.


The bridge pattern decouples an abstraction from its implementation, so that the two can vary independently.


* Story

A steering wheel is an example of the Bridge. 
The purpose of a steering wheel is to transmit driver's input to the steered wheels in order to dynamically change the direction of the vehicle. 
There are different implementations of steering wheels used in cars, buses, trucks, tractors and racing cars.

* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/bridge.jpg "1924 Stanley 740 Interior")  
###### 1924 Stanley 740 Interior, By Liftarn (Own work) [Public domain], <a href="https://commons.wikimedia.org/wiki/File%3A1924Stanley740-interior.jpg">via Wikimedia Commons</a>

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/bridge.png "UML Bridge")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to bridge folder:

```
$  cd /src/main/java/com/hundredwordsgof/bridge
```

* Structure

The *Implementator* interface defines the interface for implementation classes (concrete implementers).  
The *ConcreteImplementator* class implements the *Implementator* interface and defines its concrete implementation.  
The *Abstraction* abstract class defines the abstraction interface, maintains a reference to an object of type *Implementator*, 
and the link between the abstraction and the implementer is called a *Bridge*.  
The *RefinedAbstracion* extends the interface defined by *Abstraction*.


* Known uses

  * [JDBC-ODBC Bridge](https://docs.oracle.com/javase/7/docs/technotes/guides/jdbc/bridge.html)
  * [AWT](https://docs.oracle.com/javase/8/docs/technotes/guides/awt/), it provides an abstraction layer which maps onto the native OS the windowing support.

##### <a id="Composite"></a>Composite

* Motivation

Imagine that we need to develop a graphical framework which should speed up the development of business applications, 
where the user works with data using graphical forms. 
A graphical form is made up of the basic graphical elements, such as label, text, input field, button, list, etc.


In order to draw something on the screen, each graphical element should implement a common interface with the draw method. 
But, in addition to the draw interface, some graphical elements must act as containers for other graphical elements. 
So, for example, a form is a container for labels, input fields and buttons.


It seems that a tree structure can be the basis for such a graphical framework, but the problem is that we must treat a leaf node and an internal 
node the same way. This problem can be solved by using the Composite pattern.


The Composite pattern composes objects into tree structures to represent part-whole hierarchies. 
A group of objects is to be treated the same way as a single instance of an object.


* Story

Lego brick represents a Composite pattern. 
A brick is a basic object, but at the same time, a brick is a container which can hold other bricks in order to construct complex objects.

* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/composite.jpg "Lego Bricks")  
###### Lego Bricks, By Priwo (photo taken by de:Benutzer:Priwo) [Public domain], <a href="https://commons.wikimedia.org/wiki/File%3ALEGO-01.jpg">via Wikimedia Commons</a>

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/composite.png "UML Composite")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to composite folder:

```
$  cd /src/main/java/com/hundredwordsgof/composite
```

* Structure

The *Component* abstract class declares the interface for objects in the composition, implements default behavior for the interface common to 
all classes as appropriate, and declares an interface for accessing and managing its child components.  
The *Leaf* class represents leaf objects in the composition.  
The *Composite* class defines behavior for components having children, stores the child components and implements the child-related operations in the 
*Component* interface.  
The *Client* class uses the *Composite* interface.


* Known uses 

  * [java.awt.Container#add(Component)](https://docs.oracle.com/javase/8/docs/api/java/awt/Container.html#add-java.awt.Component-)
  * [javax.faces.component.UIComponent#getChildren()](https://docs.oracle.com/javaee/7/api/javax/faces/component/UIComponent.html#getChildren--)


##### <a id="Decorator"></a>Decorator

* Motivation

Suppose that we are working on a user interface toolkit and we want to be able to add borders and scroll bars to the windows. 
If we use inheritance, we will extend Window class with new classes, such as WindowVerticalScrollBar, WindowHorizontalScrollBar, WindowBorder, etc.


The solution with the inheritance is not flexible, since we will end up with too many subclasses. 
Such a hierarchy is difficult to maintain, difficult to extend and difficult to use.

But, if we enclose a window in an object which can add new features, such as scroll bar and border dynamically, 
we will have a much more flexible solution. The "enclosed" object is a decorator.


The Decorator pattern attaches additional responsibilities to an object dynamically.


* Story

The spoilers that are added to a car are examples of the Decorator. 
The spoilers do not change the car itself, but add additional functionality which is to 'spoil' unfavorable air movement across a body of a vehicle in motion, usually described as turbulence or drag.


* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/decorator.jpg "013 Porsche 911 Carrera S (8233337583)")  
######  <a href="https://commons.wikimedia.org/wiki/File:2013_Porsche_911_Carrera_S_(8233337583).jpg">2013 Porsche 911 Carrera S (8233337583)</a>, by <a href="http://www.flickr.com/people/15779944@N00">steve lyon</a> from los angeles, ca, usa,<a href="https://creativecommons.org/licenses/by-sa/2.0/legalcode">CC BY-SA 2.0</a>

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/decorator.png "UML Decorator")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to decorator folder:

```
$  cd /src/main/java/com/hundredwordsgof/decorator
```

* Structure

The *Component* defines interfaces for new features which will be added dynamically.  
The *ConcreteComponent* class defines object where new features can be added.  
The *Decorator* abstract class holds reference to the *Component* object.  
The *ConcreteDecorator* class adds new features to the *Component* object.  


* Known uses 

  all subclases of the:
  * [java.io.InputStream](https://docs.oracle.com/javase/7/docs/api/java/io/InputStream.html) 
  * [java.io.OutputStream](https://docs.oracle.com/javase/7/docs/api/java/io/OutputStream.html)
  * [java.io.Reader](https://docs.oracle.com/javase/7/docs/api/java/io/Reader.html)
  * [java.io.Writer](https://docs.oracle.com/javase/7/docs/api/java/io/Writer.html)
  e.g.
  * [java.io.BufferedInputStream(InputStream)](https://docs.oracle.com/javase/7/docs/api/java/io/BufferedInputStream.html)
  * [java.io.DataInputStream(InputStream)](https://docs.oracle.com/javase/7/docs/api/java/io/DataInputStream.html)
  * [java.io.BufferedOutputStream(OutputStream)](https://docs.oracle.com/javase/7/docs/api/java/io/BufferedOutputStream.html)
  * [java.util.zip.ZipOutputStream(OutputStream)](https://docs.oracle.com/javase/7/docs/api/java/util/zip/ZipOutputStream.html)

  * [javax.servlet.http.HttpServletRequestWrapper](https://docs.oracle.com/javaee/6/api/javax/servlet/http/HttpServletRequestWrapper.html)
  * [javax.servlet.http.HttpServletResponseWrapper](https://docs.oracle.com/javaee/6/api/javax/servlet/http/HttpServletResponseWrapper.html)

  * [java.util.Collections#checked()](https://docs.oracle.com/javase/8/docs/api/java/util/Collections.html#checkedCollection-java.util.Collection-java.lang.Class-)
  * [java.util.Collections#synchronized()](https://docs.oracle.com/javase/8/docs/api/java/util/Collections.html#synchronizedCollection-java.util.Collection-)
  * [java.util.Collections#unmodifiable()](https://docs.oracle.com/javase/8/docs/api/java/util/Collections.html#unmodifiableCollection-java.util.Collection-)


##### <a id="Facade"></a>Facade

* Motivation

Let's say that we need to develop a compiler for a brand new programming language.


The compiling process consist of steps, such as scanning, tokenizing, parsing, building abstract syntax tree, code generation, etc. 
We need to develop a separate subcomponent for each step. In principle, each subcomponent is complex, and the usage of subcomponents is complex as well.


It does not make sense for a client which wants to compile code to invoke complex subcomponents in order to compile.


A better approach would be to define a uniform interface which presents the compiler functionality – a Compiler class. 
The Compiler class hides "low-level" functionality from the client, so we can say that Compiler class is a facade.


The Facade design pattern hides the complexity of a system and provides an interface to the client through which the client can access the system.

* Story

You want to organize a marriage reception with dinner for 100 people. 
So, in order to organize such event, you need to find and decorate a hall where the event will happen, then you need to organize the band, 
organize flowers, send invitations, and so on and so on.

If this is too much trouble for you, you could hire an event manager who will organize the event for you.

This is a typical example for Facade.
 

* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/facade.jpg "Event Management in Pune")  
###### Event Management in Pune, By WeMaxx1248 (Own work) [<a href="http://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a>], <a href="https://commons.wikimedia.org/wiki/File%3AEvent_management_in_pune.jpg">via Wikimedia Commons</a>

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/facade.png "UML Facade")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to facade folder:

```
$  cd /src/main/java/com/hundredwordsgof/facade
```

* Structure

The UML diagram consist of *Facade* and subsystem classes.


* Known uses 

  * [javax.faces.context.FacesContext](https://docs.oracle.com/javaee/7/api/javax/faces/context/FacesContext.html), internally uses [LifeCycle](https://docs.oracle.com/javaee/7/api/javax/faces/lifecycle/Lifecycle.html), [ViewHandler](https://docs.oracle.com/javaee/7/api/javax/faces/application/ViewHandler.html), [NavigationHandler](https://docs.oracle.com/javaee/7/api/javax/faces/application/NavigationHandler.html) etc.
  * [javax.faces.context.ExternalContext](https://docs.oracle.com/javaee/7/api/javax/faces/component/UIComponent.html#getChildren--), internally uses [ServletContext](https://docs.oracle.com/javaee/7/api/javax/servlet/ServletContext.html), [HttpSession](https://docs.oracle.com/javaee/7/api/javax/servlet/http/HttpSession.html), [HttpServletRequest](https://docs.oracle.com/javaee/7/api/javax/servlet/http/HttpServletRequest.html), [HttpServletResponse](https://docs.oracle.com/javaee/7/api/javax/servlet/http/HttpServletResponse.html), etc.
  * [java.lang.Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html), acts as a facade for [Reflection API](https://docs.oracle.com/javase/7/docs/api/java/lang/reflect/package-summary.html)(getConstructors(), getMethods())

##### <a id="Flyweight"></a>Flyweight

* Motivation

Let's imagine that you are teaching youngsters programming. 
You decided to start with simple but exciting example, so during the course, a graphical editor which can draw a line will be developed.


The Base artifact is a Line class, with start and end point. 
Now a draw method needs to be implemented – and voila, our simple graphical editor is implemented. 
After using the editor for a while, we decide that a new feature should be implemented: in fact, we want our line to have basic colors.


The Line class will be extended with a new attribute (Color class), which holds information about the color, and the draw method will be 
extended accordingly. Now we have a new version of our editor, and some users want to test the editor to its limits, 
so they draw several thousand lines. Drawing several thousand lines means that we have several thousand Line objects in memory, 
but we also have several thousand Color objects in memory, even if our editor is drawing lines with basic colors only.


Can we use memory more efficiently? 
The Color objects include information that is duplicated. 
Why not set up a pool of basic color objects and share those colors when a Line object needs it?


The properties of the objects which are shared and are reasonably unchanging are moved into flyweight objects. 
For each of the Line objects which use the shared data, only a reference to the appropriate flyweight object is required. 
This will drastically reduce the memory used by each of the Line objects.


The solution used in explanation is an example of the Flyweight pattern. 
The Flyweight patterns remove duplicates and reduce memory by loading only the data necessary to perform action.


* Story

Database normalization is flyweight. 
Normalization is the process of organizing the columns (attributes) and the tables (relations) of a relational database to minimize data redundancy

* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/flyweight.jpg "Normal Form Diagram")  
###### Normal Form Diagram, By 04hutts (Own work) [Public domain], <a href="https://commons.wikimedia.org/wiki/File%3ANormalFormDiagram.png">via Wikimedia Commons</a>

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/flyweight.png "UML Flyweight")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to flyweight folder:

```
$  cd /src/main/java/com/hundredwordsgof/flyweight
```

* Structure

The Flyweight pattern uses the concepts of intrinsic and extrinsic data.  
The intrinsic data is held in the properties of the flyweight objects, which are shared.  
This information is stateless and generally remains unchanged, as any changes would be effectively replicated among all of the objects that reference 
the flyweight. Extrinsic data can be state-full, as it is held outside of a flyweight object. 
It can be passed to methods of a flyweight when needed, but should never be stored within a shared flyweight object.


The *Flyweight* interface defines interfaces through which flyweight can receive and act on extrinsic states.   
The *ConcreteFlyweight* class implements *Flyweight* and adds storage for intrinsic state (Character).   
The *UnsharedConcreteFlyweight* class defines objects which are not shared.   
The *FlyweightFactory* class creates and manages the flyweight objects.  
The *Client* class keeps flyweight reference and stores extrinsic state.  


* Known uses 

  * [java.lang.Integer#valueOf(int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html#valueOf-int-)
  * [java.lang.Boolean#valueOf(int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html#valueOf-boolean-)
  * [java.lang.Byte#valueOf(int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Byte.html#valueOf-byte-)
  * [java.lang.Character#valueOf(int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#valueOf-char-)
  * [java.lang.Short#valueOf(int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Short.html#valueOf-short-)
  * [java.lang.Long#valueOf(int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html#valueOf-long-)
  * [java.lang.BigDecimal#valueOf(int)](https://docs.oracle.com/javase/8/docs/api/java/math/BigDecimal.html#valueOf-long-int-)


##### <a id="Proxy"></a>Proxy

* Motivation

Imagine that we are implementing a Viewer application, which will show a Microsoft Word document in read only mode.

The Viewer must open and load document quickly, but the problem is that during loading of the document, 
we don't know if there are any "heavy" objects inside a document. 
A heavy object can be an image which is injected in a Word document on, let's say, page 10 of the document.

So, a straight solution where we simply load everything that is inside the document can be slow.


Another solution would be that heavy objects are loaded on demand: in our example, 
an image will be loaded when the user is on the page 10 of the document. 
Meanwhile, the heavy object will be presented by another, "lighter" object, which acts as original.


That solution is a Proxy.


The Proxy pattern provides a surrogate or a placeholder for another object to control access to it.


* Story

An Envoy Extraordinary is a Proxy. 
He is an accredited messenger, agent, or representative, who is sent by one government to represent it in dealings with another government.


* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/proxy.jpg "The Envoy Extraordinary")  
###### Burmese ambassador, The Envoy Extraordinary and Minister Plenipotentiary, By John Watkins (Kenwoon Mengyee) [Public domain or Public domain], <a href="https://commons.wikimedia.org/wiki/File%3AKinwun_Mingyi.jpg">via Wikimedia Commons</a>

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/proxy.png "UML Proxy")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to proxy folder:

```
$  cd /src/main/java/com/hundredwordsgof/proxy
```

* Structure

The *Subject* interface defines a common interface for the *RealSubject* and the *Proxy*.  
The *RealSubject* class points to the real object which the 
*Proxy* represents.  
The *Proxy* class keeps reference to the real subject: it can act as a surrogate, controlling access to the real subject and can be 
responsible for creation and maintenance of the *Real* subject.


The *Proxy* can be used in many situations, therefore we have the following Proxy types:  
The *Remote Proxy* - represents an object in a different address space.   
The *Virtual Proxy* - creates "heavy" objects on demand.   
The *Protection Proxy* - controls access to the object, protects the target from bad clients (Firewall proxy).   
The *Smart reference* - replacement for a smart pointer, can be used as a counter of the created objects.   
The *Cache Proxy* - stores the results of most frequently used target operations.   
The *Synchronization Proxy* - allows safe concurrent accesses to the target object by different client objects.   
The *Counting Proxy* - provides audit mechanism before executing a method on the target object.  


* Known uses

  * [java.lang.reflect.Proxy](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/Proxy.html)
  * [java.rmi.*](https://docs.oracle.com/javase/8/docs/api/java/rmi/package-summary.html)
  * [javax.persistence.PersistenceContext](https://docs.oracle.com/javaee/7/api/javax/persistence/PersistenceContext.html)

  
##### <a id="ChainOfResponsibility"></a>Chain Of Responsibility

* Motivation

Imagine that you just have bought a new wireless router from the local Internet Service Provider. 
You unpack a router from the box, plug the necessary cables and you switch on your new wireless router. 
But, the router is not able to establish an Internet connection. 
After checking the technical manuals and playing with router settings, you finally give up and you call the ISP operator's call center.


The first thing you hear is a machine voice of the auto responder. 
It suggests dozen of possible solutions to various problems, but none of those are related to your particular problem. 
After a while, the machine connects you to the live operator. After a short discussion, the operator realizes that he cannot help you either. 
So, he connects you to an engineer, who finally fixes your problem.


That was an example of the Chain of Responsibility.


In essence, we pass an object along a "chain" of potential handlers for that object until one of the handlers handles the request.
The Chain of Responsibility allows an object to send a command without knowing which object will receive and handle it. 
The request is sent from one object to another, making them parts of a chain and each object in this chain can handle the command, 
pass it on or do both.


* Story

A King and his army is an example of the Chain of Responsibility. 
The King gives orders to his army. The closest element to react would be the commander, 
then the officer and then the soldier and those three elements would form a Chain of Responsibility.

* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/chainofresponsibility.jpg "Zulu Soldiers of King Panda’s Army, 1847")  
###### By George French Angas, 1822-1886 (Bibliothèque numérique mondiale), Zulu Soldiers of King Panda’s Army, 1847 [Public domain], <a href="https://commons.wikimedia.org/wiki/File%3AZulu_soldiers_of_the_army_of_King_Umpande_(Panda)%2C_1847.png">via Wikimedia Commons</a>


* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/chainofresponsibility.png "UML Chain Of Responsibility")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to chainofresponsability folder:

```
$  cd /src/main/java/com/hundredwordsgof/chainofresponsibility
```

* Structure

A *Handler* defines interface for request handling.  
The *ConcreteHandler* handles the request, can access the next object in the chain and forward the request if necessary.  
A client initiates requests to the *ConcreteHandler*.  


* Known uses

  * [java.util.logging.Logger#log()](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Logger.html#log-java.util.logging.Level-java.lang.String-)
  * [javax.servlet.Filter#doFilter()](https://docs.oracle.com/javaee/7/api/javax/servlet/Filter.html#doFilter-javax.servlet.ServletRequest-javax.servlet.ServletResponse-javax.servlet.FilterChain-)
  * [java.awt.AWTEventMulticaster](https://docs.oracle.com/javase/7/docs/api/java/awt/AWTEventMulticaster.html)

##### <a id="Command"></a>Command

* Motivation

Imagine that we are developing a graphical editor. The user can add new text, delete or update existing text.

What to do in a case when user does something wrong? The user should be able to return back to the state of the text before the wrong action has 
been executed.


How to implement such behavior?


One solution would be to hold a list of the text states. 
If the text is long and if we store a lot of states of such a long text, we can run out of memory, 
so this solution is not appropriate for our particular scenario.


What if we consider an idea where the current state of text is a result of execution of a sequence of operations? 
These operations can be undone, with the effect that the text reverts to a previous state. 
The operations that have been undone become redoable, so that later model states can be reached again if necessary. 
So, we will no longer invoke operations on the text directly, but we will create Command objects, which invoke the operations. 
Each text operation will have the appropriate Command object.

This solution is a Command pattern. 
The Command pattern issues requests to objects without knowing anything about the operation being requested or about the receiver of the request.

* Story

When your car needs servicing, you visit a Car Service Center. Upon arrival, you explain the problem and you leave the car. 
The person at reception summarizes the problem and enters it into an order for the Car Technician. 
The order is queued internally. The Car Technician will receive the request and fix the problem.

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/command.png "UML Command")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to command folder:

```
$  cd /src/main/java/com/hundredwordsgof/command
```

* Structure

The *Command* declares an interface for executing an operation.  
The *ConcreteCommand* class defines the binding between a *Receiver* object and an action.  
The *Receiver* class knows how to perform the operations associated with carrying out a request.  
The *Invoker* class sends the command to carry out a request.  
The *Client* class creates a *ConcreteCommand* object and sets its receiver.  


* Known uses 

  * [java.lang.Runnable](https://docs.oracle.com/javase/8/docs/api/java/lang/Runnable.html)
  * [javax.swing.Action](https://docs.oracle.com/javase/8/docs/api/javax/swing/Action.html)

##### <a id="Interpreter"></a>Interpreter
* Motivation

* Story

A person who provides an oral translation from one language into another.

* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/interpreter.jpg "Polish Sign Language - letter C")  
######  Polish Sign Language - letter C, By Tomt87 (Own work) [CC BY-SA 4.0 (http://creativecommons.org/licenses/by-sa/4.0)], via Wikimedia Commons


* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/interpreter.png "UML Command")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to command folder:

```
$  cd /src/main/java/com/hundredwordsgof/interpreter
```

* Structure

Efficiency is a big concern for any implementation of this pattern. 
Introducing your own grammar requires extensive error checking, which will be time consuming for the programmer to implement, 
and needs careful design in order to run efficiently during runtime. 
Also, as the grammar becomes more complicated, the maintenance effort increases.


The *AbstractExpresion* defines interface for interpretation.  
The *TerminalExpresion* implements the *AbstractExpression* for literal symbols in the grammar.   
One object is defined for each literal symbol.   
The *NonterminalExpresion* implements *AbstractExpression* for grammar rules.   
One class per grammar rule is defined.   
The *Client* class creates an *Abstract Syntax Tree*, which represents expression defined in grammar.  


* Known uses 

  * [java.util.Pattern](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html)
  * [java.text.Normalizer](https://docs.oracle.com/javase/8/docs/api/java/text/Normalizer.html)
  * All subclasses of [java.text.Format](https://docs.oracle.com/javase/8/docs/api/java/text/Format.html)
  * All subclasses of [javax.el.ELResolver](https://docs.oracle.com/javaee/7/api/javax/el/ELResolver.html)

  
##### <a id="Iterator"></a>Iterator

* Motivation

In computer science, a data structure is a particular way of organizing and storing data, so that it can be accessed and modified efficiently. 
More precisely, a data structure is a collection of data values, the relationships among them, and the functions or operations 
which can be applied to the data.


There are numerous types of data structures, such as linked lists, arrays, vectors, maps, etc. 
Each collection of the data structure has its own structure and its own way of accessing elements of the collection.


In practice, it is not convenient to access each type of collection in a different way, so it would be nice to have a common interface for 
element-by-element access to a collection, independent of the collection’s shape.


The Iterator pattern lets you do all this. 
The key idea is to take the responsibility for access and traversal out of the aggregate object and put it into an Iterator object which 
defines a standard traversal protocol.

So, an Iterator pattern provides a way of accessing the elements of an aggregate object sequentially, without exposing its underlying representation.

* Story

A book is a set of written, printed sheets bound together into a volume. 
You can browse through the book page by page, or quickly jump to an interesting chapter. 
The process of browsing is an example of the Iterator pattern.


* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/iterator.jpg "Iterate book page by page")  
###### Open Book by Dave Dugdale, on Flickr&quot;&nbsp;(<a rel='license' href='https://creativecommons.org/licenses/by-sa/2.0/' target='_blank'>CC BY-SA 2.0</a>)&nbsp;by&nbsp; <a xmlns:cc='http://creativecommons.org/ns#' rel='cc:attributionURL' property='cc:attributionName' href='https://www.flickr.com/people/davedugdale/' target='_blank'>Dave Dugdale</a>


* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/iterator.png "UML Iterator")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to iterator folder:

```
$  cd /src/main/java/com/hundredwordsgof/iterator
```

* Structure

The *Iterator* defines an interface for accessing and traversing elements.  
The *ConcreteIterator* implements the *Iterator* interface, keeps track of the current position in the traversal of the aggregate.   
The *Aggregate* defines an interface for creating an *Iterator* object.   
The *ConcreteAgregate* class implements the *Iterator* creation interface to return an instance of the proper *ConcreteIterator*.  


* Known uses 

  * All implementations of [java.util.Iterator](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html)
  * All implementations of [java.util.Enumeration](https://docs.oracle.com/javase/8/docs/api/java/util/Enumeration.html)


##### <a id="Mediator"></a>Mediator

* Motivation

Imagine that we need to develop a flight simulator. Our flight simulator will have base artifacts, like airport and aircraft. 
An aircraft can take off from the airport, fly in the sky and land on the airport.


Imagine a scenario when one particular aircraft is landing on the airport: how can that aircraft be sure that the other aircrafts are not 
trying to land on the same airport at the same time? It is obvious that our aircraft can't talk to each and every aircraft which is currently 
approaching the airport.


A better approach would be to introduce a mediator, which is a "man in the middle", meaning that all the aircrafts will communicate only with the mediator. 
The task of ensuring the safe operations of the aircrafts belongs to air traffic controllers, who are mediators. 
They must coordinate the movements of all the aircrafts, keep them at safe distances from each other, direct them during takeoff and landing, 
direct them around bad weather and ensure that the air traffic flows smoothly with minimal delays.


The example above is a Mediator pattern. The Mediator pattern defines an object that controls how a set of objects interacts.


* Story

A Radio Taxi is an example of the Mediator pattern. 
The taxi drivers communicate with the Mediator (Radio Taxi Call Center), rather than with each other.


When a customer needs a taxi, he calls the Radio Taxi Call Center. 
All taxis have GPS units, which tell the Radio Taxi Call Center the taxis' current locations; there is also a central information system, 
which tells which taxi is currently available to serve the customer. 
The call center will contact the available taxi nearest to customer’s location and send it to serve the customer.


* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/mediator.jpg "Call Center Taxis Libres")  
###### Call Center Taxis Libres,By Jquemba (Own work) [Public domain], via Wikimedia Commons 

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/mediator.png "UML Mediator")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to mediator folder:

```
$  cd /src/main/java/com/hundredwordsgof/mediator
```

* Structure

A *Colleague* defines an interface for communication with another *Colleague* via the *Mediator*.  
For the *ConcreteColleague* class, each *Colleague* class knows its *Mediator* object, and each *Colleague* communicates with its mediator 
whenever it would have otherwise communicated with another colleague.  
The *Mediator* defines an interface for communicating with *Colleague* objects.  
The *ConcreteMediator* implements cooperative behavior by coordinating the *Colleague* objects. 


* Known uses 

  * [java.util.Timer](https://docs.oracle.com/javase/8/docs/api/java/util/Timer.html) (all scheduleXXX() methods)
  * [java.util.concurrent.Executor#execute()](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Executor.html#execute-java.lang.Runnable-)
  * [java.util.concurrent.ExecutorService](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ExecutorService.html) (the invokeXXX() and submit() methods)
  * [java.util.concurrent.ScheduledExecutorService](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ScheduledExecutorService.html) (all scheduleXXX() methods)
  * [java.lang.reflect.Method#invoke()](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/Method.html#invoke-java.lang.Object-java.lang.Object...-)

##### <a id="Memento"></a>Memento

* Motivation

Modern cars have brakes on all four wheels, operated by a hydraulic system. 
The brakes may be disc type or drum type.


The front brakes play a greater part in stopping the car than the rear ones, because braking throws the car weight forward on to the front wheels.


Many cars therefore have disc brakes, which are generally more efficient, at the front, and drum brakes at the rear.


Imagine a scenario in which we need to replace the drum brakes at the rear by ourselves? 
How  do we ensure that the new drum brake has all the necessary pieces in their proper places? 
One solution might be to use the Memento.


The drums are removed from both sides, exposing both the right and left brakes. 
Only one side is disassembled and the other serves as a Memento of how the brake parts fit together. 
The other side is disassembled only after the job has been completed on one side. 
When the second side is disassembled, the first side acts as the Memento.


Thus we have an example of the Memento design pattern. 
Memento design pattern helps to restore an object’s state to it previous state.


* Story

Transactions are operations on the database which occur in an atomic, consistent, durable, and isolated fashion. 
A transaction can contain multiple operations on the database. Each operation can succeed or fail, however, a transaction guarantees that, 
if all operations succeed, the transaction would commit and would be final. 
And if any operation fails, then the transaction would fail and all operations would roll back and leave the database in its original state, 
as if nothing has happened.

This rollback mechanism uses the Memento design pattern.
 

* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/memento.jpg "States of transaction")  
###### States of transaction 

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/memento.png "UML Memento")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to memento folder:

```
$  cd /src/main/java/com/hundredwordsgof/memento
```

* Structure

The *Originator* creates a *Memento* containing a snapshot of its current internal state and uses the *Memento* to restore its previous internal state.  
The *Memento* stores the internal state of the *Originator* object and protects against access by objects other than the *Originator*.   
The *Caretaker* class is responsible for *Memento's* safekeeping. 


* Known uses 

  * All implementations of [java.io.Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)
  * All implementations of [javax.faces.component.StateHolder](https://docs.oracle.com/javaee/7/api/javax/faces/component/StateHolder.html)

##### <a id="Observer"></a>Observer

* Motivation

Imagine that we are developing a computer game.


One feature of our game will be the awards system. 
Players will earn dozens of different badges for completing specific milestones during the game.


When players pass or reach a certain point in the game, for example jump over a complex fence, we need to catch that part of the code and calculate the award.


But, how should we implement such a feature?


One approach would be to find a place in the code where specific milestones are completed and extend those places with code which calculates the 
awards. This approach is not flexible, it is not intuitive, and makes our code complex and difficult and violates the single responsibility principle.


Another approach would be to create award events in the code, where specific milestones are completed. Award events are then published as 
notifications, regardless of who receives the notification. 
The awards system is listening to all award events and implements all the necessary logic.


This solution is the Observer pattern.


The Observer pattern defines a one-to-many dependency between objects, so that when one object changes state, all its dependents are notified and 
updated automatically.


* Story

Keep me updated.


A newsletter subscription demonstrates the Observer pattern. 
A newsletter is a regularly distributed publication that is generally about one main topic of interest to its subscribers. 
The subscribers can subscribe or unsubscribe to the newsletters.



* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/observer.jpg "Newsletter Banner")  
###### Newsletter Banner by, <a href="https://commons.wikimedia.org/wiki/User:Stevie_Benton_(WMUK)">Stevie Benton</a>, <a href="https://commons.wikimedia.org/wiki/File:Newsletter-banner-v2.jpg">Newsletter-banner-v2</a>, <a href="https://creativecommons.org/licenses/by-sa/3.0/legalcode">CC BY-SA 3.0</a>

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/observer.png "UML Observer")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to observer folder:

```
$  cd /src/main/java/com/hundredwordsgof/observer
```

* Structure

The *Observer* defines an updating interface for objects which should be notified of changes in a subject.  
The *Subject* knows its observers.  
A subject can be observed by any number of *Observer* objects.  
The *ConcreteSubject* stores the state of interest to *ConcreteObserver* objects and sends notifications to its observers when its state changes.  
The *ConcreteObserver* maintains a reference to a *ConcreteSubject* object, stores the state that should stay consistent with the subject's and 
implements the *Observer* updating interface to keep its state consistent with the subject's.  


* Known uses 

  * [java.util.Observer](https://docs.oracle.com/javase/8/docs/api/java/util/Observer.html)
  * [java.util.Observable](https://docs.oracle.com/javase/8/docs/api/java/util/Observable.html)
  * [java.util.EventListener](https://docs.oracle.com/javase/8/docs/api/java/util/EventListener.html)
  * [javax.servlet.http.HttpSessionBindingListener](https://docs.oracle.com/javaee/7/api/javax/servlet/http/HttpSessionBindingListener.html)
  * [javax.servlet.http.HttpSessionAttributeListener](https://docs.oracle.com/javaee/7/api/javax/servlet/http/HttpSessionAttributeListener.html)
  * [javax.faces.event.PhaseListenerl](https://docs.oracle.com/javaee/7/api/javax/faces/event/PhaseListener.html)
  
##### <a id="State"></a>State

* Motivation

Imagine that we need to implement a state machine. 
We begin with a few states, and a few simple conditions for those states. 
Our initial State machine is implemented using if/else blocks, which are checking the current state and which perform the appropriate actions.


But, the number of states gradually increases over time. 
In addition, the conditions for reaching certain states become more complex. 
Our 'if/else' based state machine has more and more 'if/else' blocks and it becomes really difficult to maintain and debug such a code base.


Is there a more elegant way to implement the State Machine?


Another approach would be that, for every possible state, a separate class is implemented over a common  interface, with the state related behavior. 
The Context class will contain a reference to a state object, which represents its current state. 
Instead of acting on its own, the context will delegate the execution to the state object. 
To change the state of the context, one would pass another state object to the context.


This solution is an example of the State pattern.


The State pattern allows an object to alter its behavior when its internal state changes.


* Story

Behavior depends on its state.


Pregnancy is a time of great physical and emotional change for women. 
Everything from the size of her belly to the speed at which her heart beats will change over the nine months leading up to the childbirth. 
Partly as the result of hormonal fluctuations, and partly due to the physical strain of carrying extra body weight, 
pregnant women can expect to buy new bras, search for ways to alleviate swollen ankles, gasp for breath after climbing a few stairs, 
and marvel at how quickly their nails grow.


* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/state.jpg "Human Pregnancy")  
###### <a href="https://commons.wikimedia.org/wiki/File:Pregnant_graffiti.jpg">Pregnant graffiti</a> by, <a href="http://flickr.com/photos/19616008@N00">Petteri Sulonen from Helsinki, Finland</a>, <a href="https://creativecommons.org/licenses/by/2.0/legalcode">CC BY 2.0</a>

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/state.png "UML State")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to state folder:

```
$  cd /src/main/java/com/hundredwordsgof/state
```

* Structure

The *State* defines an interface for encapsulating the behavior associated with a particular state of the Context.  
The *ConcreteState* implements a behavior associated with the state of the *Context*.  
The *Context* class maintains an instance of a *ConcreteState* subclass which defines the current state.  


* Known uses 

  * [javax.faces.lifecycle.LifeCycle#execute()](https://docs.oracle.com/javaee/7/api/javax/faces/lifecycle/Lifecycle.html#execute-javax.faces.context.FacesContext-)
  
  
##### <a id="Strategy"></a>Strategy

* Motivation

Imagine that we need to implement a network load balancer. 
The Load balancer serves as the single point of contact for clients: it distributes incoming traffic across multiple targets, 
which increases the availability and capability of your application.


The question is: how will the load balancer distribute the incoming traffic? 
We can have various algorithms, like round robin, ip-hash, least connected, etc. 
New algorithms can be introduced over time. 
So, it is obvious that an algorithm for traffic distribution can be implemented in different ways.


A straight solution would be to implement a few algorithms and hide the invocation of the algorithm in an 'if/then' or in a 'switch' statement.


Is the proposed solution flexible enough?


Another solution would be to define a common interface for our algorithm and then encapsulate the behavior of an algorithm as an object which 
implements a common interface. 
During runtime we can select which object to use and many different behaviors can be implemented without 
creating huge 'if/then' or 'switch' statements.


This solution is a Strategy pattern. 

The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. 
The Strategy lets the algorithm vary independently from the clients that use it.


* Story

Select an algorithm at runtime.


The payment options in a Shopping Cart are an example of a Strategy. 
User can choose various payment options, such as Master Card, Amex or PayPal. 
Any of these payment options will pay for the items in the Shopping Cart, and they can be used interchangeably. 
The user may choose the Strategy based on his possibilities and preferences.


* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/strategy.jpg "Credit Card")  
###### Credit Card&nbsp;(<a rel='license' href='https://creativecommons.org/licenses/by/2.0/' target='_blank'>CC BY 2.0</a>)&nbsp;by&nbsp;<a xmlns:cc='http://creativecommons.org/ns#' rel='cc:attributionURL' property='cc:attributionName' href='https://www.flickr.com/people/mecklenburg/' target='_blank'>ThomasKohler</a>

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/strategy.png "UML Strategy")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to strategy folder:

```
$  cd /src/main/java/com/hundredwordsgof/strategy
```

* Structure

The *Strategy* declares an interface common to all supported algorithms.  
The *ConcreteStrategy* implements the algorithm using the *Strategy* interface.   
The *Context* uses this interface to call the algorithm defined by a *ConcreteStrategy*.  


* Known uses 

  * [java.util.Comparator#compare()](https://docs.oracle.com/javase/8/docs/api/java/util/Comparator.html#compare-T-T-), executed by among others [Collections#sort()]()
  * [javax.servlet.Filter#doFilter()](https://docs.oracle.com/javaee/7/api/javax/servlet/Filter.html#doFilter-javax.servlet.ServletRequest-javax.servlet.ServletResponse-javax.servlet.FilterChain-)
  
##### <a id="TemplateMethod"></a>TemplateMethod

* Motivation

Imagine that we need to implement an application which performs various operations on a database. We decide to use JDBC, which is a standard Java interface for accessing a relational database. 
Using JDBC for database operations (for example, a read operation via select SQL statement), the user must execute following steps:

* connect to database   
* execute SQL statement   
* process data which are gathered from database   
* close database connection   
* handle errors if something goes wrong   

If we implement such a database operation several times for various read operations, we will find out that we are repeating some steps. 
We can also see that some steps are always the same, i.e. 'connect to database', 'close database connection', 'handle errors'. 
The remaining steps, such as 'execute SQL statement' and 'process data obtained from the database' are different for each read operation. 
So, let's call those steps which are the same 'invariant' and remaining steps 'variant'.


We now implement invariant steps inside an abstract base class, while the variant steps are either given a default implementation, or no 
implementation at all. The variant steps represent "hooks", or "placeholders", that may, or must, be supplied by the component's client in a 
concrete derived class.


The solution in the above example is the Template Method design pattern.


The Template Method defines a skeleton of an algorithm in an operation. Algorithm will have a common part and a specialized part.

* Story

Daily routine is example of the Template Method. 
Every day people get up (common part), go to work (common part), do their job (specialized part), go home (common part) and go to sleep (common part). 
There are people with different professions, such as engineers, teachers, etc. During work, an engineer will fix machines, 
while teacher will teach children how to read and write. 
At the end of the day they go home, have dinner and go to sleep.

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/templatemethod.png "UML Template")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to template folder:

```
$  cd /src/main/java/com/hundredwordsgof/templatemethod
```

* Structure

The *AbstractClass* defines abstract primitive operations that concrete subclasses should implement.  
The *ConcreteClass* implements the abstract primitive operations to carry out subclass-specific steps of the algorithm.


* Known uses 

  * All non-abstract methods of [java.io.InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html), [java.io.OutputStream](https://docs.oracle.com/javase/8/docs/api/java/io/OutputStream.html), [java.io.Reader](https://docs.oracle.com/javase/8/docs/api/java/io/Reader.html) and [java.io.Writer](https://docs.oracle.com/javase/8/docs/api/java/io/Writer.html).
  * All non-abstract methods of [java.util.AbstractList](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractList.html), [java.util.AbstractSet](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractSet.html) and [java.util.AbstractMap](https://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html)


##### <a id="Visitor"></a>Visitor

* Motivation

Imagine that we need to implement a compiler. 
A compiler is a program which transforms code written in one programming language (the source language) into another programming 
language (the target language).

The compiler functionality is divided into two major blocks: a front-end and a back-end. 
The front-end block comprises of a sequence of several phases, with each stage taking input from its previous stage, 
modifying it and producing its own representation of the source program and passing it to the next phase. 
The front-end includes three main stages, which are called the lexical, the syntax and the semantic analysis.


The first phase takes the source code as a stream of characters and identifies distinct words (tokens), such as variable names, keywords and 
punctuators. 
The second phase determines the validity of syntactic organization of the program and produces the Abstract Syntax Tree (AST). 
The semantic analysis checks whether the AST follows the rules of a language (type checking, name resolution, etc.).


AST, which represents the program written in source code, is created during the second phase and is used in later phases of the compiling process 
for operations such as type-checking, code generation, code optimization, flow analysis, pretty-printing, code instrumentation, etc.


Most of these operations will need to treat nodes that represent assignment statements differently from nodes that represent variables or 
arithmetic expressions. 
Distributing all these operations across the various node classes leads to a system that's hard to understand, maintain and change.


It would be better if each new operation could be added separately, and if the node classes were independent of the operations that apply to them. 
If we package related operations in a separate object, called a visitor, and pass it to elements of the AST as it is traversed, 
then when an element of the AST "accepts" the visitor, it sends a request to the visitor that encodes the element's class.


This solution is example of the Visitor design pattern.

The Visitor allows one or more operations to be applied to a set of objects at runtime, decoupling the operations from the object structure.


* Story

Shopping in a supermarket is an example of the Visitor pattern. You pick products and put them in a shopping cart. 
When you get to the checkout, the cashier acts as a visitor, taking the disparate set of elements, some with prices and others that need to be 
weighted, in order to provide you with the total to be paid.

* Image

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/gh-pages-resources/visitor.jpg "Cashier in Supermarket")  
###### Cashier in Supermarket, CC0 Public Domain

* Implementation

UML: 

![alt text](https://github.com/dstar55/100-words-design-patterns-java/blob/master/src/main/resources/visitor.png "UML Visitor")

Source Code:

Clone repo:
```
$  git clone https://github.com/dstar55/100-words-design-patterns-java.git .
```

Move to visitor folder:

```
$  cd /src/main/java/com/hundredwordsgof/visitor
```

* Structure

The *Visitor* declares a *Visit* operation for each class of *ConcreteElements* in the object structure.  
The *ConcreteVisitor* implements each operation declared by the *Visitor*.  
Each operation implements a fragment of the algorithm defined for the corresponding class of objects in the structure.   
The *Element* defines an *Accept* operation that takes a visitor as an argument.  
The *ConcreteElement* implements an *Accept* operation that takes a visitor as an argument.  
The *ObjectStructure* provides a composition or collection of the elements and allows the visitor to visit its elements.  


* Known uses 

  * [javax.lang.model.element.AnnotationValue](https://docs.oracle.com/javase/8/docs/api/javax/lang/model/element/AnnotationValue.html) and [AnnotationValueVisitor](https://docs.oracle.com/javase/8/docs/api/javax/lang/model/element/AnnotationValueVisitor.html)
  * [javax.lang.model.element.Element](https://docs.oracle.com/javase/8/docs/api/javax/lang/model/element/Element.html) and [ElementVisitor](https://docs.oracle.com/javase/8/docs/api/javax/lang/model/element/ElementVisitor.html)
  * [javax.lang.model.type.TypeMirror](https://docs.oracle.com/javase/8/docs/api/javax/lang/model/type/TypeMirror.html) and [TypeVisitor](https://docs.oracle.com/javase/8/docs/api/javax/lang/model/type/TypeVisitor.html)
  * [java.nio.file.FileVisitor](https://docs.oracle.com/javase/8/docs/api/java/nio/file/FileVisitor.html) and [SimpleFileVisitor](https://docs.oracle.com/javase/8/docs/api/java/nio/file/SimpleFileVisitor.html)
  * [javax.faces.component.visit.VisitContext](https://docs.oracle.com/javaee/7/api/javax/faces/component/visit/VisitContext.html) and [VisitCallback](https://docs.oracle.com/javaee/7/api/javax/faces/component/visit/VisitCallback.html)

  
