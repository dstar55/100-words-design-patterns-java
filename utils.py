'''
Created on 11 Oct 2016

@author: dstar55@yahoo.com
'''

# key, tuple dictionary
orderedPatternFilesDict = {"Singleton":( "Singleton.java",), # note that if there is just one item in a tuple, than we must add comma at the end of the statement, otherwise it will be threated as a string 
                            "Prototype":( "Prototype.java", "ConcretePrototype.java", "Client.java"),
                            "Builder":( "Builder.java", "ConcreteBuilder.java", "Product.java", "Director.java" ),
                            "FactoryMethod":( "Product.java", "ConcreteProductA.java", "ConcreteProductB.java", "Creator.java", "ConcreteCreator.java"),
                            "AbstractFactory":( "AbstractProductA.java", "ProductA1.java",  "ProductA2.java", "AbstractProductB.java", "ProductB1.java", "ProductB2.java", "AbstractFactory.java" ,  "ConcreteFactory1.java", "ConcreteFactory2.java" ),
                            "Adapter":(),
                            "Bridge":("Implementor.java", "ConcreteImplementorA.java", "ConcreteImplementorB.java", "RefinedAbstraction.java", "Abstraction.java"),
                            "Composite":("Component.java", "Leaf.java", "Composite.java" ),
                            "Decorator":("Component.java", "ConcreteComponent.java", "Decorator.java", "ConcreteDecoratorA.java", "ConcreteDecoratorB.java" ),
                            "Facade":("Compiler.java", "Tokenizer.java", "Generator.java", "Node.java", "ExpressionNode.java",  "OperandNode.java", "Parser.java"  ),
                            "Flyweight":("Flyweight.java", "ConcreteFlyweight.java", "UnsharedConcreteFlyweight.java", "FlyweightFactory.java" ),
                            "Proxy":("Subject.java", "RealSubject.java", "Proxy.java"),
                            "ChainOfResponsibility":( "Handler.java", "ConcreteHandler1.java", "ConcreteHandler2.java" ),
                            "Command":( "Command.java", "ConcreteCommand.java", "Receiver.java", "Invoker.java" ),
                            "Interpreter":( "AbstractExpression.java", "AndExpression.java", "OrExpression.java", "TerminalExpression.java", "Context.java" ),
                            "Iterator":( "Iterator.java", "ConcreteIterator.java", "Aggregate.java", "ConcreteAggregate.java"   ),
                            "Mediator":( "Colleague.java", "ConcreteColleague1.java", "ConcreteColleague2.java", "Mediator.java", "ConcreteMediator.java" ),
                            "Memento":( "Memento.java", "Originator.java", "Caretaker.java" ),
                            "Observer":( "Observer.java", "ConcreteObserver.java", "Subject.java", "ConcreteSubject.java"  ),
                            "State":( "State.java", "ConcreteState1.java", "ConcreteState2.java", "Context.java" ),
                            "Strategy":( "Strategy.java", "ConcreteStrategyA.java", "ConcreteStrategyB.java", "ConcreteStrategyC.java", "Context.java"  ),
                            "TemplateMethod":( "AbstractClass.java", "ConcreteClass.java" ),
                            "Visitor":( "Element.java", "ConcreteElementA.java", "ConcreteElementB.java", "Visitor.java", "ConcreteVisitor1.java", "ConcreteVisitor2.java", "ObjectStructure.java" )
                        }


# get position of the file, dictionary contains key and a tuple as a value. tuple contains ordered list of the file name for each key 
def getFilePosition(patternName, fileName):
    
    counter = 0
    try:
        for item in orderedPatternFilesDict.get(patternName):
            counter = counter + 1
            
            if str(item) == fileName:
                return counter
    except TypeError as e:
        return -1
           
    return -1

def getKey(item):
    return item[0]

def sort(lst):
    return sorted(lst, key=getKey)
    
