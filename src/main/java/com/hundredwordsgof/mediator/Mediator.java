package com.hundredwordsgof.mediator;

/**
 * Mediator defines an interface for communicating with Colleague objects.
 *
 */
public interface Mediator {

  void notifyColleague(Colleague colleague, String message);
}
