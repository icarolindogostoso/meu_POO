#include <iostream>

class Circulo{
    public:
    double r = 0;

    double calc_area(){
        return 3.14 * (r * r);
    }
};

int main(){
    Circulo c;
    std::cout << "Digite o raio de um circulo: ";
    std::cin >> c.r;
    std::cout << "Area = " << c.calc_area() << std::endl;
    return 0;
}