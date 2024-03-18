<!-- markdownlint-disable MD041 -->
<!-- cSpell:ignore miniconda scikit numpy matplotlib tensorflow pexpect -->

# miniconda

## install miniconda

```Bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
 ~/miniconda3/bin/conda init bash
 ~/miniconda3/bin/conda init zsh

 source ~/.bashrc # update bash terminal
```

## environment

### create a new environment

```Bash
conda create --name py311
```

### use environment

```Bash
conda activate env1-py311
#instalar paquete
conda install nombre_del_paquete
# desstalar paquete
conda remove nombre_del_paquete
```

### verificar version de librería

```bash
conda list | grep scikit-learn

```

## current env

### env1-py311

```bash
# algoritmos de pia
conda activate env1-py311
conda install numpy # instala en el entorno coda actual
conda install matplotlib # lib -
conda install pandas # lib
conda install scikit-learn

```

### env-py38

```bash
# algoritmos de mia
# tensorflow solo admite hasta python 3.9
conda create --name env-py38 python=3.8
conda activate env-py38

# tensorflow
# Biblioteca de aprendizaje automático de código abierto desarrollada por Google que se utiliza principalmente para tareas de aprendizaje automático y desarrollo de modelos de inteligencia artificial.
conda install tensorflow

# numpy
# Biblioteca para trabajar con arrays multidimensionales y matrices en Python.
conda install numpy # arrays

# matplotlib
# Biblioteca para la creación de gráficos y visualizaciones de datos en Python.
conda install matplotlib # lib - gráficos

# pandas
# Biblioteca de análisis de datos que proporciona estructuras de datos flexibles y herramientas para trabajar con datos estructurados.
conda install pandas # lib DataFrames Secuencies

# scikit-learn
# Biblioteca de aprendizaje automático (machine learning) que proporciona herramientas simples y eficientes para el análisis predictivo de datos.
conda install scikit-learn

# pexpect
# Biblioteca de Python para controlar aplicaciones externas (por ejemplo, emuladores de terminal) y automatizar tareas interactivas.
conda install pexpect

# seaborn
# Biblioteca de visualización de datos basada en matplotlib que proporciona una interfaz de alto nivel para crear gráficos estadísticos atractivos y informativos.
conda install seaborn # lib - gráficos

# pillow
# Biblioteca de procesamiento de imágenes que proporciona capacidades básicas de manipulación de imágenes, como abrir, guardar, rotar y cambiar el tamaño de las imágenes.
conda install pillow # procesamiento de imágenes

```
