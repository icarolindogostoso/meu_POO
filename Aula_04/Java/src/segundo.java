import java.util.Scanner;

public class segundo {
    public static class Viagem{
        double distancia = 0;
        int tempo_hora = 0, tempo_minuto = 0;

        Viagem (double distancia,int tempo_hora,int tempo_minuto){
            this.distancia = distancia;
            this.tempo_hora = tempo_hora;
            this.tempo_minuto = tempo_minuto;
        }

        double calc_velocidade(){
            double tempo_total = this.tempo_hora + (this.tempo_minuto / 60.0);
            return this.distancia / tempo_total;
        }
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite a distancia da viagem em km: ");
        double d = sc.nextDouble();

        System.out.print("Digite o numero de horas demora a viagem: ");
        int thora = sc.nextInt();

        System.out.print("Digite o numero de minutos demora a viagem: ");
        int tminuto = sc.nextInt();

        Viagem v = new Viagem(d,thora,tminuto);

        System.out.println("Velocidade media da viagem = " + (v.calc_velocidade()) + " km/h");

        sc.close();
    }
}
