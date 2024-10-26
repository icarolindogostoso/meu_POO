import java.util.Scanner;

class Viagem{
    private double distancia, tempo;

    public Viagem (){
        distancia = 0;
        tempo = 0;
    }

    public void setDistancia (double v) {
        if (v > 0){
            distancia = v;
        } else {
            throw new IllegalArgumentException ("a distancia nao pode ser negativa");
        }
    }

    public void setTempo (double v){
        if (v > 0){
            tempo = v;
        } else {
            throw new IllegalArgumentException ("o tempo nao pode ser negativo");
        }
    }

    public double getDistancia () {
        return distancia;
    }

    public double getTempo () {
        return tempo;
    }

    public double velocidadeMedia () {
        return distancia / tempo;
    }
}

public class segunda {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        Viagem x = new Viagem();

        System.out.print("Informe o valor da distancia da viagem: ");
        x.setDistancia(sc.nextDouble());
        System.out.print("Informe o valor do tempo da viagem: ");
        x.setTempo(sc.nextDouble());

        System.out.println("Distancia = " + (x.getDistancia()) + " Tempo = " + (x.getTempo()));
        System.out.println("Velocidade media = "+ (x.velocidadeMedia()));

        sc.close();
    }
}
