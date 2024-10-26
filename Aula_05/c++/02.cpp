#include <iostream>

class Viagem{
    private: 
    double distancia = 0, tempo = 0;

    public:
    void setDistancia (double v) {
        if (v > 0){
            distancia = v;
        } else {
            throw std::invalid_argument ("a distancia nao pode ser negativa");
        }
    }

    void setTempo (double v){
        if (v > 0){
            tempo = v;
        } else {
            throw std::invalid_argument ("o tempo nao pode ser negativo");
        }
    }

    double getDistancia () {
        return distancia;
    }

    double getTempo () {
        return tempo;
    }

    double velocidadeMedia () {
        return distancia / tempo;
    }
};

class UI{
    public:
    static void main(){
        Viagem x;

        double v;
        std::cout << "Informe o valor da distancia da viagem: ";
        std::cin >> v;
        x.setDistancia(v);

        std::cout << "Informe o valor do tempo da viagem: ";
        std::cin >> v;
        x.setTempo(v);

        std::cout << "Distancia = " << x.getDistancia() << " Tempo = " << x.getTempo() << std::endl;
        std::cout << "Velocidade media = " << x.velocidadeMedia() << std::endl;
    }
};

int main(){
    UI::main();
    return 0;
}