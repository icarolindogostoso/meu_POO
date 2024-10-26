#include <iostream>
#include <string>

class ContaBancaria {
    private:
    std::string nome;
    int numeroConta;
    double saldo;

    public: 
    void setNome (std::string v){
        if (v.length() > 1) {
            nome = v;
        } else {
            throw std::invalid_argument("Nome vazio");
        }
    }

    void setNumeroDaConta (int v){
        if (v > 1){
            numeroConta = v;
        } else {
            throw std::invalid_argument("Nome da conta nao pode ser um valor negativo");
        }
    }

    std::string getNome () {
        return nome;
    }

    int getNumeroDaConta () {
        return numeroConta;
    }

    double getSaldo (){
        return saldo;
    }

    void deposito (double v) {
        if (v > 1){
            saldo = saldo + v;
        } else {
            throw std::invalid_argument("Voce so pode depositar valores acima de 1");
        }
    }

    void saque (double v){
        if (v < saldo){
            saldo = saldo - v;
        } else {
            throw std::invalid_argument("Saldo insuficiente");
        }
    }
};

class UI{
    public:
    static void main(){
        ContaBancaria x;

        std::string n;
        int v;

        std::cout << "Informe seu nome: ";
        std::cin >> n;
        x.setNome(n);

        std::cout << "Informe o numero da sua conta: ";
        std::cin >> v;
        x.setNumeroDaConta(v);

        float z;
        std::cout << "Informe qual o valor do deposito: ";
        std::cin >> z;
        x.deposito(z);

        std::cout << "Informe o valor do saque: ";
        std::cin >> z;
        x.saque(z);

        std::cout << "Nome = " << x.getNome() << std::endl;
        std::cout << "Numero da conta = " << x.getNumeroDaConta() << std::endl;
        std::cout << "Saldo = " << x.getSaldo() << std::endl;
    }
};

int main(){
    UI::main();
    return 0;
}