#include <iostream>
#include <string>

int main(){
    std::string a;
    std::cin >> a;
    float b,c;
    std::cin >> b >> c;
    std::cout << "TOTAL = R$ " << (b+c*0.15) << std::endl;
    return 0;
}