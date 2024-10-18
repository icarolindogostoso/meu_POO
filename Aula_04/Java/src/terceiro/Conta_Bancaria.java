package terceiro;

public class Conta_Bancaria {
    private String nome;
    private int n_conta;
    private double saldo;

    public Conta_Bancaria(String nome, int n_conta){
        this.nome = nome;
        this.n_conta = n_conta;
    }

    public String getNome(){
        return nome;
    }

    public int getNConta(){
        return n_conta;
    }

    public double getSaldo(){
        return saldo;
    }

    public void deposito (double valor){
        saldo = saldo + valor;
        System.out.println("Deposito realizado com sucesso");
    }

    public void saque (double valor){
        if (valor > saldo){
            System.out.println("Saldo insuficiente");
        } else {
            saldo = saldo - valor;
            System.out.println("Saque realizado com sucesso");
        }
    }
}
