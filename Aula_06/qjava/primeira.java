package qjava;
import java.util.Scanner;

class Retangulo{
    private double base, altura;

    public Retangulo (double base, double altura){
        setBase(base);
        setAltura(altura);
    }

    public void setAltura (double valor){
        if (valor > 0){
            altura = valor;
        } else {
            throw new IllegalArgumentException("altura negativa");
        }
    }

    public void setBase (double valor){
        if (valor > 0){
            base = valor;
        } else {
            throw new IllegalArgumentException("base negativa");
        }
    }

    public double getAltura (){
        return altura;
    }

    public double getBase (){
        return base;
    }

    public double calcArea () {
        return base * altura;
    }

    public double caclDiagonal () {
        return Math.sqrt(Math.pow(altura, 2) + Math.pow(base, 2));
    }

    public String toString(){
        return String.format("Eu sou um retangulo de base %.2f e altura %.2f", base, altura);
    }
}

public class primeira {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.print("Informe o valor da base do retangulo: ");
        double base = sc.nextDouble();
        System.out.print("Informe o valor da altura do retangulo: ");
        double altura = sc.nextDouble();

        Retangulo x = new Retangulo(base, altura);

        System.out.println(x);
        System.out.println("Area = " + (x.calcArea()));
        System.out.println("Diagonal = " + (x.caclDiagonal()));

        sc.close();
    }
}
