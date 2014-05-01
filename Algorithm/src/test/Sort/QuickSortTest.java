package test.Sort;

import Sort.QuickSort;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.assertArrayEquals;

/**
 * QuickSort Tester.
 *
 * @author Tom Wu
 * @version 1.0
 * @since <pre>May 1, 2014</pre>
 */
public class QuickSortTest {

    @Before
    public void before() throws Exception {
    }

    @After
    public void after() throws Exception {
    }

    /**
     * Method: quickSort(int[] collection, int i, int j)
     */
    @Test
    public void testQuickSort() throws Exception {
        int[] actual = {2, 3, 5, 7, 0, 9, 4, 1, 6, 8};
        int[] expected = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

        QuickSort q = new QuickSort(actual);
        q.quickSort(0, actual.length - 1);

        System.out.println(Arrays.toString(actual));
        assertArrayEquals(expected, actual);
    }


    /**
     * Method: partition(int[] collection, int left, int right)
     */
    @Test
    public void testPartition() throws Exception {
//TODO: Test goes here... 
/* 
try { 
   Method method = QuickSort.getClass().getMethod("partition", int[].class, int.class, int.class); 
   method.setAccessible(true); 
   method.invoke(<Object>, <Parameters>); 
} catch(NoSuchMethodException e) { 
} catch(IllegalAccessException e) { 
} catch(InvocationTargetException e) { 
} 
*/
    }

} 
