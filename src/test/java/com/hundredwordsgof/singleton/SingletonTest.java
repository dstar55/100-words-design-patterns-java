package com.hundredwordsgof.singleton;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

import org.junit.Test;

/**
 * Test implementation of the Singleton pattern.
 */
public class SingletonTest {
	
	
	@Test
	public void testSingleton() {

		// invoke Singleton.getInstance() for first time, object must be created
		Singleton singleton = Singleton.getInstance();
		assertNotNull(singleton);
		
		// invoke Singleton.getInstance() for second time, we will get reference to the same object 
		Singleton secondSingleton = Singleton.getInstance();		
		assertEquals(singleton, secondSingleton);
		
	}		
}
