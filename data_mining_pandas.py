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
print(semesters.info()) # Printar info om rader, kolumner och datatyper


#------------# Columnsoperationer #----------------------#
#print(semesters.program.value_counts()) # får fram mängden av alla olika programtyper
#print(semesters.program.nunique()) # får fram antalet olika program
#print(semesters.program.unique()) # Får fram de olika programtyperna i en lista


#----------------# Statistisk Data #------------------------------#
#print(semesters.describe()) # Printar statistisk för de kolumner med int/float som datatyp
#print(semesters.poang_p.describe()) # Printar statistik för poang_p

#--------------# Sortering #------------------------------------#
#females = semesters[semesters.female == 1] # Endast tjejer
#non_zero = semesters[semesters.poang_p != 0] # Inga nollterminer
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
# Skapa funktioner som objekt och applya till panda-objekten

        #------# Start_year_cleaner #---------#
#start_year_cleaner = lambda x: int(str(x)[:-1]) # tar bort termins-numret ur "kull"
#print(semesters.kull.apply(start_year_cleaner).head()) # printar de översta start åren, där terminsnumret är borttaget
#semesters.kull = semesters.kull.apply(start_year_cleaner) # ändrar om listan så att terminsnumret inte är med i "kull"
        #------------------------------------#

        #-------# Add boolean-column to check if semester has over 30p #--------#
#over_30_points = lambda x: x>30 #create function
#semesters['over_30'] = semesters.poang_p.apply(over_30_points) # create new column in semesters named 'over_30'
#print(semesters.head(40)) # check if works as intended
        #----------------------------------------#
