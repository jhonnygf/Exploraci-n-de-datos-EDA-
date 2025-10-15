import os
import numpy as np
import pandas as pd
import wget

def get_version():
    print('Tengo la versión de Pandas:', pd.__version__)

def get_datting(url, local_filename):
    if os.path.exists(local_filename):
        print(f"Archivo encontrado: {local_filename}. Leyendo archivo...")
        return local_filename
    else:
        filename = wget.download(url)
        print('Descargando archivo:', filename)
        return filename

def get_dataframe(filename):
    if filename is None:
        print("No se puede cargar el DataFrame porque no hay archivo.")
        return None
    return pd.read_csv(filename)

def records_count(df):
    if df is not None:
        print("Número de registros en el dataset:", len(df))

def fuel_types(df):
    if df is not None:
        print("Tipos de combustible únicos:", df['fuel_type'].unique())
        print("Cantidad de tipos de combustible:", df['fuel_type'].nunique())

def missing_values(df):
    if df is not None:
        missing_cols = df.columns[df.isnull().any()]
        print("Columnas con valores faltantes:", missing_cols.tolist())
        print("Cantidad de columnas con valores faltantes:", len(missing_cols))

def max_fuel_effiency(df):
    print("Columnas disponibles:", df.columns.tolist())
    asia_cars = df[df['origin'] == 'Asia']
    max_eff = asia_cars['fuel_efficiency_mpg'].max()
    print("Máxima eficiencia de combustible de autos de Asia:", max_eff)

def median_value_horsepower(df):
    print("Columnas disponibles:", df.columns.tolist())
    # Calcular la mediana original de horsepower
    median_hp_before = df['horsepower'].median()
    print("Mediana original de horsepower:", median_hp_before)

    # Calcular el valor más frecuente (moda) de horsepower
    most_freq_hp = df['horsepower'].mode()[0]
    print("Valor más frecuente de horsepower:", most_freq_hp)

    # Rellenar los valores faltantes con la moda
    df['horsepower'] = df['horsepower'].fillna(most_freq_hp)

    # Calcular la mediana después de rellenar
    median_hp_after = df['horsepower'].median()
    print("Mediana de horsepower después de rellenar:", median_hp_after)

def sum_of_weights(df):
    # Seleccionar autos de Asia
    asia_cars = df[df['origin'] == 'Asia']

    # Seleccionar solo las columnas vehicle_weight y model_year
    X_df = asia_cars[['vehicle_weight', 'model_year']].head(7)

    # Obtener el array subyacente
    X = X_df.values

    # Calcular XTX y su inversa
    XTX = X.T @ X
    XTX_inv = np.linalg.inv(XTX)

    # Crear el array y
    y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])

    # Calcular w
    w = XTX_inv @ X.T @ y

    # Sumar los elementos de w
    sum_w = w.sum()
    print("Suma de los elementos de w:", sum_w)


url = "https://raw.githubusercontent.com/bigdatadatafan/datasets-clase/main/car_fuel_efficiency.csv"
local_filename = "car_fuel_efficiency.csv"

# Imprimir versión de Pandas
get_version()

# Obtener el nombre del archivo (descargar o buscar local)
filename = get_datting(url, local_filename)

# Cargar DataFrame
df = get_dataframe(filename)

# Contador de registros
records_count(df)

# Mostrar los tipos de combustible únicos
fuel_types(df)

# Contar columnas con valores faltantes
missing_values(df)

# Mostrar máxima eficiencia de combustible
max_fuel_effiency(df)

# Mostrar la media
median_value_horsepower(df)

# Suma de pesos
sum_of_weights(df)

