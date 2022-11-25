#include <stdio.h>
#include <math.h>

#define LEN 7

double xn[LEN+1] = {-1, -0.714, -0.428, -0.142, 0.144, 0.430, 0.716, 1};
double m[LEN+1][LEN+1];

void clearMatrix();
void printMatrix();

double newton(double x);
double h(double x, int i);
void dividedDiff();
double f(double x); // funciona direito (feito com radianos)

int main() {
    clearMatrix();
    dividedDiff();

    double val1 = newton(0.1);
    double val2 = newton(0.9);

    /* dividedDiff Testes -> ainda por avaliar
    int parcelas = LEN;
    for (int i = 0; i <= LEN; i++) {
        for (int j = 0; j <= parcelas; j++) {
            printf("%lf\t", m[i][j]);
        }
        --parcelas;
        putchar('\n');
    }*/

    /* funcao h Testes -> Funcional
    double testVal = 1;
    for (int i = 0; i <= LEN; i++) {
        testVal *= h(0.1,i);
        printf("h(0.1, %d) -> %.3f\n", i, h(0.1, i));
        printf("testVal -> %lf\n-=-\n", testVal);
    }*/

    return 0;
}

void clearMatrix() {
    for (int i = 0; i <= LEN; i++) {
        for (int j = 0; j <= LEN; j++) {
            m[i][j] = 0;
        }
    }
}

void printMatrix() {
    for (int i = 0; i <= LEN; i++) {
        for (int j = 0; j <= LEN; j++) {
            printf("%lf\t", m[i][j]);
        }
        putchar('\n');
    }
}

// function values
double f(double x) {
    return x*x + sin(6*x);
}

// f(xi) -> f[x0, ... ,xn]
void dividedDiff() {
    // 1st row
    for (int i = 0; i <= LEN; i++) {
        m[0][i] = f(xn[i]);
    }

    for (int i = 1; i <= LEN; i++) {
        for (int j = 0; j <= LEN; j++) {
            m[i][j] = (m[i-1][j+1] - m[i-1][j]) / (xn[j] - xn[i+j]);
        }
    }
}

// (x - x0)(x - x1)...(x - xn)
double h(double x, int i) {
    return x - xn[i];
}

// f(x0) + h(0)f[x0, x1] + ... + h(n-1)f[x0, ... , xn]
double newton(double x) {
    double val = 0;
    double hval = 1;
    for (int i = 0; i <= LEN; i++) {
        val += hval*m[i][0];
        hval *= h(x, i);
    }
    return val;
}