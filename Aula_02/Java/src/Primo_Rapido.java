import java.util.Scanner;

public class Primo_Rapido {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int repeticoes = sc.nextInt();
        for (int i = 0; i < repeticoes; i++){
            int numero = sc.nextInt();
            int variavel = 0;
            for (int j = 2; j <= numero/2; j++){
                if (numero%j == 0){
                    variavel = 1;
                    break;
                }
            }
            if (variavel == 1){
                System.out.println("Not Prime");
            } else{
                System.out.println("Prime");
            }
        }
        sc.close();
    }
}
