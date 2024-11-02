package qjava;
import java.util.Scanner;

class Conversor{
    int num;

    public Conversor (int num){
        setNum(num);
    }

    public void setNum(int valor){
        if (valor > 0){
            num = valor;
        } else {
            throw new IllegalArgumentException("Valor negativo");
        }
    }

    public int getNum () {
        return num;
    }

    public String binario (){
        int valor = num;
        if (valor == 0) {
            return "0";
        }

        StringBuilder binario = new StringBuilder();
        while (valor > 0) {
            int resto = valor % 2;
            binario.insert(0, resto); 
            valor = valor / 2;
        }

        return binario.toString();
    }

    public String toString (){
        return String.format("Convertendo o numero %d para binario", num);
    }
}

public class terceira {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.print("Informe um numero: ");
        int numero = sc.nextInt();

        Conversor x = new Conversor(numero);

        System.out.println(x.getNum());
        System.out.println(x.binario());
        System.out.println(x);

        sc.close();
    }
}
