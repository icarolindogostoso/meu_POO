import java.util.Scanner;

class Circulo{
    private double raio;

    public Circulo () {
        raio = 0;
    }

    public void setRaio (double v) {
        if (v > 0){
            raio = v;
        } else {
            throw new IllegalArgumentException ("o raio do circulo nao pode ser um valor negativo");
        }
    }

    public double getRaio () {
        return raio;
    }

    public double calcArea () {
        return raio * raio * Math.PI;
    }

    public double calcCircunferencia () {
        return 2 * Math.PI * raio;
    }
}

public class primeira{
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);

        Circulo x = new Circulo();

        System.out.print("Informe o valor do raio do circulo: ");
        x.setRaio(sc.nextDouble());

        System.out.println("Raio = " + (x.getRaio()));
        System.out.printf("Area = %.2f%n" , (x.calcArea()));
        System.out.printf("Circunferencia = %.2f%n" , (x.calcCircunferencia()));

        sc.close();
    }
}