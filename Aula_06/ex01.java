import java.util.Scanner;

class Triangulo{
    private double b, h;

    public Triangulo (){
        b = 0;
        h = 0;        
    }

    public void setBase (double v){
        if (v > 0){
            b = v;
        } else {
            throw new IllegalArgumentException("a base do triangulo não pode ser negativa");
        }
    }

    public void setAltura (double v){
        if (v > 0){
            h = v;
        } else {
            throw new IllegalArgumentException("a altura do triangulo não pode ser negativa");
        }
    }

    public double getBase (){
        return b;
    }

    public double getAltura (){
        return h;
    }

    public double calcArea(){
        return b * h / 2;
    }

    public String toString(){ // substitui o __str__ do python
        return String.format("Eu sou um triangulo de base %.2f e altura %.2f", b, h);
    }
}

public class ex01{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        Triangulo x = new Triangulo();

        System.out.print("Informe o valor da base do triangulo: ");
        x.setBase(sc.nextDouble());

        System.out.print("Informe o valor da altura do triangulo: ");
        x.setAltura(sc.nextDouble());

        System.out.println("Base = " + (x.getBase()) + " Altura = " + (x.getAltura()));

        System.out.println("Area = " + (x.calcArea()));

        System.out.println(x);

        sc.close();
    }
}