package segundo;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite a distancia da viagem em km: ");
        double d = sc.nextDouble();

        System.out.print("Digite o numero de horas demora a viagem: ");
        int thora = sc.nextInt();

        System.out.print("Digite o numero de minutos demora a viagem: ");
        int tminuto = sc.nextInt();

        Viagem v = new Viagem(d,thora,tminuto);

        System.out.println("Velocidade media da viagem = " + (v.calcularVelocidade()) + " km/h");

        sc.close();
    }
}
