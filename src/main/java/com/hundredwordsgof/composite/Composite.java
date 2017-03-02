package com.hundredwordsgof.composite;

import java.util.ArrayList;
import java.util.List;

/**
 * 
 * Composite class defines behavior for components having children, stores child
 * components, implements child-related operations in the Component interface
 * 
 */
public class Composite extends Component {

  private List<Component> children = new ArrayList<Component>();

  public void operation() {

    for (Component component : children) {
      component.operation();
    }
  }

  public void add(Component component) {
    children.add(component);
  }

  public void remove(Component component) {
    children.remove(component);
  }

  public Component getChild(int index) {
    return children.get(index);
  }
}
