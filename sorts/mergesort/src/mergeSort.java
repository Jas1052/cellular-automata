import java.lang.*;
import java.util.InputMismatchException;
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

/**
 * Created by jas1052 on 6/25/17.
*/

public class mergeSort {

    private static void merge(int [] numbers, int left, int mid, int right, int length){
        //sorts numbers in given indices
        int [] temp = new int[length];
        int i, left_end, num_elements, tmp_pos;

        left_end = (mid - 1);
        tmp_pos = left;
        num_elements = (right - left + 1);

        while ((left <= left_end) && (mid <= right)){
            if (numbers[left] <= numbers[mid])
                temp[tmp_pos++] = numbers[left++];
            else
                temp[tmp_pos++] = numbers[mid++];
        }

        while (left <= left_end)
            temp[tmp_pos++] = numbers[left++];

        while (mid <= right)
            temp[tmp_pos++] = numbers[mid++];

        for (i = 0; i < num_elements; i++){
            numbers[right] = temp[right];
            right--;
        }
    }

    // Recursive function that also calls merge

    private static void mergeRecurse(int [] numbers, int left, int right, int len){
        int mid;
        if (right > left){
            mid = (right + left) / 2;
            //Splits into two groups to recurse
            mergeRecurse(numbers, left, mid, len);
            mergeRecurse(numbers, (mid + 1), right, len);

            //sorts the given section
            merge(numbers, left, (mid+1), right, len);
        }
    }


    public static void main(String[] args){
        int input = -1;
        Scanner reader = new Scanner(System.in);
        while(input < 1) {
            try {
                System.out.print("Input a valid number greater than 0: ");
                input = reader.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("That's not an integer.");
                reader.next();
            }
        }
        System.out.println("Generating random array of length " + input + ". ");
        System.out.print("Unsorted: ");
        int[] numbers = new int[input];
        for(int i = 0; i < input; i++){
            //populates numbers with random integers between 0 and 100
            numbers[i] = ThreadLocalRandom.current().nextInt(0, 100);
            if(i == input-1)
                System.out.println(numbers[i]);
            else
                System.out.print(numbers[i] + ", ");
        }

        int len = numbers.length;
        mergeRecurse(numbers, 0, len - 1, len);

        System.out.print("Sorted: ");
        for(int i = 0; i < input-1; i++) {
            System.out.print(numbers[i] + ", ");
        }
        System.out.println(numbers[input-1]);
    }
}