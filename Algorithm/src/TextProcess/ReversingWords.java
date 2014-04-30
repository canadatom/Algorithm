package TextProcess;

import java.util.StringTokenizer;

public class ReversingWords {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String input = "Write a function to reverse the order of words in a string in place";

        // Step 1 reverse first to last char
        String newInput = reverseChar(input);
        System.out.println(newInput);

        // Step 2 reverse char in each word delimited by space
        StringTokenizer st = new StringTokenizer(newInput, " ");
        String finalInput = "";
        while (st.hasMoreTokens()) {
            if (finalInput.equals(null)) {
                finalInput = reverseChar(st.nextToken());
            } else {
                finalInput = finalInput + " " + reverseChar(st.nextToken());
            }
        }
        System.out.println(finalInput);

	}

    public static String reverseChar(String input) {
        StringBuilder newInput = new StringBuilder(input);
        int i = 0;  // beginning
        int j = input.length() - 1; // end
        for (i = 0; i < input.length(); i++) {
            newInput.setCharAt(i, input.charAt(j));
            j--;
        }

        return newInput.toString();
    }

}
