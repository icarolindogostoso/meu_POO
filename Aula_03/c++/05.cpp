#include <iostream>
#include <string>

std::string iniciais(std::string nome){
    std::string novo_nome;
    bool espaco = true;

    for (int i = 0; i < nome.size(); i++){
        char c = nome[i];
        if (c == ' '){
            espaco = true;
            novo_nome += c;
        } else if (espaco){
            novo_nome += toupper(c);
            espaco = false;
        } else{
            novo_nome += c;
        }
    }
    return novo_nome;
}

int main(){
    std::string nome;
    std::getline(std::cin, nome);
    std::string novo_nome = iniciais(nome);
    std::cout << novo_nome << std::endl;
    return 0;
}