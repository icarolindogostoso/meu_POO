import java.util.Scanner;

class ContaBancaria {
    private String nome;
    private int numeroConta;
    private double saldo;

    public ContaBancaria () {
        nome = "";
        numeroConta = 0;
        saldo = 0;
    }

    public void setNome (String v){
        if (v.length() > 1) {
            nome = v;
        } else {
            throw new IllegalArgumentException("Nome vazio");
        }
    }

    public void setNumeroDaConta (int v){
        if (v > 1){
            numeroConta = v;
        } else {
            throw new IllegalArgumentException("Nome da conta nao pode ser um valor negativo");
        }
    }

    public String getNome () {
        return nome;
    }

    public int getNumeroDaConta () {
        return numeroConta;
    }

    public double getSaldo (){
        return saldo;
    }

    public void deposito (double v) {
        if (v > 1){
            saldo = saldo + v;
        } else {
            throw new IllegalArgumentException ("Voce so pode depositar valores acima de 1");
        }
    }

    public void saque (double v){
        if (v < saldo){
            saldo = saldo - v;
        } else {
            throw new IllegalArgumentException ("Saldo insuficiente");
        }
    }
}

public class terceira {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        ContaBancaria x = new ContaBancaria();

        System.out.print("Informe seu nome: ");
        x.setNome(sc.nextLine());
        System.out.print("Informe o numero da sua conta: ");
        x.setNumeroDaConta(sc.nextInt());

        System.out.print("Informe qual o valor do deposito: ");
        x.deposito(sc.nextDouble());
        System.out.print("Informe o valor do saque: ");
        x.saque(sc.nextDouble());

        System.out.println("Nome = " + (x.getNome()));
        System.out.println("Numero da conta = " + (x.getNumeroDaConta()));
        System.out.println("Saldo = " + (x.getSaldo()));

        sc.close();
    }
}
