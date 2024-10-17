#include <iostream>

class Viagem{
    public:
    double distancia = 0;
    int tempo_hora = 0, tempo_minuto = 0;

    double calc_velocidade(){
        double tempo_total = tempo_hora + (tempo_minuto / 60.0);
        return distancia / tempo_total;
    }
};

int main(){
    Viagem v;

    std::cout << "Digite a distancia de uma viagem de km: ";
    std::cin >> v.distancia;

    std::cout << "Digite o numero de horas demora a viagem: ";
    std::cin >> v.tempo_hora;

    std::cout << "Digite o numero de minutos demora a viagem: ";
    std::cin >> v.tempo_minuto;

    std::cout << "Velocidade media da viagem = " << v.calc_velocidade() << " km/h" << std::endl;
    return 0;
}