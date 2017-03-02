package com.hundredwordsgof.proxy;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

import org.junit.Test;

/**
 * Test implementation of the Proxy pattern.
 */
public class ProxyTest {

  @Test
  public void testProxy() {

    Proxy proxy = new Proxy();

    // realSubject is not created yet, therefore we expect null
    assertEquals(null, proxy.getRealSubject());

    proxy.doOperation();

    assertNotNull(proxy.getRealSubject());
  }
}
