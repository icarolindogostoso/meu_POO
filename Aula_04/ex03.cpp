#include <iostream>

class Triangulo{
    public: // controlar a visibilidade dos membros
    double b = 0, h = 0;
    double calc_area(){
        return b * h / 2;
        // return this->b * this->h / 2 tambem funciona (this-> equivale ao self do python)
    }
};

int main(){
    Triangulo x; // Triangulo x = new Triangulo();
    std::cout << x.b << " " << x.h << std::endl;
    std::cout << "Informe o valor da base: ";
    std::cin >> x.b;
    std::cout << "Informe o valor da altura: ";
    std::cin >> x.h;
    std::cout << "Area = " << x.calc_area() << std::endl;
    return 0;
}