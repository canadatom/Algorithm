package Sort;

import java.util.Arrays;
import java.util.Random;

import org.apache.commons.lang3.ArrayUtils;

/**
 * 
 * @author tom
 */
public class MergeSort {
	public static void main(String[] args) {
		int max = 10;
		Random gen = new Random();
		int[] numbers = new int[max];

		for (int i = 0; i < max; i++) {
			numbers[i] = gen.nextInt(max);
		}

		System.out.println(Arrays.toString(numbers));
		mergeSort(numbers);
		System.out.println(Arrays.toString(numbers));

	}

	public static void mergeSort(int[] numbers) {

		if (numbers.length > 1) {
			int midPoint = numbers.length / 2;

			int[] firstHalf = ArrayUtils.subarray(numbers, 0, midPoint);
			int[] secondHalf = ArrayUtils.subarray(numbers, midPoint,
					numbers.length);
			
			System.out.println("First Half: " + Arrays.toString(firstHalf));
			System.out.println("Second Half: " + Arrays.toString(secondHalf));
			
			mergeSort(firstHalf);
			mergeSort(secondHalf);

			merge(numbers, firstHalf, secondHalf);
		}
	}

	public static void merge(int[] result, int[] left, int[] right) {
		int i1 = 0; // index into left array
		int i2 = 0; // index into right array
		System.out.print("Merged from " + Arrays.toString(result));

		for (int i = 0; i < result.length; i++) {
			if (i2 >= right.length
					|| (i1 < left.length && left[i1] <= right[i2])) {
				result[i] = left[i1]; // take from left
				i1++;
			} else {
				result[i] = right[i2]; // take from right
				i2++;
			}
		}
		System.out.println(" to " + Arrays.toString(result));
	}
}
