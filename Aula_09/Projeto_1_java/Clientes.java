import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class Clientes {
    private static List<Cliente> objetos = new ArrayList<>();

    public static void inserir (Cliente obj){
        abrir();

        int id = 0;
        for (Cliente x : objetos){
            if (x.getId() > id){
                id = x.getId();
            }
        }
        obj.setId(id + 1);
        objetos.add(obj);
        salvar();
    }

    public static List<Cliente> listar(){
        abrir();
        return objetos;
    }

    public static Cliente listar_id (int id){
        abrir();
        for (Cliente x : objetos){
            if (x.getId() == id){
                return x;
            }
        }
        return null;
    }

    public static void atualizar(Cliente obj){
        Cliente x = listar_id(obj.getId());
        if (x != null){
            x.setNome(obj.getNome());
            x.setEmail(obj.getEmail());
            x.setFone(obj.getFone());
            salvar();
        }
    }

    public static void excluir(Cliente obj){
        Cliente x = listar_id(obj.getId());
        if (x != null){
            objetos.remove(x);
            salvar();
        }
    }

    public static void abrir(){
        objetos.clear();
        try {
            FileReader reader = new FileReader("clientes3.json");
            Type listType = new TypeToken<List<Cliente>>(){}.getType();
            objetos = new Gson().fromJson(reader, listType);
            reader.close();
        } catch (FileNotFoundException e){

        } catch (IOException e){
            e.printStackTrace();
        }
    }

    public static void salvar(){
        try {
            FileWriter writer = new FileWriter("clientes3.json");
            Gson gson = new Gson();
            gson.toJson(objetos, writer);
            writer.close();
        } catch (IOException e){
            e.printStackTrace();
        }
    }

}
