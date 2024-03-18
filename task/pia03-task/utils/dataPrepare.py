import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def DataPrepare(path):
    """
    Carga y procesa los datos.

    Args:
    - path: Ruta del archivo CSV con los datos.

    Returns:
    - housing: DataFrame con los datos procesados.
    - null_rows_idx: Índices de las filas con valores nulos.
    """
    housing = pd.read_csv(path)

    # Generación de conjuntos de entrenamiento y prueba mediante muestreo estratificado por ingreso medio
    # función train_test_split de scikit-learn
    # Divide el conjunto de datos en conjuntos de entrenamiento y prueba,
    train_set, test_set = train_test_split(
        housing,  # DataFrame
        test_size=0.2,  # El conjunto de prueba es el 20% del tamaño total
        stratify=pd.cut(  #  se estratifica por el ingreso medio,
            housing["median_income"],
            bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
            labels=[1, 2, 3, 4, 5],
        ),
    )
    # Procesamiento de datos
    # Eliminamos la columna de la variable dependiente
    housing = train_set.drop("median_house_value", axis=1)

    # Identificación de valores no disponibles
    # Índices de las filas con valores nulos
    null_rows_idx = housing.isnull().any(axis=1)

    return housing, null_rows_idx
