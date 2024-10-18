import java.util.Scanner;

public class quarto {
    public static class Entrada_Cinema{
        String dia = "";
        int hora = 0, minuto = 0;

        Entrada_Cinema (String dia, int hora, int minuto){
            this.dia = dia;
            this.hora = hora;
            this.minuto = minuto;
        }

        double entrada(){
            double valor = 16.00;
            if (hora >= 17 && hora < 24){
                valor = valor * 1.5;
            }
            if (dia.equalsIgnoreCase("Quarta")){
                return 8.00;
            }
            String dias[] = {"Sexta", "Sabado", "Domingo"};
            for (int i = 0; i < 3; i++){
                if (dias[i].equalsIgnoreCase(dia)){
                    return valor + 4;
                }
            }
            return valor;
        }

        double meia_entrada (){
            double valor = 8.00;
            if (hora >= 17 && hora < 24){
                valor = valor * 1.5;
            }
            if (dia.equalsIgnoreCase("Quarta")){
                return 8.00;
            }
            String dias[] = {"Sexta", "Sabado", "Domingo"};
            for (int i = 0; i < 3; i++){
                if (dias[i].equalsIgnoreCase(dia)){
                    return valor + 2;
                }
            }
            return valor;
        }
    }

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
        System.out.println("Valor meia-entrada: " + ec.meia_entrada());
    
        sc.close();
    }
}
