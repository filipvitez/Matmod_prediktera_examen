from __future__ import print_function

import math

from IPython import display
from sys import platform as sys_pf
if sys_pf == "darwin":
    import matplotlib
    matplotlib.use("TkAgg")
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

#-------------# Load the txt-file into a panda dataframe #------------#

semesters = pd.read_csv("terminsstatus_17.txt", sep= "\t")

#--------------# Sort based on start-year to make guesses causal #------------#
sorted_on_start_year = semesters.sort_values(by = "kull")
soty = sorted_on_start_year
poang_p = soty['poang_p']

''' LTH gissar baserat på medelvärde '''

# mean = 0
# rmse = 0
# acc = 0
# for i,p in enumerate(poang_p):
#     rmse += np.sqrt(np.power(p-mean,2))
#     acc += p
#     mean = acc/(i+1)
# rmse /= poang_p.shape[0]
#
# print(rmse) # blir 13.18251


''' Program gissar medelvärde '''

# program_semesters = dict()
#
# program = soty.program.unique()
# for p in program:
#     ##program_means[p] = semesters[semesters.program == p].poang_p.mean()
#     program_semesters[p] = soty[soty.program == p].poang_p
#
#
# rmse = 0
# for ps in program_semesters:
#     val = program_semesters.get(ps)
#     mean = 0
#     acc = 0
#     rmse_temp = 0
#     for i, p in enumerate(val):
#         rmse_temp += np.sqrt(np.power(p-mean, 2))
#         acc += p
#         mean = acc/(i+1)
#     rmse += rmse_temp/val.shape[0]
# rmse /= len(program_semesters)
#
# print(rmse) # blir 12.704

''' Kön gissar medelvärde '''

#
# boy_points = soty[soty.female==0].poang_p
# girl_points = soty[soty.female==1].poang_p
#
# girl_rmse = 0
# girl_mean = 0
# girl_acc = 0
# for i, gp in enumerate(girl_points):
#      girl_rmse += np.sqrt(np.power(gp-girl_mean,2))
#      girl_acc += gp
#      girl_mean = girl_acc/(i+1)
# girl_rmse /= girl_points.shape[0]
#
# print(girl_rmse) # 13.31
#
# boy_rmse = 0
# boy_mean = 0
# boy_acc = 0
# for j, bp in enumerate(boy_points):
#     boy_rmse += np.sqrt(np.power(bp-boy_mean,2))
#     boy_acc = 0
#     boy_mean = boy_acc/(j+1)
# boy_rmse /= boy_points.shape[0]
#
# print(boy_rmse) #15.52
# rmse = (girl_rmse + boy_rmse)/2
# print(rmse) #14.42



#
# ''' förra termin gissar medelvärde '''
#
# prev_points = semesters.loc[semesters['lopnr'].shift(-1)==1, 'poang_p']
# print(prev_points)
#
# semesters2 = semesters.iloc[:100000 :]
#
#
# prev_points = lambda x: x.shift(+1)
# prev_semesters = semesters2.apply(prev_points)
# prev = []
#
# # Denna foor-loop tar sjukt lång tid av nån anledning, därför har jag valt att korta ner semesters2
# for i, s in semesters2.iterrows():
#     if s.lopnr == prev_semesters.iloc[i].lopnr:
#         prev.append(prev_semesters.iloc[i].poang_p)
#     else:
#         prev.append(None)
#
# prev_points = pd.DataFrame(prev)
#
#
# semesters2['prev_points'] = prev_points
#
# rmse = 0
# mean = 0
# acc = 0
#
#
# p1 = semesters2.poang_p
# p2 = semesters2.prev_points
#
#
# for i, p in enumerate(p1):
#     if not math.isnan(p2[i]):
#         rmse += np.sqrt(np.power(p-p2[i],2))
#     acc += p
#     mean = acc/(i+1)
# rmse /= p1.shape[0]
# print(rmse) # blir 8.33 Alltså rätt bra. Har dock bara kört den på 100k terminer
