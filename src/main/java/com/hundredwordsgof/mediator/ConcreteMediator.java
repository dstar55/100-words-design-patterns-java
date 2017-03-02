package com.hundredwordsgof.mediator;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * ConcreteMediator implements Mediator, coordinates between Colleague objects.
 *
 */
public class ConcreteMediator implements Mediator {

  private List<Colleague> colleagues;

  public ConcreteMediator() {
    colleagues = new ArrayList<Colleague>();
  }

  public void addColleague(Colleague colleague) {
    colleagues.add(colleague);
  }

  public void notifyColleague(Colleague colleague, String message) {

    for (Iterator iterator = colleagues.iterator(); iterator.hasNext();) {
      Colleague receiverColleague = (Colleague) iterator.next();

      if (colleague != receiverColleague) {
        receiverColleague.receive(message);
      }
    }
  }
}
