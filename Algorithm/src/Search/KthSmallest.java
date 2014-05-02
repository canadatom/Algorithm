package Search;

/**
 * Created by tom.wu on 01/05/2014.
 */
public class KthSmallest {
    int[] sortedCollection;
    int k;

    public KthSmallest(int[] sortedCollection, int k) {
        this.sortedCollection = sortedCollection;
        this.k = k;
    }

    public int findKthSmallest() {
        int count = 1;
        int n = sortedCollection.length;

        if (n == 1) {
            return -1;
        }

        for (int i = 0; i < n; i++) {
            if (i != 0 && (sortedCollection[i] != sortedCollection[i - 1])) {
                count++;
            }

            if (count == k) {
                return sortedCollection[i];
            }
        }

        // if unique numbers are less than k
        if (count < k) {
            return -1;
        }

        return -1;
    }
}
