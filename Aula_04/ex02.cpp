#include <iostream>

int main(){
    int x = 10;
    int* y = &x; // vai guardar em y o endereco de x

    std::cout << x << std::endl; // vai mostrar valor guardado em x -> 10
    std::cout << &x << std::endl; // vai mostrar endereço de x
    // std::cout << *x << std::endl; // nao funciona por x nao guardar um endereco

    std::cout << y << std::endl; // vai mostrar valor guardado em y -> endereco de x
    std::cout << &y << std::endl; // vai mostrar endereço de y
    std::cout << *y << std::endl; // vai mostrar o valor que está guardada no endereço guardado na variavel y

    y = new int();
    std::cout << y << std::endl; // vai mostrar o endereco de y
    std::cout << &y << std::endl; // vai mostrar o endereco de y
    std::cout << *y << std::endl; // vai mostrar o valor que está guardada no endereço guardado na variavel y

    *y = 20;
    std::cout << y << std::endl;
    std::cout << &y << std::endl;
    std::cout << *y << std::endl;

    delete y;

    return 0;
}