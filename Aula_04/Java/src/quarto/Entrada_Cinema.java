package quarto;

public class Entrada_Cinema {
    private String dia;
    private int hora, minuto;

    public Entrada_Cinema(String dia, int hora, int minuto){
        this.dia = dia;
        this.hora = hora;
        this.minuto = minuto;
    }

    public int[] horario(){
        return new int[] {hora, minuto};
    }

    public double entrada(){
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

    public double meiaEntrada(){
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
