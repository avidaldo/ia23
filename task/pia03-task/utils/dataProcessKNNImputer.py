import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.model_selection import train_test_split

def DataProcessKNNImputer(housing):
    """
    Ejecuta KNNImputer para imputar los valores nulos.
    
    Args:
    - housing: DataFrame con los datos.
    - null_rows_idx: Índices de las filas con valores nulos.
    
    Returns:
    - housing_imputed: DataFrame con los valores nulos imputados.
    """
    # Creamos una instancia de `KNNImputer` 
    # para imputar los valores nulos con la estrategia de vecinos más cercanos
    imputer = KNNImputer(n_neighbors=5)  # Puedes ajustar el número de vecinos según tus necesidades

    # Seleccionamos las columnas numéricas
    housing_num = housing.select_dtypes(include=[np.number])

    # Imputamos los valores nulos utilizando KNN
    housing_imputed = pd.DataFrame(imputer.fit_transform(housing_num), columns=housing_num.columns, index=housing_num.index)

    return housing_imputed