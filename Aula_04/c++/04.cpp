#include <iostream>
#include <string>

class Entrada_Cinema{
    public:
    std::string dia = "";
    int hora = 0, minuto = 0;

    double entrada (){
        double valor = 16.00;
        if (hora >= 17 && hora < 24){
            valor = valor * 1.5;
        } 
        if (dia == "Quarta"){
            return 8.00;
        } 
        std::string dias [3] = {"Sexta", "Sabado", "Domingo"};
        for (int i = 0; i < 3; i++){
            if (dias[i] == dia){
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
        if (dia == "Quarta"){
            return 8.00;
        } 
        std::string dias [3] = {"Sexta", "Sabado", "Domingo"};
        for (int i = 0; i < 3; i++){
            if (dias[i] == dia){
                return valor + 2;
            }
        }
        return valor;
    }
};

int main(){
    Entrada_Cinema ec;

    std::cout << "Digite o dia da sua sessao: ";
    std::cin >> ec.dia;

    std::cout << "Digite o horario da sua sessao: ";
    std::cin >> ec.hora >> ec.minuto;

    std::cout << "Valor esquerda: " << ec.entrada() << std::endl;
    std::cout << "Valor meia-esquerda: " << ec.meia_entrada() << std::endl;

    return 0;
}