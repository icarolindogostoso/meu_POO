import java.util.Scanner;

public class Pedagio {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        int l = sc.nextInt();
        int d = sc.nextInt();
        int k = sc.nextInt();
        int p = sc.nextInt();

        int pedagio = l /d;
        int pagamento = l*k+pedagio*p;

        System.out.println(pagamento);

        sc.close();
    }
}
