# Importamos librerias necesarias para proyecto
import pandas as pd
import plotly.express as px

"""
    Ejecutamos la lectura de los archivos que nos permitirán ejecutar el análisis del proyecto
"""

# Lectura de los archivos
car_data = pd.read_csv('./notebooks/vehicles_us.csv')  # leer los datos

# Descripción de los datos
"""
    descripción de las columnas en el DataFrame `vehicles_us.csv`:
        1. price: Costo del vehículo en dólares.
        2. model_year: Año de fabricación del vehículo.
        3. model: Modelo específico del vehículo.
        4. condition: Estado general del vehículo.
        5. cylinders: Número de cilindros del motor.
        6. fuel: Tipo de combustible utilizado.
        7. odometer: Kilometraje recorrido del vehículo.
        8. transmission: Tipo de transmisión del vehículo.
        9. type: Clasificación del vehículo.
        10. paint_color: Color de la pintura del vehículo.
        11. is_4wd: Indica tracción en las cuatro ruedas.
        12. date_posted: Fecha de publicación del anuncio.
        13. days_listed: Días que el anuncio estuvo activo.

        Se verificó que los nombres de las columnas están en snake_case, que sus tipos de datos son concordantes con la información mostrada y su nomenclatura es la adecuada.
"""

# Analizamos la información y el tipo de datos de las columnas del dataFrame
print(car_data.info())

# Verificamos si hay valores NaN
# print("\nValores NaN:\n", car_data.isna().sum())
# Se observa una gran presencia de valores nulos en las columnas 'is_4wd' y 'paint_color'

# Verificamos si hay valores duplicados en cada columna [No es a lugar para ninguna de las columnas]

# Etapa de preprocesamiento de Datos (EDA)


# Creación de función de corrección de nombres de columnas
def fix_columns_name(df):
    new_columns = []  # Lista que almacenará los nombres corregidos de columnas

    for column in df.columns:
        # Quitamos espacios al inicio y al final del encabezado de cada columna
        stripped_col = column.strip()
        # Convertimos a minúsculas los encabezados de cada columna
        lowered_col = stripped_col.lower()
        # Agregamos el nombre corregido a la lista
        new_columns.append(lowered_col)

    # Asignamos los nuevos nombres a las columnas del DataFrame
    df.columns = new_columns


# Uso de la función
fix_columns_name(car_data)

# Creación de función que permite hallar valores repetidos en columnas específicas


def hallar_repetidos(df):
    # Analizamos las columnas {condition, fuel, transmission, type, paint_color} para encontrar valores repetidos
    columns_to_check = ['condition', 'fuel',
                        'transmission', 'type', 'paint_color']

    duplicados_dict = {}
    for columna in columns_to_check:
        # Contamos las ocurrencias de cada valor
        value_counts = df[columna].value_counts()
        # Filtramos para quedarnos solo con los valores que se repiten
        repetidos = value_counts[value_counts > 1].index.tolist()

        if repetidos:
            duplicados_dict[columna] = repetidos

    return duplicados_dict


# Uso de la función
repetidos = hallar_repetidos(car_data)
# comprobamos que no existen duplicados implícitos en las columnas seleccionadas
