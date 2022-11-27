import numpy as np
import matplotlib.pyplot as plt 

n = 7
h = 0.286

# Abcissas
xn = [-1.000, -0.714, -0.428, -0.142, 0.144, 0.430, 0.716, 1.000]

# Função f(x) = x² + sin(6x)
def f(x):
    return x**2 + (np.sin(6*x))

# Cálculo dos f(x_i)
print("Valores de f(x):")
fi = []
for i in range (n+1):
    fi += [f(xn[i])]
    print(i," : ",fi[i])

# Função Spline - slide 120
def spline(x):
    if xn[0] <= x <= xn[1]:
        return (M[1] * (x-xn[0])**3 / (6*h)) + (fi[0] * (xn[1]-x)/h) + ((fi[1] - (M[1]*h**2)/6) * (x - xn[0])/h)
    if xn[1] <= x <= xn[2]:
        return (M[1] * (xn[2] - x)**3 / (6*h)) + (M[2] * (x-xn[1])**3 / (6*h)) + ((fi[1] - (M[1]*h**2)/6) * (xn[2]-x)/h) + ((fi[2] - (M[2]*h**2)/6) * (x - xn[1])/h)
    if xn[2] <= x <= xn[3]:
        return (M[2] * (xn[3] - x)**3 / (6*h)) + (M[3] * (x-xn[2])**3 / (6*h)) + ((fi[2] - (M[2]*h**2)/6) * (xn[3]-x)/h) + ((fi[3] - (M[3]*h**2)/6) * (x - xn[2])/h)
    if xn[3] <= x <= xn[4]:
        return (M[3] * (xn[4] - x)**3 / (6*h)) + (M[4] * (x-xn[3])**3 / (6*h)) + ((fi[3] - (M[3]*h**2)/6) * (xn[4]-x)/h) + ((fi[4] - (M[4]*h**2)/6) * (x - xn[3])/h)
    if xn[4] <= x <= xn[5]:
        return (M[4] * (xn[5] - x)**3 / (6*h)) + (M[5] * (x-xn[4])**3 / (6*h)) + ((fi[4] - (M[4]*h**2)/6) * (xn[5]-x)/h) + ((fi[5] - (M[5]*h**2)/6) * (x - xn[4])/h)
    if xn[5] <= x <= xn[6]:
        return (M[5] * (xn[6] - x)**3 / (6*h)) + (M[6] * (x-xn[5])**3 / (6*h)) + ((fi[5] - (M[5]*h**2)/6) * (xn[6]-x)/h) + ((fi[6] - (M[6]*h**2)/6) * (x - xn[5])/h)
    if xn[6] <= x <= xn[7]:
        return (M[6] * (xn[7] - x)**3 / (6*h)) + ((fi[6] - (M[6]*h**2)/6) * (xn[7]-x)/h) + (fi[7] * (x - xn[6])/h)


# Cálculo do sistema para encontrar os M's
A = [ [1, 0, 0, 0, 0, 0, 0, 0],
      [h/6, 2*h/3, h/6, 0, 0, 0, 0, 0],
      [0, h/6, 2*h/3, h/6, 0, 0, 0, 0],
      [0, 0, h/6, 2*h/3, h/6, 0, 0, 0],
      [0, 0, 0, h/6, 2*h/3, h/6, 0, 0],
      [0, 0, 0, 0, h/6, 2*h/3, h/6, 0],
      [0, 0, 0, 0, 0, h/6, 2*h/3, h/6],
      [0, 0, 0, 0, 0, 0, 0, 1]                                
    ]
B = [0]
for i in range (1,n):
    B += [ (fi[i+1]-fi[i])/h - (fi[i]-fi[i-1])/h ]
B += [0]

print("Valores de B:")
for i in range(n+1):
    print(i," : ", B[i])
M = np.linalg.solve(A,B)

print("Valores de M:")
for i in range(n+1):
    print(i, " : ", M[i])

S = np.vectorize(spline)

# Erros
def erro_spline(x):
    return abs(f(x)-S(x))

def f_der(x):
    return 1296 * (np.sin(6*x))

print("|f(0.1)-S(0.1)| <=",(5/384)*f_der(np.pi/12)*h**4)
print("|f(0.9)-S(0.9)| <=",(5/384)*f_der(np.pi/12)*h**4)


# Gráficos
x = np.arange(start = -1, stop = 1, step = 0.001)

y = S(x)
ff = f(x)
y2 = erro_spline(x)
plt.plot(x, ff, label = 'f(x)')
plt.plot(x, y, 'r-', label = 's(x)')
plt.plot(x, y2, 'g-', label= '|f(x) - S(x)|')

pontos = np.array([ [xn[i], fi[i]] for i in range(n+1) ])
xx, yy = pontos.T
plt.scatter(xx, yy, color='k')

plt.axis([-1,1,-1.0,2])
plt.grid()
plt.legend()
plt.show()
