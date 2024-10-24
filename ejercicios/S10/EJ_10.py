import numpy as np

# Importar la biblioteca de scikit-image
from skimage import io

# Crear una función para mostrar información sobre un array de NumPy
def numpy_info(arr):
 print("\nLa dimensión es:", arr.ndim)
 print("La forma es:", arr.shape)
 print("El tamaño es:", arr.size)

# Leer una imagen utilizando skimage
photo = io.imread("img/img_prueba.png")
# Mostrar información sobre la imagen
numpy_info(photo)
# Dimensiones de la imagen
print(f'Primera dimensión: {photo.shape[0]}, Segunda dimensión:{photo.shape[1]}, Tercera dimensión: {photo.shape[2]}')
print("RED: ", photo[0][0][0])
print("GREEN: ", photo[0][0][1])
print("BLUE: ", photo[0][0][2])
#RED: 255
#GREEN: 255
#BLUE: 255
#Mostrar la imagen
pic = io.imshow(photo)

#print (photo)
photo = io.imread("img/img_prueba.png")