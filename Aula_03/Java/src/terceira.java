import java.util.Scanner;

public class terceira {

    public static String iniciais(String nome){
        String novo_nome = "";
        boolean novapalavra = true;

        for (int i = 0; i < nome.length(); i++){
            char c = nome.charAt(i);
            if (c == ' '){
                novapalavra = true;
            } else if (novapalavra){
                novo_nome += c;
                novo_nome += ' ';
                novapalavra = false;
            }
        }
        return novo_nome;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String nome = sc.nextLine();
        String novo_nome = iniciais(nome);
        System.out.println(novo_nome);
        sc.close();
    }
}
