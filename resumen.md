Teoria

- Cuanto más grande sea el dataset, menos datos necesitaremos para el conjunto de prueba.
- (**_train set_**) datos para usarlos como conjunto de prueba (normalmente 20%)
- (**_training set_**) entrena el modelo con el resto
- Evita **sobreajuste** o **_overfitting_**
- Resuelve cuando el modelo se ajusta demasiado a los datos de entrenamiento, y no generaliza bien a datos nuevos. Si el error en el conjunto de entrenamiento es bajo y en el de prueba es alto, es que el modelo está sobreajustado.

Es importante aclarar ciertos términos que se utilizan en scikit-learn:

- **Estimadores**: cualquier objeto que pueda estimar algunos parámetros basados en un conjunto de datos se llama estimador. La estimación en sí misma se realiza mediante el método **`fit()`**.

  - **Transformadores**: estimadores que además pueden transformar datos usando el método **`transform()`**. Por ejemplo, `SimpleImputer` es un transformador: estima valores con `fit()` y los imputa con `transform()`.

    - Scalers: son transformadores que escalan los datos.
    - Imputers: son transformadores que imputan valores faltantes.
    - Encoders: son transformadores que codifican variables categóricas.
    - Reductores de dimensionalidad: son transformadores que reducen la cantidad de variables.
    - ...

  - **Predictores**: aquellos estimadores que son capaces de hacer predicciones basadas en un conjunto de datos. Por ejemplo, el modelo de regresión lineal es un predictor: estima los hiperparámetros `fit()` y hace predicciones con **`predict()`**.
    - Clasificadores: son predictores que predicen etiquetas categóricas.
    - Regresores: son predictores que predicen valores continuos.
    - Clusters: son predictores que predicen a qué cluster pertenece un dato.
    - ...

El término "predictor" puede prestarse a confusión ya que también se utiliza, en general, para referirse a las _features_ o variables independientes de un modelo, y a veces solo para aquellas variables que son de hecho **predictoras**, dejando fuera aquellas característcas que no tienen capacidad predictiva.

- Identificamos la columna de la variable independiente

- Generación de conjunto de entrenamiento

  - `train_set, test_set = train_test_split(df, test_sinze , stratify , bins , labels , random_state)`

    ```python
    df =housing
    test_size=0.2,
    stratify=pd.cut(housing["median_income"]
    bins=[0., 1.5, 3.0, 4.5, 6., np.inf]
    labels=[1, 2, 3, 4, 5]),
    random_state=42
    train_set, test_set = train_test_split(df, test_sinze , stratify , bins , labels , random_state)
    ```

- Eliminamos la columna de la variable dependiente

      ```python
      housing = train_set.drop("median_house_value", axis=1) # Eliminamos la columna de la variable dependiente
      housing_labels = train_set["median_house_value"].copy() # Guardamos la variable dependiente (etiquetas)
      ```

- Identificación de valores no disponibles (missing values)

  ```python
    null_rows_idx = housing.isnull().any(axis=1)
  ```

- Tratamos los valores nulos
- Eliminación de las filas con valores nulos (_**Listwise deletion**_)
- Imputación de algún valor (la mediana en este caso)
  - Usando `SimpleImputer`

    ``` python
        from sklearn.impute import SimpleImputer
    # instanciamos modelo

        imputer = SimpleImputer(strategy="median")

    # preparamos los datos

    # en este caso seleccinamos las columnas nuemericas

    # dato sobre el que vamos a actuar

        housing_num = housing.select_dtypes(
            include=[np.number]
        )  # seleccionamos las columnas numéricas

    # instanciamos modelo con los parametros

        imputer.fit(housing_num)

    # el modelo guarda la mediana en una variable `statistics_`

        imputer.statistics_  # mediana de cada columna numérica

    # transform() nos devuelve un <class 'numpy.ndarray'> con una matriz

    # sustituyendo los valores nulos por la mediana

    # recibe un df en el cual recoge la mediana y sustitulle los valores nulos

        housing_num_array_tr = imputer.transform(
          housing_num
        )  # reemplazamos los valores nulos por la mediana

    # empaquetamos los datos en un df

        data_array = housing_num_array_tr
        columns =housing_num.columns,
        index =housing_num.index
          housing_tr = pd.DataFrame(
          data_array , columns=columns, index=index
        )
      ```
