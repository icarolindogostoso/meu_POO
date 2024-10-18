package segundo;

public class Viagem {
    private double distancia;
    private int tempo_hora, tempo_minuto;

    public Viagem (double distancia, int tempo_hora, int tempo_minuto){
        this.distancia = distancia;
        this.tempo_hora = tempo_hora;
        this.tempo_minuto = tempo_minuto;
    }

    public double calcularVelocidade(){
        double tempo_total = tempo_hora + (tempo_minuto / 60.0);
        return distancia / tempo_total;
    }
}
