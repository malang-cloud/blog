import java.util.Scanner;

public class UserInputExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Nilai A: ");
        int a = scanner.nextInt();

        System.out.print("Nilai B: ");
        int b = scanner.nextInt();

        int c = a + b;

        System.out.println("Nilai A + B = " + c);

        scanner.close();
    }
}