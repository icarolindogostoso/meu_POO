import java.util.Scanner;
import java.util.Locale;

public class Distancia_entre_dois_pontos {
    public static void main(String[] args){

        Locale.setDefault(Locale.US);

        Scanner sc = new Scanner(System.in);

        double x1 = sc.nextDouble();
        double y1 = sc.nextDouble();
        double x2 = sc.nextDouble();
        double y2 = sc.nextDouble();

        double valor1 = (x2 - x1) * (x2 - x1);
        double valor2 = (y2 - y1) * (y2 - y1);

        System.out.printf("%.4f-'",(Math.sqrt(valor1+valor2)));

        sc.close();
    }
}
