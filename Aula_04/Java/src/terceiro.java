import java.util.Scanner;

public class terceiro {
    public static class Conta_Bancaria{
        String nome = "";
        int n_conta = 0;
        double saldo = 0.0;

        Conta_Bancaria(String nome, int n_conta){
            this.nome = nome;
            this.n_conta = n_conta;
        }

        void m_saldo(){
            System.out.println("Saldo atual: " + (this.saldo));
        }

        void deposito (double valor){
            this.saldo = this.saldo + valor;
            System.out.println("Deposito realizado com sucesso");
        }

        void saque (double valor){
            if (valor > this.saldo){
                System.out.println("Saldo insuficiente");
            } else {
                this.saldo = this.saldo - valor;
                System.out.println("Saque realizado com sucesso");
            }
        }
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite seu nome: ");
        String nome = sc.nextLine();

        System.out.print("Digite o numero da sua conta: ");
        int n_conta = sc.nextInt();

        Conta_Bancaria cb = new Conta_Bancaria(nome, n_conta);

        System.out.print("Digite quanto dinherio voce quer depositar: ");
        double valor = sc.nextDouble();

        cb.deposito(valor);
        cb.m_saldo();

        System.out.print("Digite quando dinheiro voce quer sacar: ");
        valor = sc.nextDouble();

        cb.saque(valor);

        sc.close();
    }
}
