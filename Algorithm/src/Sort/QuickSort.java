package Sort;

/**
 * @author tom
 */
public class QuickSort {
    int[] collection;

    public QuickSort(int[] collection) {
        this.collection = collection;
    }

    public void quickSort(int left, int right) {

        // base case when right >=left
        if (left < right) {
            int iPivot = partition(left, right);
            quickSort(left, iPivot - 1);
            quickSort(iPivot + 1, right);
        }

    }

    private int partition(int left, int right) {
        // take pivot from right
        int pivot = collection[right];

        // start index from left
        int pIndex = left;

        for (int i = left; i < right; i++) {
            if (collection[i] <= pivot) {
                swap(i, pIndex);
                pIndex++;
            }
        }

        swap(pIndex, right);
        return pIndex;
    }

    private void swap(int i, int j) {
        int tmp = collection[i];
        collection[i] = collection[j];
        collection[j] = tmp;
    }
}
