package quarto;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o dia da sua sessao: ");
        String dia = sc.nextLine();

        System.out.print("Digite o horario da sua sessao: ");
        String[] tempo = sc.nextLine().split(":");

        int hora = Integer.parseInt(tempo[0]);
        int minuto = Integer.parseInt(tempo[1]);

        Entrada_Cinema ec = new Entrada_Cinema(dia, hora, minuto);

        System.out.println("Valor entrada: " + ec.entrada());
        System.out.println("Valor meia-entrada: " + ec.meiaEntrada());
    
        sc.close();
    }
}
