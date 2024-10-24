import io
import numpy as np
exchange_rates = np.array([1.10, 1.12, 1.15, 1.11, 1.14, 1.13, 1.10, 1.12, 
                            1.13, 1.11, 1.15, 1.16, 1.18, 1.20, 1.19, 1.17, 
                            1.16, 1.14, 1.12, 1.13, 1.11, 1.10, 1.12, 1.13, 
                            1.14, 1.15, 1.11, 1.10, 1.08, 1.09, 1.11, 1.13])

dates = np.array(['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', 
                  '2023-10-05', '2023-10-06', '2023-10-07', '2023-10-08', 
                  '2023-10-09', '2023-10-10', '2023-10-11', '2023-10-12', 
                  '2023-10-13', '2023-10-14', '2023-10-15', '2023-10-16', 
                  '2023-10-17', '2023-10-18', '2023-10-19', '2023-10-20', 
                  '2023-10-21', '2023-10-22', '2023-10-23', '2023-10-24', 
                  '2023-10-25', '2023-10-26', '2023-10-27', '2023-10-28', 
                  '2023-10-29', '2023-10-30', '2023-10-31'])
trade_volumes = np.array([1000, 1200, 1100, 1300, 1500, 1400, 1600, 1700, 
                          1800, 1900, 2100, 2200, 2000, 2300, 2400, 2500, 
                          2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 
                          3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 
                          4200])

external_variable = np.array([102, 103, 101, 104, 105, 106, 107, 108, 
                              109, 110, 111, 112, 113, 114, 115, 116, 
                              117, 118, 119, 120, 121, 122, 123, 124, 
                              125, 126, 127, 128, 129, 130, 131, 132, 
                              133])

exchange_rates =exchange_rates[:31]
a=sum(exchange_rates)
c=len(exchange_rates)
print(a)
print(c)
print(a/c)
print(np.mean(exchange_rates))
print(len(dates))
print(len(trade_volumes))
print(len(external_variable))

from typing import List, Tuple
from functools import reduce

tbl=[]
for (y,z,t) in zip(exchange_rates,trade_volumes,external_variable):
    tbl.append([y,z,t])

tblnp =  np.array(tbl)


print(tblnp)
print(len(tblnp))
vFMax =(lambda x,y: x if x[1] > y[1] else y)
arr=tbl
vMaximo =reduce(vFMax,arr)
print(vMaximo)
vRes = [t[1] for t in arr]
#
vRes = (lambda x,y: x if x > y else y, [t[1] for t in arr],0)
print(vRes)
# Extraer la columna 2 (índice 1)
columna_2 = [t[1] for t in arr]

# Usar 'reduce' para encontrar el máximo
vRes = reduce(lambda x, y: x if x > y else y, columna_2)

print(vRes)  # Debería imprimir 20, que es el máximo en la segunda columna
columna_2 = [t[1] for t in arr]

# Usar 'reduce' para encontrar el máximo
vRes = reduce(lambda x, y: x if x > y else y, [t[1] for t in arr])

print(vRes)  # Debería imprimir 20, que es el máximo en la segunda columna
min_item = min(arr, key=lambda x: x[1]) 
print(tblnp)
print(type(tblnp))
print(type(trade_volumes))
print(tblnp[:,0])
print(tblnp[:,1])
print(tblnp[:,2])
print(tblnp[1,:])
min_item2 =  np.min(tblnp[:,0])
max_item2 =  np.max(tblnp[:,0])

print(min_item)
#print(min_item2)
#vFSum = (lambda x,y: x[3]+y[3])
#total_Volumen = reduce(vFSum,arr)
#print(total_Volumen)
vTotalC = reduce(lambda x,y: x+y, [z[2] for z in arr])
print(vTotalC)



# Definir una matriz 3x2
matrix = np.array([[1, 2], [3, 4], [5, 6]])

print(matrix)
print('\n')
print(matrix[:1])
print('\n')
print(matrix[1:])
print('\n')



matrix = np.array([1, 2, 3, 4, 5, 6]).reshape(3, 2)

print(matrix)
print('\n')
print(matrix[:,1])
print('\n')
print(matrix[1,:])
print('\n')
