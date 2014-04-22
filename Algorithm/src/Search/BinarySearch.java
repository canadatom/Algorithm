package Search;

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

/**
 * This is a binary search in recursive
 * @author tom
 */
public class BinarySearch {

    public static void main(String[] args) {

        int number = 5;
        int min = 1;
        int max = 20;

        Random gen = new Random();
        int[] numbers = new int[max];
        for (int i = min; i < max; i++) {
            numbers[i] = gen.nextInt(max);
        }
        Arrays.sort(numbers);
        System.out.println(Arrays.toString(numbers));

        search(numbers, number, min, max - 1);

    }

    public static void search(int[] numbers, int number, int min, int max) {

        int mid = (min + max) / 2;
        System.out.println("middle point: " + mid);

        if (number > numbers[mid]) {
            search(numbers, number, mid + 1, max);
        } else if (number < numbers[mid]) {
            search(numbers, number, min, mid - 1);
        } else {
            System.out.printf("Found the %d at position %d\n", number, mid + 1);
        }
    }
}
