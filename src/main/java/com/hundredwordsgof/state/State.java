package com.hundredwordsgof.state;

/**
 * The interface for encapsulating the behavior associated with a particular
 * state of the Context.
 *
 */
public interface State {

  void handle();
}
