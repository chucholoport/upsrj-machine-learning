# 1. Preparación del entorno
#    - Usa la librería pandas.
#    - Usa la librería numpy.
#    - Usa la librería scipy.
#    Objetivo: Tener listo el entorno de trabajo.
#
# 2. Cargar el archivo CSV
#    - Usa pandas para leer el archivo "estudiantes.csv".
#    - Muestra las primeras filas de la tabla.
#    Objetivo: Familiarizarse con la estructura del DataFrame.
#
# 3. Explorar los datos
#    - Usa pandas para revisar la información de columnas y tipos de datos.
#    - Usa pandas para obtener estadísticas básicas de las columnas numéricas.
#    Objetivo: Identificar qué tipo de información contiene cada columna.
#
# 4. Selección y filtrado
#    - Usa pandas para seleccionar la columna de nombres.
#    - Usa pandas para filtrar los alumnos cuyo promedio sea mayor a 9.
#    Objetivo: Aprender a extraer subconjuntos de datos.
#
# 5. Operaciones con NumPy
#    - Usa numpy para convertir la columna de edades en un arreglo.
#    - Usa numpy para calcular medidas estadísticas básicas (media, desviación estándar).
#    Objetivo: Practicar cálculos numéricos con NumPy.
#
# 6. Agregar y transformar columnas
#    - Usa pandas junto con numpy para crear una nueva columna que indique
#      si el alumno es "Excelente" o "Regular" según su promedio.
#    Objetivo: Aprender a enriquecer los datos con nuevas variables.
#
# 7. Guardar resultados
#    - Usa pandas para exportar el DataFrame modificado a un nuevo archivo CSV.
#    Objetivo: Practicar la escritura de datos en CSV.
#
# 8. Operaciones con SciPy
#    - Usa scipy para realizar pruebas estadísticas sobre los datos de los alumnos.
#    - Ejemplo de aplicación: comparar edades o promedios con una distribución teórica,
#      o verificar si hay diferencias significativas entre grupos.
#    Objetivo: Introducir el uso de herramientas estadísticas más avanzadas.
#
# 9. Preguntas interpretativas
#    1. ¿Qué diferencia hay entre un DataFrame y un arreglo de NumPy?
#    2. ¿Por qué es útil explorar los datos antes de hacer cálculos?
#    3. ¿Qué aporta SciPy respecto a pandas y numpy en el análisis de datos?
#    4. ¿Cómo podrías usar estas herramientas para analizar el rendimiento de toda una clase?

import os
import pandas as pd
import numpy as np
import time
import shutil
import seaborn as sns
import matplotlib.pyplot as plt

from scipy import stats

# Windows: ".\inputs\estudiantes.csv"
# Linux:   "./inputs/estudiantes.csv"
SOURCE_FILE = os.path.join('.', 'inputs', 'estudiantes.csv')
print(SOURCE_FILE)

# Generamos un DataFrame con el contenido de "./inputs/estudiantes.csv"
# Despliego solamente los primeros 3 elementos del DataFrame.
estudiantes = pd.read_csv(SOURCE_FILE)
print(estudiantes.head(n=3))

# Desplegamos columnas de nuestro DataFrame
print(estudiantes.columns)

# Iteramos las columnas de nuestro DataFrame para visualizar el tipo de datos
for col in estudiantes.columns:
    
    data_type = estudiantes[col].dtype
    
    print('nombre:', col)
    print('tipo de dato:', data_type)
    
    if data_type == int or data_type == float:
        print('metricas (pandas):')
        print('-', 'media:', estudiantes[col].mean())
        print('-', 'mediana:', estudiantes[col].median())
        print('-', 'maximo:', estudiantes[col].max())
        print('-', 'minimo:', estudiantes[col].min())

    print('------------------')
    
# Seleccionamos la columna de nombres
#nombres = estudiantes['nombre']
nombres = estudiantes.nombre
mejores = estudiantes[estudiantes['promedio'] > 9]

# Convertimos columna de edades en array de numpy
# Si queremos ir desde Series -> NumPy con API de pandas
edades_pandas = estudiantes['edad'].to_numpy()
# Si queremos ir desde Series -> NumPy con API de numpy
edades_numpy = np.array(estudiantes['edad'])

# Metricas en NumPy
print('metricas (numpy):')
print('-', 'media:', edades_numpy.mean())
print('-', 'desviación estándar:', edades_numpy.std())
print('-', 'máximo:', edades_numpy.max())
print('-', 'mínimo:', edades_numpy.min())

# Creamos nueva columna con una evaluación del alumno conforme a su promedio
estudiantes['opinion'] = np.where(estudiantes['promedio'] > 9, 'Excelente', 'Regular')

# Windows: ".\out\estudiantes.csv"
# Linux:   "./out/estudiantes.csv"
OUTPUT_FILE = os.path.join('.', 'out', 'estudiantes.csv')
# Windows: ".\out"
# Linux:   "./out"
OUTPUT_DIR  = os.path.dirname(OUTPUT_FILE)

# Checamos si el directorio ./out existe y lo refrescamos
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.mkdir(OUTPUT_DIR)

# Creamos un ./out/estudiantes.csv
estudiantes.to_csv(OUTPUT_FILE)

edades_pandas        = estudiantes['edad'].to_numpy()
cuatrimestres_pandas = estudiantes['cuatrimestre'].to_numpy()
promedios_pandas     = estudiantes['edad'].to_numpy()

descripcion = stats.describe(edades_pandas)
print('statistics with SciPy:')
print(f'- mean: {descripcion.mean}')

#                  t_edad    p_edad
# ttest_1samp -> (statistic, pvalue, df)
# test_edad:
#   - _statistic_np
#   - _standard_error
#   - _estimate
#       ...
test_edad = stats.ttest_1samp(edades_pandas, 20)

print('Edad vs 20:')
print(test_edad._statistic_np)
print(test_edad._standard_error)
print(test_edad._estimate)

#                 0         1
# shapiro -> (statistic, pvalue)
p_edad_norm = stats.shapiro(edades_pandas)[1]
p_prom_norm = stats.shapiro(promedios_pandas)[1]

print('Normalidad edad -> p =', p_edad_norm)
print('Normalidad promedio -> p =', p_prom_norm)

# generar grafico
plt.figure(figsize=(10, 4))
plt.title('Mi primer grafico')
plt.xlabel('Cuatrimestre')
plt.ylabel('Promedio')
sns.boxplot(data=estudiantes, x='cuatrimestre', y='promedio')

# Windows: ".\out\figure.png"
# Linux:   "./out/figure.png"
OUTPUT_FIG = os.path.join(OUTPUT_DIR, 'figure.png')

# guardar y desplegar grafico
plt.savefig(OUTPUT_FIG)
plt.show()