import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import StratifiedShuffleSplit

semesters = pd.read_csv("terminsstatus_17.txt", sep= "\t") # Läser in datasetet i ett speciellt pandaobjekt


#---------------# Info om Datasettet #--------------------------------#
#print(semesters.head()) # Printar de översta elementen i datasetet
#print(semesters.shape[0]) # Printar antalet observationer (rader)
#print(semesters.shape[1]) # Printar antalet kolumner
#print(semesters.columns) # Printar column-namnen
#print(semesters.info()) # Printar info om rader, kolumner och datatyper


#------------# Columnsoperationer #----------------------#
#print(semesters.program.value_counts()) # får fram mängden av alla olika programtyper
#print(semesters.program.nunique()) # får fram antalet olika program
#print(semesters.program.unique()) # Får fram de olika programtyperna i en lista


#----------------# Statistisk Data #------------------------------#
#print(semesters.describe()) # Printar statistisk för de kolumner med int/float som datatyp
#print(semesters.poang_p.describe()) # Printar statistik för poang_p

#--------------# Sortering #------------------------------------#
#females = semesters[semesters.female == 1] # Endast tjejer
#M_students = semesters[semesters.program == "M"] # Endast M-studenter
#print(semesters.sort_values(by = "poang_p", ascending = False).head(10)) # printa de 10 terminerna med högst poäng
#sorted_startingyear = semesters.groupby('kull') # grupperar baserat på startår (kull)


#----------------# Kombinationer #------------------------#
#print(semesters.groupby('kull').poang_p.mean()) # printar poäng-medelvärde för alla årskullar
#print(semesters.groupby('kull').poang_p.describe()) # printar ut statistisk data för varje årskull
#print(semesters.groupby('kull').poang_p.agg(['mean', 'median', 'min', 'max'])) # printar medelvärde, median, min och max för kullarna
#print(semesters.groupby('program').female.sum() / semesters.program.value_counts() * 100) # Andel tjejer i varje program
#print(semesters.groupby(['program', 'female']).poang_p.mean()) # Printar medelvärdet för killar/tjejer för varje program


#------------------# Funktioner #-------------------------------#
