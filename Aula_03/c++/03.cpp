#include <iostream>
#include <string>

std::string iniciais(std::string nome){
    std::string novo_nome;
    bool novapalavra = true;

    for (int i = 0; i < nome.size(); i++){
        char c = nome[i];
        if (c == ' '){
            novapalavra = true;
        } else if (novapalavra){
            novo_nome += c;
            novo_nome += ' ';
            novapalavra = false;
        }
    }
    return novo_nome;
}

int main(){
    std::string nome;
    std::getline(std::cin,nome);
    std::string novo_nome = iniciais(nome);
    std::cout << novo_nome << std::endl;
    return 0;
}