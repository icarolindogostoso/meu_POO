#include <iostream>
#include <math.h>

class Circulo{
    private:
    double raio = 0;

    public: 
    void setRaio (double v) {
        if (v > 0){
            raio = v;
        } else {
            throw std::invalid_argument ("o raio do circulo nao pode ser um valor negativo");
        }
    }

    double getRaio () {
        return raio;
    }

    double calcArea () {
        return std::pow(raio, 2) * M_PI;
    }

    double calcCircunferencia () {
        return 2 * M_PI * raio;
    }
};

class UI{
    public:
    static void main(){
        Circulo x;

        double valor;
        std::cout << "Informe o valor do raio do circulo: ";
        std::cin >> valor;
        x.setRaio(valor);

        std::cout << "Raio = " << x.getRaio() << std::endl;
        std::cout << "Area = " << x.calcArea() << std::endl;
        std::cout << "Circunferencia = " << x.calcCircunferencia() << std::endl;
    }
};

int main(){
    UI::main();
    return 0;
}