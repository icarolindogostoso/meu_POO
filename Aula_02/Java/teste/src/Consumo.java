import java.util.Scanner;
import java.util.Locale;

public class Consumo {
    public static void main(String[] args){

        Locale.setDefault(Locale.US);

        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        double b = sc.nextDouble();

        double resultado = a/b;
        System.out.printf("%.3f Km/L", resultado);

        sc.close();
    }
}
