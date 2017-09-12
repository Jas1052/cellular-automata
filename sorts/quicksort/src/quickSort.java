import java.util.InputMismatchException;
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

/**
 * Created by jas1052 on 6/24/17.
 **/
public class quickSort {
    private static void quickRecur() {
        return;
    }
    public static void main(String[] args) {
        int input = -1;
        Scanner reader = new Scanner(System.in);
        while (input < 1) {
            try {
                System.out.print("Input a valid number greater than 0: ");
                input = reader.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("That's not an integer.");
                reader.next();
            }
        }
        System.out.println("You chose: " + input);
        int[] numbers = new int[input];
        for (int i = 0; i < input; i++) {
            //populates numbers with random integers between 0 and 100
            numbers[i] = ThreadLocalRandom.current().nextInt(0, 100);
        }

        System.out.print("Unsorted: ");
        for(int number: numbers){
            System.out.print(number);
            System.out.print(" ");
        }

    }
}
