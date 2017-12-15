# Chain Of Responsibility

+++

### Story 


The Chain of Responsibility allows an object to send a command without knowing which object will receive and handle it. 
The request is sent from one object to another making them parts of a chain and each object in this chain can handle the command, pass it on or do both. 

Service request to call center is example of the Chain of Responsibility. 
Request can be handled at front desk level, supervisor level or any higher level. 
Correct handler of request is only known during execution of the request when request is traversing at various levels. 




+++



### UML 
[![](http://www.design-patterns-stories.com/assets/img/uml/chainofresponsibility.png)](http://www.design-patterns-stories.com/assets/img/uml/chainofresponsibility.png)

