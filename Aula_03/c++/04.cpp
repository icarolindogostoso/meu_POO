#include <iostream>

bool aprovado (int nota1, int nota2){
    int media = (nota1 + nota2)/2;
    if (media < 60){
        return 0;
    }
    return 1;
}

int main(){
    int nota1, nota2;
    std::cin >> nota1 >> nota2;
    bool passou = aprovado(nota1,nota2);
    if (passou){
        std::cout << "Aprovado!\n";
    } else{
        std::cout << "Recuperacao!\n";
    }
    return 0;
}