import java.util.List;
import java.util.Scanner;

public class Ui{
    static Scanner scanner = new Scanner(System.in);

    public static int menu(){
        System.out.println("Cadastro de Clientes");
        System.out.println("1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir, 9 - Fim");
        System.out.print("Informe uma opção: ");
        int op = scanner.nextInt();
        scanner.nextLine();
        return op;
    }

    public static void main(String[] args){
        int op = 0;
        while (op != 9){
            op = menu();
            switch (op){
                case 1:
                    inserirCliente();
                    break;
                case 2:
                    listarClientes();
                    break;
                case 3:
                    atualizarCliente();
                    break;
                case 4:
                    excluirCliente();
                    break;
                case 9:
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Opção ivalida. Tente novamente.");
            }
        }
    }

    public static void inserirCliente(){
        System.out.print("Informe o nome: ");
        String nome = scanner.nextLine();

        System.out.print("Informe o email: ");
        String email = scanner.nextLine();

        System.out.print("Informe o fone: ");
        String fone = scanner.nextLine();

        Cliente cliente = new Cliente(0, nome, email, fone);

        Clientes.inserir(cliente);
    }

    public static void listarClientes(){
        List<Cliente> clientes = Clientes.listar();

        if (clientes.isEmpty()){
            System.out.println("Nenhum cliente cadastrado.");
        } else {
            for (Cliente cliente : clientes){
                System.out.println(cliente);
            }
        }
    }

    public static void atualizarCliente(){
        listarClientes();

        System.out.print("Informe o id do cliente a ser alterado: ");
        int id = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Informe o novo nome: ");
        String nome = scanner.nextLine();

        System.out.print("Informe o novo email: ");
        String email = scanner.nextLine();

        System.out.print("Informe o novo fone: ");
        String fone = scanner.nextLine();

        Cliente cliente = new Cliente(id, nome, email, fone);

        Clientes.atualizar(cliente);
    }

    public static void excluirCliente(){
        listarClientes();

        System.out.print("Informe o id do cliente a ser excluido: ");
        int id = scanner.nextInt();

        Cliente cliente = new Cliente(id, "", "", "");

        Clientes.excluir(cliente);
    }
}