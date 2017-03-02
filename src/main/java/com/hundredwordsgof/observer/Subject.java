package com.hundredwordsgof.observer;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Subject knows its observers. Any number of Observer objects may observe a
 * subject.
 *
 */
abstract class Subject {

  private List<Observer> observers = new ArrayList<Observer>();

  public void attach(Observer observer) {
    observers.add(observer);
  }

  public void dettach(Observer observer) {
    observers.remove(observer);
  }

  public void notifyObervers() {
    for (Iterator iterator = observers.iterator(); iterator.hasNext();) {
      Observer observer = (Observer) iterator.next();
      observer.update();
    }
  }
}
