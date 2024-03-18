# -*- coding: utf-8 -*-
"""
main.py -

Descripción:
estrategias de tratamiento de valores numéricos no disponibles

librerías externas: pandas, numpy y sklearn.

Autor: Bieito Sousa Barreiro
Versión de Python: 3.8.18
"""

# Importa las funciones definidas en utils
from utils.dataPrepare import DataPrepare
from utils.dataProcessKNNImputer import DataProcessKNNImputer
from utils.dataProcessSimpleImputer import DataProcessSimpleImputer

isMyEnv = False

# Ruta del archivo CSV con los datos
archivo_datos = (
    "ceia-pia/pia-task/pia03-task/data/housing.csv" if isMyEnv else "./data/housing.csv"
)

# Cargar y procesar los datos
housing, null_rows_idx = DataPrepare(archivo_datos)

# Ejecutar SimpleImputer
housing_imputed_simple = DataProcessSimpleImputer(housing)

# Ejecutar KNNImputer
housing_imputed_knn = DataProcessKNNImputer(housing)

# Mostrar los primeros registros del DataFrame con valores nulos imputados
print("-" * 90)
print("- \t\tMostramos los primeros registros del DataFrame transpuesto\t\t -")
print("-" * 90)
print(housing.head().T)  # Mostramos los primeros registros del DataFrame transpuesto

# Mostrar los primeros registros del DataFrame con valores nulos imputados usando SimpleImputer
print("-" * 90)
print("- \t\tEjemplo de valores nulos imputados con SimpleImputer:\t\t -")
print("-" * 90)
print(housing_imputed_simple.loc[null_rows_idx].head())

# Mostrar los primeros registros del DataFrame con valores nulos imputados usando KNNImputer
print("-" * 90)
print("- \t\tEjemplo de valores nulos imputados con KNNImputer:\t\t -")
print("-" * 90)
print(housing_imputed_knn.loc[null_rows_idx].head())
