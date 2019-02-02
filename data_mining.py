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
over_90_list = []
all_B = []
all_C = []
all_D = []
all_E = []
all_F = []
all_I = []
all_K = []
all_L = []
all_M = []
all_N = []
all_Pi = []
all_W = []




#reads and imports txtfile to all list. Change the value of i to make the code run faster
def read_txtfile():
    with open("terminsstatus_17.txt") as f:
        for i, line in enumerate(f):
            if i < 1:
                keys = line.split()
            else:
                if i < 1000000000:
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

# divides input list into sublists for each input program
def sort_program(list, program):
    return_list = []
    for l in list:
        if l["program"] == program:
            return_list.append(l)
    return return_list

# populate lists for each program
all_B = sort_program(all_standardized_points, "B")
all_C = sort_program(all_standardized_points, "C")
all_D = sort_program(all_standardized_points, "D")
all_E = sort_program(all_standardized_points, "E")
all_F = sort_program(all_standardized_points, "F")
all_G = sort_program(all_standardized_points, "G")
all_I = sort_program(all_standardized_points, "I")
all_K = sort_program(all_standardized_points, "K")
all_L = sort_program(all_standardized_points, "L")
all_M = sort_program(all_standardized_points, "M")
all_N = sort_program(all_standardized_points, "N")
all_Pi = sort_program(all_standardized_points, "P")
all_T = sort_program(all_standardized_points, "T")
all_V = sort_program(all_standardized_points, "V")
all_W = sort_program(all_standardized_points, "W")


# returns list of sublists containing semesters for each starting year
def sort_starting_year(list):
    sorted_list = []
    newlist = sorted(list, key=lambda k: k['kull'])
    p = newlist[0]["kull"]
    temp = []
    for l in newlist:
        if l["kull"] == p:
            temp.append(l)
        else:
            sorted_list.append(temp.copy())
            temp.clear()
            temp.append(l)
        p = l["kull"]
    return sorted_list


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

# Returns list with point average for each starting year (kull)
def calc_points_average_per_starting_year(list):
    return_list = []
    for l in list:
        sum = 0
        for ll in l:
            sum += float(ll["poang_p"])
        average = sum/len(l)
        return_list.append(average)
        #print(l[0]["kull"] + ": " + str(sum/len(l)))
    return return_list

# ----------- # Populates year_average # ------------#
year_list = sort_starting_year(all_standardized_points)
year_average = calc_points_average_per_starting_year(year_list)


# Returns all semesters where the points taken are over 80 from input list
def over_80(list):
    for l in list:
        if float(l["poang_p"]) > 100:
            over_90_list.append(l)

# Plots program average
def plot_program_histogram():
    average_list = [get_point_average(all_B)] + [get_point_average(all_C)] + [get_point_average(all_D)] + [get_point_average(all_E)] + [get_point_average(all_F)] + [get_point_average(all_G)] + [get_point_average(all_I)] + [get_point_average(all_K)] + [get_point_average(all_L)] + [get_point_average(all_M)] + [get_point_average(all_N)] + [get_point_average(all_Pi)] + [get_point_average(all_T)] + [get_point_average(all_V)] + [get_point_average(all_W)]
    np_list = np.asarray(average_list)
    program_names = ["B","C","D","E","F","MD","I","K","L","M","N","Pi","BME", "V", "W"]
    plt.bar(range(len(np_list)), np_list)
    plt.xticks(np.arange(15), program_names)
    plt.show()


# Plots startyear average
def plot_startyear_histogram():
    np_list = np.asarray(year_average)
    year_names = [n[0]["kull"][:-1] for n in year_list]
    plt.bar(range(len(np_list)), np_list, width = 0.5)
    plt.xticks(np.arange(22), year_names)
    #tick.label.set_fontsize(8)
    plt.show()

# populates over_90 list with semester where points taken > 90
over_90(all_standardized_points)
for l in over_90_list:
    print(l)
