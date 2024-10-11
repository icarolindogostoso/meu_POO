import java.util.Locale;
import java.util.Scanner;

public class Salario_com_Bonus {
    public static void main(String[] args){

        Locale.setDefault(Locale.US);

        Scanner scanner = new Scanner(System.in);
        String nome = scanner.nextLine();
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();

        System.out.println("TOTAL = R$"+(a+b*0.15));

        scanner.close();
    }
}
