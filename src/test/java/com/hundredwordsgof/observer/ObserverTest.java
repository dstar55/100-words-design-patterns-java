package com.hundredwordsgof.observer;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * Test Observer pattern.
 */
public class ObserverTest {

  @Test
  public void testObserver() throws CloneNotSupportedException {

    ConcreteSubject subject = new ConcreteSubject();

    Observer observer = new ConcreteObserver(subject);
    subject.attach(observer);
    subject.setState(1);

    // changes via subject.setState is propagated towards observer
    assertEquals(1, ((ConcreteObserver) observer).getObserverState());

    subject.dettach(observer);
    subject.setState(0);

    // observer is detached so changes are not propageted
    assertEquals(1, ((ConcreteObserver) observer).getObserverState());
  }
}
