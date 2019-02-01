import numpy as np
import matplotlib.pyplot as plt
import copy

all = [] # List containing all semesters (1 semester = 1 dictionary with 10 key-value pairs)
all_standardized_points = [] # List containing all semesters following the new point-system
all_girls= []
all_boys=[]
before_change = []
after_change = []
all_minus_zero = []
over_80 = []

#reads and imports txtfile to all list. Change the value of i to make the code run faster
def read_txtfile():
    with open("terminsstatus_17.txt") as f:
        for i, line in enumerate(f):
            if i < 1:
                keys = line.split()
            else:
                if i < 1000:
                    res = {}
                    v = line.split()
                    for k, item in enumerate(keys):
                        res[item] = v[k]
                    all.append(res)
                else:
                    break


#-----# THE FOLLOWING FUNCTIONS ARE FOR SORTING THE ORIGINAL ALL-LIST #--------#

# Populates before_list and after_list with semesters before- and after 2007
def separate_before_after():
    for item in all:
        if int(item["kull"]) >= 20072:
            after_change.append(item)
        else:
            before_change.append(item)

# Returns a list converted to the new point system
def convert_to_new_point_system(list):
    return_list = []
    for l in list:
        lcopy = l.copy()
        lcopy.update({'poang_p': (float(l["poang_p"])*1.5) })
        return_list.append(lcopy)
    return return_list

#------------# I kommande rader populeras listorna all, before_change, after_change och all_standardized_points mha funktionerna ovan #--------------#

read_txtfile()
separate_before_after()

all_standardized_points = convert_to_new_point_system(before_change) + after_change # En ny lista där alla terminer följer det gamla systemet


# from now on, all_standardized_points (a.s.p) will be the standard list to do operations on

#-------------------------------------------------------------------------------#

# Separates input list into girl and boys
def divide_sex(list):
    for l in list:
        if int(l["female"]) == 1:
            all_girls.append(l)
        else:
            all_boys.append(l)

# ----------------------------------------------------------------------------#
divide_sex(all_standardized_points) #populates all_boys and all_girls

# ----------------------------------------------------------------------------#

# returns a list where all the zero-point-semesters from input list is exluded
def remove_zero(list):
    return_list
    for item in list:
        if float(item["poang_p"]) > 0:
            return_list.append(item)
    return return_list


# Returns a list with sublists containing semesters for each student
def sort_students(list):
    sorted_list = []
    i = int(list[0]["lopnr"])
    temp = []
    for l in list:
        if i == int(l["lopnr"]):
            temp.append(l)
        else:
            sorted_list.append(temp.copy())
            temp.clear()
            temp.append(l)
        i = int(l["lopnr"])
    return sorted_list


#-----------------------# END OF SORTING FUNCTIONS #---------------------------#


#---------# THE FOLLOWING FUNCTIONS DO OPERATIONS ON SORTED LISTS #------------#

# Returns average points per semester for input list
def get_point_average(list):
    point_sum = 0
    for l in list:
        point_sum += float(l["poang_p"])
    return point_sum / len(list)


# Returns all semesters where the points taken are over 80 from input list
def over_80(list):
    for l in list:
        if float(l["poang_p"]) > 80:
            over_100.append(l)
