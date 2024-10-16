import java.util.Scanner;

public class quarta {

    public static boolean aprovado(int nota1, int nota2){
        int media = (nota1 + nota2)/2;
        if (media < 60){
            return false;
        }
        return true;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int nota1 = sc.nextInt();
        int nota2 = sc.nextInt();
    
        boolean passou = aprovado(nota1,nota2);
        if (passou){
            System.out.println("Aprovado!");
        } else{
            System.out.println("Recuperacao!");
        }

        sc.close();
    }
}
