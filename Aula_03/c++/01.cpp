#include <iostream>

int maior(int a, int b){
    return a + ((a - b) * (-1 * (a < b)));
}

int main(){
    int a,b;
    std::cin >> a >> b;
    int mr = maior(a,b);
    std::cout << mr << std::endl;
    return 0;
}