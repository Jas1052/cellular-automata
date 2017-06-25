import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * Created by jas1052 on 6/24/17.
 */
public class quickSort {
    public static void main(String[] args){
        int input;
        Scanner reader = new Scanner(System.in);
        try {
            System.out.println("Input a number");
            input = reader.nextInt();
        }
        catch(InputMismatchException e){
            System.out.println("That's not an int. Enter an integer greater than 0");
            input = reader.nextInt();
        }
        System.out.println("You chose: " + input);
    }
}
