package com.hundredwordsgof.adapter;

import static org.junit.Assert.*;
import org.junit.Test;
import com.hundredwordsgof.adapter.clazz.Adapter;
import com.hundredwordsgof.adapter.clazz.Target;

/**
 * Test implementation of the Adapter(object) pattern.
 */
public class ClazzAdapterTest {

  @Test
  public void testAdapter() {

    // creates Adapter
    Target target = new Adapter();

    assertEquals("specialRequest", target.request());
  }
}
