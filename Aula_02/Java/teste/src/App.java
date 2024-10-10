import java.util.Scanner;

public class App {
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);
        String nome = scanner.nextLine();
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();

        System.out.println("TOTAL = R$"+(a+b*0.15));

        scanner.close();
    }
}
