import os
import sys
import pandas as pd

# creo variable con el url inputs/estudiantes.csv
CSV_FILE = os.path.join('inputs','estudiantes.csv')
# con read_csv creo un dataframe con el contenid de inputs/estudiantes.csv
estudiantes = pd.read_csv(CSV_FILE)
