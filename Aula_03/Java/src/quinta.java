import java.util.Scanner;

public class quinta {

    public static String iniciais(String[] nome){
        String novo_nome = "";
        boolean novapalavra = true;

        for (int i = 0; i < nome.length(); i++){
            char c = nome.charAt(i);
            if (c == ' '){
                novapalavra = true;
                novo_nome += c;
            } else if (novapalavra){
                novo_nome += Character.toUpperCase(c);
                novapalavra = false;
            } else{
                novo_nome += c;
            }
        }
        return novo_nome;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String nome = sc.nextLine();
        String novonome = iniciais(nome);
        System.out.println(novonome);
        sc.close();
    }
}