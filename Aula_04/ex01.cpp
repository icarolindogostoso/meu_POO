#include <iostream>

int area_triangulo(int base, int altura){
    return (base*altura)/2;
}

int main(){
    int base,altura;
    std::cin >> base >> altura;
    std::cout << area_triangulo(base,altura) << std::endl;
    return 0;
}