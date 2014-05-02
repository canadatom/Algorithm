package test.Search;

import Search.KthSmallest;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

/**
 * KthSmallest Tester.
 *
 * @author <Authors name>
 * @version 1.0
 * @since <pre>May 1, 2014</pre>
 */
public class KthSmallestTest {

    @Before
    public void before() throws Exception {
    }

    @After
    public void after() throws Exception {
    }

    /**
     * Method: findKthSmallest()
     */
    @Test
    public void testFindKthSmallest() throws Exception {
        int[] a = {0, 1, 1, 2, 2, 3, 3, 3, 3, 6, 7, 8, 9};
        int expected = 2;
        int k = 3;
        KthSmallest ks = new KthSmallest(a, k);
        int actual = ks.findKthSmallest();

        assertEquals(expected, actual);

    }


} 
