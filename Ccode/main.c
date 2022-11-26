#include <stdio.h>
#include <math.h>

#define MAX 8

double xn[MAX] = { 0 };
double m[MAX][MAX];
int len;

void clearMatrix();
void printMatrix();

double newton(double x);
double h(double x, int i);
void dividedDiff();
double f(double x); // funciona direito (feito com radianos)

int main() {
    // definir pontos xi
    for (int i = 0; i < MAX; i++) {
        scanf("%lf", &xn[i]);
    }

    dividedDiff();

    printMatrix();
    /*
    // geracao de g(x) em falta (200 pontos)
    double gap = 0.01;
    //printf("Gap -> %lf\n", gap);
    double x = -1;
    printf("X\tY\n");
    for (int i = 0; i < 200; i++) {
        if (x > 1) x = 1;
        
        printf("%lf\t%lf\n", x, newton(x));
        x += gap;
        if (x == 1) break;
    }*/

    return 0;
}

void clearMatrix() {
    for (int i = 0; i <= MAX; i++) {
        for (int j = 0; j <= MAX; j++) {
            m[i][j] = 0;
        }
    }
}

void printMatrix() {
    int limit = MAX;
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < limit; j++) {
            printf("%lf\t", m[i][j]);
        }
        --limit;
        putchar('\n');
    }
}

// function values
double f(double x) {
    return x*x + sin(6*x);
}

// f(xi) -> f[x0, ... ,xn]
void dividedDiff() {
    // preenchimento da 1º linha com valores f(xi)
    for (int i = 0; i <= MAX; i++) {
        m[0][i] = f(xn[i]);
    }

    // calculo das restantes diferencas
    int limite = MAX-1; // evitar calculos impossiveis
    for (int i = 1; i < MAX; i++) {
        for (int j = 0; j < limite; j++) {
            m[i][j] = (m[i-1][j+1] - m[i-1][j]) / (xn[i+j] - xn[j]);
        }
        --limite;
    }
}

// (x - x0)(x - x1)...(x - xn)
double h(double x, int i) {
    return x - xn[i];
}

// f(x0) + h(0)f[x0, x1] + ... + h(n-1)f[x0, ... , xn]
double newton(double x) {
    // valor final aproximado
    double val = 0;

    // var que guarda (x-x0)(x-x1)...(x-xn), etc
    double hval = 1;

    // aplicacao da definicao do metodo de Newton
    for (int i = 0; i <= MAX; i++) {
        val += hval*m[i][0];
        hval *= h(x, i);
    }
    
    return val;
}