package com.hundredwordsgof.visitor;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Holds objects in structure. Provides interface to allow visitors to visit its
 * elements.
 * 
 */
public class ObjectStructure {

  private List<Element> children = new ArrayList<Element>();

  public void add(Element element) {
    children.add(element);
  }

  public void remove(Element element) {
    children.remove(element);
  }

  public Element getChild(int index) {
    return children.get(index);
  }

  public void acceptAll(Visitor visitor) {
    for (Iterator iterator = children.iterator(); iterator.hasNext();) {
      Element element = (Element) iterator.next();
      element.accept(visitor);
    }
  }
}
