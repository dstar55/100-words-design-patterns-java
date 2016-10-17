'''
Created on 11 Oct 2016

@author: dstar55@yahoo.com
'''

import unittest
import utils

class TestUtils(unittest.TestCase):
    
    def setup(self):
        pass

    def test_updateDict(self):
        
        # prepare data     
        arrayList = []
        dict1 = {}
        dict1.update({"patternName": "Singleton"})
        dict1.update({"patternId": "Singleton"})
                        
        dict2 = {}
        dict2.update({"patternName": "Proxy"})
        dict2.update({"patternId": "Proxy"})

        arrayList.append(dict1)
        arrayList.append(dict2)
        
        # call update                
        utils.updateDict(arrayList, "Singleton", "patternName", "SingletonNameUpdated")        
        self.assertEqual("SingletonNameUpdated", arrayList[0].get("patternName"))
        
        utils.updateDict(arrayList, "Proxy", "patternName", "ProxyNameUpdated")
        self.assertEqual("ProxyNameUpdated", arrayList[1].get("patternName"))
        

    def test_extractSubStringBetween(self):
        self.assertEqual('Singleton', utils.extractSubStringBetween("* [Singleton](#Singleton)", '\[', '\]'))
        self.assertEqual('Singleton', utils.extractSubStringBetween("* [Singleton](#Singleton)", '\#', '\)'))
        
    def test_getKey(self):
        lst = [3, 2, 1]
        self.assertEqual(3, utils.getKey(lst))
        
    
    def test_sort(self):
        
        lst = [[3, 'Client.java'], [2, 'ConcretePrototype.java'], [1, 'Prototype.java']]
        
        sortedLst = utils.sort(lst)
        
        self.assertEqual(1, sortedLst[0][0])
        self.assertEqual('Prototype.java', sortedLst[0][1])

        self.assertEqual(2, sortedLst[1][0])
        self.assertEqual('ConcretePrototype.java', sortedLst[1][1])

        self.assertEqual(3, sortedLst[2][0])
        self.assertEqual('Client.java', sortedLst[2][1])
        
        
    def test_getFilePosition(self):
        self.assertEquals(-1, utils.getFilePosition("", ""))
        self.assertEquals(-1, utils.getFilePosition("x", "x"))
        
        self.assertEquals(1, utils.getFilePosition("Singleton", "Singleton.java"))
                        
        self.assertEquals(1, utils.getFilePosition("Prototype", "Prototype.java"))
        self.assertEquals(2, utils.getFilePosition("Prototype", "ConcretePrototype.java"))
        self.assertEquals(3, utils.getFilePosition("Prototype", "Client.java"))
        
        self.assertEquals(1, utils.getFilePosition("Builder", "Builder.java"))
        self.assertEquals(2, utils.getFilePosition("Builder", "ConcreteBuilder.java"))
        self.assertEquals(3, utils.getFilePosition("Builder", "Product.java"))
        self.assertEquals(4, utils.getFilePosition("Builder", "Director.java"))
        
        self.assertEquals(1, utils.getFilePosition("FactoryMethod", "Product.java"))
        self.assertEquals(2, utils.getFilePosition("FactoryMethod", "ConcreteProductA.java"))
        self.assertEquals(3, utils.getFilePosition("FactoryMethod", "ConcreteProductB.java"))
        self.assertEquals(4, utils.getFilePosition("FactoryMethod", "Creator.java"))
        self.assertEquals(5, utils.getFilePosition("FactoryMethod", "ConcreteCreator.java"))

        self.assertEquals(1, utils.getFilePosition("Strategy", "Strategy.java"))
        self.assertEquals(2, utils.getFilePosition("Strategy", "ConcreteStrategyA.java"))
        self.assertEquals(3, utils.getFilePosition("Strategy", "ConcreteStrategyB.java"))
        self.assertEquals(4, utils.getFilePosition("Strategy", "ConcreteStrategyC.java"))
        self.assertEquals(5, utils.getFilePosition("Strategy", "Context.java"))

        self.assertEquals(1, utils.getFilePosition("State", "State.java"))
        self.assertEquals(2, utils.getFilePosition("State", "ConcreteState1.java"))
        self.assertEquals(3, utils.getFilePosition("State", "ConcreteState2.java"))
        self.assertEquals(4, utils.getFilePosition("State", "Context.java"))

        self.assertEquals(1, utils.getFilePosition("AbstractFactory", "AbstractProductA.java"))
        self.assertEquals(2, utils.getFilePosition("AbstractFactory", "ProductA1.java"))
        self.assertEquals(3, utils.getFilePosition("AbstractFactory", "ProductA2.java"))
        self.assertEquals(4, utils.getFilePosition("AbstractFactory", "AbstractProductB.java"))
        self.assertEquals(5, utils.getFilePosition("AbstractFactory", "ProductB1.java"))
        self.assertEquals(6, utils.getFilePosition("AbstractFactory", "ProductB2.java"))
        self.assertEquals(7, utils.getFilePosition("AbstractFactory", "AbstractFactory.java"))
        self.assertEquals(8, utils.getFilePosition("AbstractFactory", "ConcreteFactory1.java"))
        self.assertEquals(9, utils.getFilePosition("AbstractFactory", "ConcreteFactory2.java"))
        
        self.assertEquals(1, utils.getFilePosition("ChainOfResponsibility", "Handler.java"))
        self.assertEquals(2, utils.getFilePosition("ChainOfResponsibility", "ConcreteHandler1.java"))
        self.assertEquals(3, utils.getFilePosition("ChainOfResponsibility", "ConcreteHandler2.java"))
        
        self.assertEquals(1, utils.getFilePosition("Composite", "Component.java"))
        self.assertEquals(2, utils.getFilePosition("Composite", "Leaf.java"))
        self.assertEquals(3, utils.getFilePosition("Composite", "Composite.java"))

        self.assertEquals(1, utils.getFilePosition("Proxy", "Subject.java"))
        self.assertEquals(2, utils.getFilePosition("Proxy", "RealSubject.java"))
        self.assertEquals(3, utils.getFilePosition("Proxy", "Proxy.java"))
        
        self.assertEquals(1, utils.getFilePosition("Memento", "Memento.java"))
        self.assertEquals(2, utils.getFilePosition("Memento", "Originator.java"))
        self.assertEquals(3, utils.getFilePosition("Memento", "Caretaker.java"))
        
        self.assertEquals(1, utils.getFilePosition("Command", "Command.java"))
        self.assertEquals(2, utils.getFilePosition("Command", "ConcreteCommand.java"))
        self.assertEquals(3, utils.getFilePosition("Command", "Receiver.java"))
        self.assertEquals(4, utils.getFilePosition("Command", "Invoker.java"))
        
        self.assertEquals(1, utils.getFilePosition("Bridge", "Implementor.java"))
        self.assertEquals(2, utils.getFilePosition("Bridge", "ConcreteImplementorA.java"))
        self.assertEquals(3, utils.getFilePosition("Bridge", "ConcreteImplementorB.java"))
        self.assertEquals(4, utils.getFilePosition("Bridge", "RefinedAbstraction.java"))
        self.assertEquals(5, utils.getFilePosition("Bridge", "Abstraction.java"))
        
        self.assertEquals(1, utils.getFilePosition("Iterator", "Iterator.java"))
        self.assertEquals(2, utils.getFilePosition("Iterator", "ConcreteIterator.java"))
        self.assertEquals(3, utils.getFilePosition("Iterator", "Aggregate.java"))
        self.assertEquals(4, utils.getFilePosition("Iterator", "ConcreteAggregate.java"))
        
        self.assertEquals(1, utils.getFilePosition("Observer", "Observer.java"))
        self.assertEquals(2, utils.getFilePosition("Observer", "ConcreteObserver.java"))
        self.assertEquals(3, utils.getFilePosition("Observer", "Subject.java"))
        self.assertEquals(4, utils.getFilePosition("Observer", "ConcreteSubject.java"))
        
        self.assertEquals(1, utils.getFilePosition("Mediator", "Colleague.java"))
        self.assertEquals(2, utils.getFilePosition("Mediator", "ConcreteColleague1.java"))
        self.assertEquals(3, utils.getFilePosition("Mediator", "ConcreteColleague2.java"))
        self.assertEquals(4, utils.getFilePosition("Mediator", "Mediator.java"))
        self.assertEquals(5, utils.getFilePosition("Mediator", "ConcreteMediator.java"))
               
        self.assertEquals(1, utils.getFilePosition("Decorator", "Component.java"))
        self.assertEquals(2, utils.getFilePosition("Decorator", "ConcreteComponent.java"))
        self.assertEquals(3, utils.getFilePosition("Decorator", "Decorator.java"))
        self.assertEquals(4, utils.getFilePosition("Decorator", "ConcreteDecoratorA.java"))
        self.assertEquals(5, utils.getFilePosition("Decorator", "ConcreteDecoratorB.java"))
        
        self.assertEquals(1, utils.getFilePosition("Flyweight", "Flyweight.java"))
        self.assertEquals(2, utils.getFilePosition("Flyweight", "ConcreteFlyweight.java"))
        self.assertEquals(3, utils.getFilePosition("Flyweight", "UnsharedConcreteFlyweight.java"))
        self.assertEquals(4, utils.getFilePosition("Flyweight", "FlyweightFactory.java"))
        
        self.assertEquals(1, utils.getFilePosition("Facade", "Compiler.java"))
        self.assertEquals(2, utils.getFilePosition("Facade", "Tokenizer.java"))
        self.assertEquals(3, utils.getFilePosition("Facade", "Generator.java"))
        self.assertEquals(4, utils.getFilePosition("Facade", "Node.java"))
        self.assertEquals(5, utils.getFilePosition("Facade", "ExpressionNode.java"))
        self.assertEquals(6, utils.getFilePosition("Facade", "OperandNode.java"))
        self.assertEquals(7, utils.getFilePosition("Facade", "Parser.java"))
        
        self.assertEquals(1, utils.getFilePosition("Interpreter", "AbstractExpression.java"))
        self.assertEquals(2, utils.getFilePosition("Interpreter", "AndExpression.java"))
        self.assertEquals(3, utils.getFilePosition("Interpreter", "OrExpression.java"))
        self.assertEquals(4, utils.getFilePosition("Interpreter", "TerminalExpression.java"))
        self.assertEquals(5, utils.getFilePosition("Interpreter", "Context.java"))

        self.assertEquals(1, utils.getFilePosition("TemplateMethod", "AbstractClass.java"))
        self.assertEquals(2, utils.getFilePosition("TemplateMethod", "ConcreteClass.java"))
        
        self.assertEquals(1, utils.getFilePosition("Visitor", "Element.java"))
        self.assertEquals(2, utils.getFilePosition("Visitor", "ConcreteElementA.java"))
        self.assertEquals(3, utils.getFilePosition("Visitor", "ConcreteElementB.java"))
        self.assertEquals(4, utils.getFilePosition("Visitor", "Visitor.java"))
        self.assertEquals(5, utils.getFilePosition("Visitor", "ConcreteVisitor1.java"))
        self.assertEquals(6, utils.getFilePosition("Visitor", "ConcreteVisitor2.java"))        
        self.assertEquals(7, utils.getFilePosition("Visitor", "ObjectStructure.java"))
        
        
if __name__ == '__main__':
    unittest.main()         