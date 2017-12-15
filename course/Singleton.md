# Singleton

+++

### Story 


Singleton ensures that only one(single) object can be created from the class.

Men's 100 meters world record holder is a singleton.
There can be at most one active "Men's 100 meters world record holder" at any given time. 
Regardless of who that person is the title, "Men's 100 meters world record holder" is a global point of access that identifies the fastes person in the world.


+++

### Image 


![alt text](http://www.design-patterns-stories.com/assets/img/image/singleton.jpg "Usain Bolt, Men's 100 meters world record holder")  
###### Brick Lane Graffiti Usain Bolt&nbsp;(<a rel='license' href='https://creativecommons.org/licenses/by/2.0/' target='_blank'>CC BY 2.0</a>)&nbsp;by&nbsp;<a xmlns:cc='http://creativecommons.org/ns#' rel='cc:attributionURL' property='cc:attributionName' href='https://www.flickr.com/people/mdpettitt/' target='_blank'>Martin Pettitt</a>


+++

### UML 
[![](http://www.design-patterns-stories.com/assets/img/uml/singleton.png)](http://www.design-patterns-stories.com/assets/img/uml/singleton.png)

+++

- Implementation

---?code=src/main/java/com/hundredwordsgof/singleton/Singleton.java&lang=java&title=Singleton

@[1,3-6](Present code found within any repo source file.)
