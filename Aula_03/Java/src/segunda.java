import java.util.Scanner;

public class segunda {

    public static int maior(int a, int b, int c){
        int maior = a;
        if (b > maior){
            maior = b;
        } if (c > maior){
            maior = c;
        }
        return maior;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int mr = maior(a,b,c);

        System.out.println(mr);

        sc.close();
    }
}
