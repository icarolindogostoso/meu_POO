package qjava;
import java.util.Scanner;

class Frete{
    private double distancia, peso;

    public Frete(double distancia, double peso){
        setDistancia(distancia);
        setPeso(peso);
    }

    public void setDistancia (double valor){
        if (valor > 0){
            distancia = valor;
        } else {
            throw new IllegalArgumentException ("Distancia negativa");
        }
    }

    public void setPeso (double valor){
        if (valor >= 0){
            peso = valor;
        } else {
            throw new IllegalArgumentException ("Peso invalido");
        }
    }

    public double getDistancia (){
        return distancia;
    }

    public double getPeso(){
        return peso;
    }

    public double calcFrete(){
        return peso / distancia * 100;
    }

    public String toString (){
        return String.format("Frete de distancia %.2f e peso %.2f", distancia, peso);
    }
}

public class segunda {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.print("Informe o peso: ");
        double peso = sc.nextDouble();
        System.out.print("Informe a distancia: ");
        double distancia = sc.nextDouble();

        Frete x = new Frete(distancia, peso);

        System.out.println(x);
        System.out.println("Frete = " + (x.calcFrete()));

        sc.close();
    }
}
