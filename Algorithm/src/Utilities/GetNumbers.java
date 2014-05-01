package Utilities;

import java.util.Arrays;
import java.util.Random;

/**
 * Created by tom.wu on 29/04/2014.
 * Generate an array of random numbers by given max int
 */
public class GetNumbers {
    int[] numbers;
    int max;

    public GetNumbers(int max) {
        this.max = max;
        this.numbers = generateNumbers(this.max);
    }

    private int[] generateNumbers(int max) {
        Random rand = new Random();
        this.numbers = new int[max];
        for (int i = 0; i < max; i++) {
            this.numbers[i] = rand.nextInt(max);
        }

        return numbers;
    }

    public void setMax(int max) {
        this.max = max;
    }

    public int[] getNumbers() {
        return this.numbers;
    }

    public String toString() {
        return Arrays.toString(this.numbers);
    }
}
