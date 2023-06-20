import java.util.Scanner;

public class UserInputExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // input
        System.out.print("Nilai A: ");
        int a = scanner.nextInt();

        System.out.print("Nilai B: ");
        int b = scanner.nextInt();

        // proses
        int c = a + b;

        // output
        System.out.println("Nilai A + B = " + c);

        scanner.close();
    }
}