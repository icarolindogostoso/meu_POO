import java.util.Scanner;
import java.util.Locale;

public class Validacao_da_nota {
    public static void main(String[] args){

        Locale.setDefault(Locale.US);

        Scanner sc = new Scanner(System.in);
        double soma = 0; 
        int quantidade = 0;
        while (quantidade != 2){

            double numero = sc.nextDouble();

            if (numero < 0 || numero > 10){
                System.out.println("nota invalida");
            } else{
                soma = soma + numero;
                quantidade = quantidade + 1;
            }
        }
        double media = soma/quantidade;

        System.out.printf("media = %.2f",media);

        sc.close();
    }
}
