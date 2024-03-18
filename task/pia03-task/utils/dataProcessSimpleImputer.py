import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.model_selection import train_test_split

def DataProcessSimpleImputer(housing):
    """
    Ejecuta SimpleImputer para imputar los valores nulos.
    
    Args:
    - housing: DataFrame con los datos.
    - null_rows_idx: Índices de las filas con valores nulos.
    
    Returns:
    - housing_imputed: DataFrame con los valores nulos imputados.
    """
    # Creamos una instancia de `SimpleImputer` 
    # para imputar los valores nulos con la mediana
    imputer = SimpleImputer(strategy="median")

    # Seleccionamos las columnas numéricas
    housing_num = housing.select_dtypes(include=[np.number])

    # Calculamos la mediana de cada columna numérica
    imputer.fit(housing_num)

    # Reemplazamos los valores nulos por la mediana
    housing_imputed = pd.DataFrame(imputer.transform(housing_num), columns=housing_num.columns, index=housing_num.index)

    return housing_imputed