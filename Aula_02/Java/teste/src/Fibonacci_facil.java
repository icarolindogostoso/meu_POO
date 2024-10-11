import java.util.Scanner;

public class Fibonacci_facil {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int numero = sc.nextInt();

        if (numero == 1){
            int primeiro_valor = 0;
            System.out.println(primeiro_valor);
        } else {
            int primeiro_valor = 0, segundo_valor = 1;
            System.out.print(primeiro_valor + " " + segundo_valor + " ");
            for (int i = 0; i < numero-2; i++){
                int valor = primeiro_valor + segundo_valor;
                System.out.print(valor + " ");
                primeiro_valor = segundo_valor;
                segundo_valor = valor;
            }
        }

        sc.close();
    }
}
