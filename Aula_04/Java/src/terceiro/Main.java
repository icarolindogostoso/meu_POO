package terceiro;
import java.util.Scanner;

public class Main {
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
        System.out.println("Saldo: " + cb.getSaldo());

        System.out.print("Digite quando dinheiro voce quer sacar: ");
        valor = sc.nextDouble();

        cb.saque(valor);

        sc.close();
    }
}
