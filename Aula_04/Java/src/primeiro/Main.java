package primeiro;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Digite o raio de um circulo: ");
        double valor = sc.nextDouble();

        Circulo c = new Circulo(valor);
        System.out.println("Area = " + (c.calcularArea()));

        sc.close();
    }
}
