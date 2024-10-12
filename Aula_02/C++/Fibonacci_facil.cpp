#include <iostream>

int main(){
    int numero;
    std::cin >> numero;
    if (numero == 1){
        int primeiro_valor = 0;
        std::cout << primeiro_valor << std::endl;
    } else {
        int primeiro_valor = 0, segundo_valor = 1;
        std::cout << primeiro_valor << " " << segundo_valor << " ";
        for (int i = 0; i < numero-2; i++){
            int valor = primeiro_valor + segundo_valor;
            std::cout << valor << " ";
            primeiro_valor = segundo_valor;
            segundo_valor = valor;
        }
        std::cout << std::endl;
    }

    return 0;
}