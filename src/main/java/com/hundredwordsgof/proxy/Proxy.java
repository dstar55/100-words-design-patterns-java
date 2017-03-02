package com.hundredwordsgof.proxy;

/**
 * Proxy class keep reference on a real subject, define interface which
 * represents Subject, so he can: - act as a surogate - controll acces to real
 * subject - can be responisble for creation and maintainence of the real
 * subject
 * 
 */
public class Proxy implements Subject {

  private RealSubject realSubject;

  public void doOperation() {
    this.realSubject = new RealSubject();
    this.realSubject.doOperation();
  }

  public RealSubject getRealSubject() {
    return realSubject;
  }
}
