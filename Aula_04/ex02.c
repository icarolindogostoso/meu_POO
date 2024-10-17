#include <stdio.h>

typedef struct{
    double b,h;
} Triangulo;

double CalcArea (Triangulo t){
    return t.b * t.h / 2;
}

int main(){
    Triangulo x;
    x.b = 10;
    x.h = 20;
    printf("%lf",CalcArea(x));
    return 0;
}