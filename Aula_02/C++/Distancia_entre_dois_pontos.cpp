#include <iostream>
#include <math.h>

int main(){
    double x1, y1, x2, y2;
    std::cin >> x1 >> y1;
    std::cin >> x2 >> y2;

    double valor1, valor2;
    valor1 = (x2 - x1) * (x2 - x1);
    valor2 = (y2 - y1) * (y2 - y1);

    std::cout << sqrt(valor1+valor2) << std::endl;

    return 0;
}