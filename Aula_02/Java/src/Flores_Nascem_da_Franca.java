import java.util.Scanner;

public class Flores_Nascem_da_Franca {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        while (true){String frase = sc.nextLine();
        
            String[] palavras = frase.toUpperCase().split(" ");
    
            if (palavras[0].equalsIgnoreCase("*")){
                break;
            }

            String palavra = palavras[0];
            int contador = 0;

            for (int i = 0; i < palavras.length; i++){
                String variavel = palavras[i];
                char letra = variavel.charAt(0);
                char ourtraletra = palavra.charAt(0);
                if (letra == ourtraletra){
                    contador++;
                }
            }

            if (contador == palavras.length){
                System.out.println("Y");
            } else {
                System.out.println("N");
            }
        }

        sc.close();
    }
}