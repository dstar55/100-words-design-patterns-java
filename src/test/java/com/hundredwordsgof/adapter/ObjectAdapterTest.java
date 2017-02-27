package com.hundredwordsgof.adapter;

import static org.junit.Assert.assertEquals;
import org.junit.Test;
import com.hundredwordsgof.adapter.object.Adaptee;
import com.hundredwordsgof.adapter.object.Adapter;
import com.hundredwordsgof.adapter.object.Target;

/**
 * Test implementation of the Adapter(object) pattern.
 */
public class ObjectAdapterTest {

  @Test
  public void testAdapter() {

    // creates Adaptee
    Adaptee adaptee = new Adaptee();

    // creates Adapter
    Target target = new Adapter(adaptee);

    assertEquals("specialRequest", target.request());
  }
}
