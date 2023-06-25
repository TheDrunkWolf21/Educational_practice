import numpy as np
import math

INPUT_DIM = 2
OUT_DIM = 1
H_DIM = 4

Z_vih = 0
Y_vih = 0

x = np.array([1, 0])

W1 = np.array([[ 0.2,  0.4, 0.7, 0.5 ],
               [ 0.3,  0.5, 0.6, 0.9 ]])

W2 = np.array([[ 0.2],
               [ 0.4],
               [ 0.6],
               [ 0.8]])

b1 =  np.array([ 1, 1, 1, 1 ])
b2 =  np.array([1, 1, 1, 1 ])

Y_prih = np.array([0, 0, 0, 0])

def predict(x):
    t1 = x @ W1 + b1
    h1 = t1
    return h1
 
print("Нейрони прихованого шару")
print(predict(x))
Y_prih = predict(x)

print("Результат активаційної функції")
for i in range(0,4):
    Y_prih[i] = round(1 / (1+math.exp(-Y_prih[i])),3)
print(Y_prih)


print("Загальний вихід нейромережі")
for i in range(0,4):
    Z_vih = Z_vih + Y_prih[i]*W2[i]
Z_vih += b2[i] 
print(Z_vih)

print("Вихід нейромережі")
Y_prih = round(1 / (1 + math.exp(-Z_vih)),3)
print(Y_prih)
