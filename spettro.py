#! /usr/bin/env python
"""
legge un file .sp prodotto con spotread e lo plotta
uso: spettro.py nome_file

Testato con:
python 3.8.8
colour-science 0.3.16
spotread 2.1.1

opzioni spotread:

ambient light spectrum
spotread -v -s -H -a "file.sp"

reflectance spectrum
spotread -v -s -H "file_refl.sp"

transmission spectrum
spotread -v -s -H -t "file_trans.sp"

emission spectrum
spotread -v -s -H -e "file_emiss.sp"

flash emission spectrum
spotread -v -s -H -f "file_flash.sp"

"""

import colour.plotting as colorplot
from colour import SpectralDistribution
import argparse

# gestisce argomenti
parser = argparse.ArgumentParser()
parser.add_argument("file", help="file .sp generato con spotread")
args = parser.parse_args()

# nome del file prodotto da spotread
filepath = args.file
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        line = fp.readline()
        # linea 15 contiene lunghezze d'onda
        if cnt == 14:
            wavelenght = line
        # linea 20 contiene i dati di spettro
        if cnt == 19:
            data = line
        cnt += 1

# wavelenght e data sono stringhe, costruisce liste di
# stringhe e crea nuova lista lunghezze d'onda senza prefisso
wavelenght_list = wavelenght.split()
data_list = data.split()
new_wave_list = []

for i in wavelenght_list:
    if "_" in i:
        param, value = i.split("_", 1)
        new_wave_list.extend([value])

# crea spectral distribution dalle due liste e plotta
sd = SpectralDistribution(data=data_list, domain=new_wave_list)
colorplot.plot_single_sd(sd, name=filepath)

