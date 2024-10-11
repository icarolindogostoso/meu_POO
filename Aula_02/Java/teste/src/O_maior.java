import java.util.Scanner;

public class O_maior {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        int numero1 = sc.nextInt();
        int numero2 = sc.nextInt();
        int numero3 = sc.nextInt();

        int maior = (numero1 + numero2 + Math.abs(numero1 - numero2))/2;
        maior = (maior + numero3 + Math.abs(maior - numero3))/2;

        System.out.println(maior + " eh o maior");

        sc.close();
    }
}
