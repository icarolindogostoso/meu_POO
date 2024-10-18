import java.util.Scanner;

public class primeiro {

    public static class Circulo {
        double r = 0;

        Circulo (double r){
            this.r = r;
        }

        double Calc_area (){
            return 3.14 * r * r;
        }
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Digite o raio de um circulo: ");
        double valor = sc.nextDouble();

        Circulo c = new Circulo(valor);
        System.out.println("Area = " + (c.Calc_area()));

        sc.close();
    }
}
