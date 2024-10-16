#include <iostream>

int maior(int a, int b, int c){
    int mr = a + ((a - b) * (-1 * (a < b)));
    return mr + ((mr - c) * (-1 * (mr < c)));
}

int main(){
    int a,b,c;
    std::cin >> a >> b >> c;
    int mr = maior(a,b,c);
    std::cout << mr << std::endl;
    return 0;
}