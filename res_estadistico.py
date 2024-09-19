import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", type = str)

args = parser.parse_args()
file = args.file

datos = pd.read_csv(file, header=None)

serie = datos.iloc[:,0]

n = serie.count()
prom = serie.mean()
med = serie.median()
q1 = serie.quantile(0.25)
q3 = serie.quantile(0.75)
iqr = q3 - q1

resumen = pd.DataFrame({
    "n":n,
    "Promedio":round(prom,1),
    "Mediana":round(med,1),
    "Cuartil_1":round(q1,1),
    "Cuartil_3":round(q3,1),
    "IQR":round(iqr,1)
}, index = [""])

print(resumen)