import numpy as np
import matplotlib.pyplot as plt

n = 11

# Abcissas
xn = list(range(1,13))
fi = [8.6, 7.0, 6.4, 4.0, 2.8, 1.8, 1.8, 2.1, 3.2, 4.7, 6.2, 7.6]
h = 1

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
        return (M[6] * (xn[7] - x)**3 / (6*h)) + (M[7] * (x-xn[6])**3 / (6*h)) + ((fi[6] - (M[6]*h**2)/6) * (xn[7]-x)/h) + ((fi[7] - (M[7]*h**2)/6) * (x - xn[6])/h)
    if xn[7] <= x <= xn[8]:
        return (M[7] * (xn[8] - x)**3 / (6*h)) + (M[8] * (x-xn[7])**3 / (6*h)) + ((fi[7] - (M[7]*h**2)/6) * (xn[8]-x)/h) + ((fi[8] - (M[8]*h**2)/6) * (x - xn[7])/h)
    if xn[8] <= x <= xn[9]:
        return (M[8] * (xn[9] - x)**3 / (6*h)) + (M[9] * (x-xn[8])**3 / (6*h)) + ((fi[8] - (M[8]*h**2)/6) * (xn[9]-x)/h) + ((fi[9] - (M[9]*h**2)/6) * (x - xn[8])/h)
    if xn[9] <= x <= xn[10]:
        return (M[9] * (xn[10] - x)**3 / (6*h)) + (M[10] * (x-xn[9])**3 / (6*h)) + ((fi[9] - (M[9]*h**2)/6) * (xn[10]-x)/h) + ((fi[10] - (M[10]*h**2)/6) * (x - xn[9])/h)   
    if xn[10] <= x <= xn[11]:
        return (M[10] * (xn[11] - x)**3 / (6*h)) + ((fi[10] - (M[10]*h**2)/6) * (xn[11]-x)/h) + (fi[11] * (x - xn[10])/h) 

# Cálculo do sistema para encontrar os M's
A = [ [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [h/6, 2*h/3, h/6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, h/6, 2*h/3, h/6, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, h/6, 2*h/3, h/6, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, h/6, 2*h/3, h/6, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, h/6, 2*h/3, h/6, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, h/6, 2*h/3, h/6, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, h/6, 2*h/3, h/6, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, h/6, 2*h/3, h/6, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, h/6, 2*h/3, h/6, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, h/6, 2*h/3, h/6],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]                                
    ]

B = [0]
for i in range (1,n):
    B += [ (fi[i+1]-fi[i])/h - (fi[i]-fi[i-1])/h ]
B += [0]

M = np.linalg.solve(A,B)

S = np.vectorize(spline)

# Gráficos
x = np.arange(start = 1, stop = 12, step = 0.1)

y = S(x)
plt.plot(x, y, label = 's(x)')
# plt.plot(x, y, 'r-', label = 's(x)')

pontos = np.array([ [xn[i], fi[i]] for i in range(n+1) ])
xx, yy = pontos.T
plt.scatter(xx, yy, color='k')

plt.axis([1,12,-1.0,10])
plt.grid()
plt.legend()
plt.show()