#include <iostream>
#include <string>

class Conta_Bancaria{
    public:
    std::string nome = "";
    int n_conta = 0;
    double saldo = 0.0;

    void m_saldo(){
        std::cout << "Saldo atual: " << saldo << std::endl;
    }

    void deposito (double valor){
        saldo = saldo + valor;
        std::cout << "Deposito realizado com sucesso" << std::endl;
    }

    void saque (double valor){
        if (valor > saldo){
            std::cout << "Saldo insuficiente" << std::endl;
        } else {
            saldo = saldo - valor;
            std::cout << "Saque realizado com sucesso" << std::endl;
        }
    }
};

int main(){
    Conta_Bancaria cb;

    std::cout << "Digite seu nome: ";
    std::cin >> cb.nome;

    std::cout << "Digite o numero da sua conta: ";
    std::cin >> cb.n_conta;

    double valor;
    std::cout << "Digite quanto dinheiro voce quer depositar: ";
    std::cin >> valor;
    cb.deposito(valor);
    cb.m_saldo();

    std::cout << "Digite quanto dinheiro voce quer sacar: ";
    std::cin >> valor;
    cb.saque(valor);

    return 0;
}