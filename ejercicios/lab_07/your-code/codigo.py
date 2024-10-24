import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Tu código aquí
# Datos: Admission_Predict.csv
df_csv = pd.read_csv("../Admission_Predict.csv")
# Mostrar conjunto de datos
print(df_csv)
print(df_csv.info())