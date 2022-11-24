#include <stdio.h>
#include <math.h>

#define LEN 7

double xn[LEN+1] = {-1, -0.714, -0.428, -0.142, 0.144, 0.430, 0.716, 1};

double lagrange(double x);
double l(double x, int i);
double f(double x);

int main() {
    return 0;
}

double f(double x) {
    return pow(x,2) + sin(6*x);
}

double l(double x, int i) {
    double num = 1, denom = 1;
    for (int j = 0; j < LEN; j++) {
        if (j != i) {
            num *= x - xn[j];
            denom *= xn[i] - xn[j];
        }
    }

    return num / denom;
}

double lagrange(double x) {
    double val = 0;
    for (int i = 0; i < LEN; i++) {
        val += l(x,i) * f(xn[i]);
    }
    return val;
}