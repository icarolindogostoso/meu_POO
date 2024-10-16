import java.util.Scanner;

public class primeira{

    public static int maior(int a, int b){
        int maior = a;
        if (b > maior){
            maior = b;
        }
        return maior;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int mr = maior(a,b);

        System.out.println(mr);

        sc.close();
    }
}
