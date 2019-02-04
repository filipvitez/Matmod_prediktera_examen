import numpy as np
import matplotlib.pyplot as plt
import copy

all = [] # List containing all semesters (1 semester = 1 dictionary with 10 key-value pairs)
all_standardized_points = [] # List containing all semesters with semesters before 2007 multiplied by 1.5
all_minus_zero = []
all_girls= [] #not containing zero-semesters
all_boys=[] #not containing zero-semesters
before_change = []
after_change = []
all_minus_zero = []
over_80_list = []
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
semesters = []
students_minus_zero_list = [] # List of lists of non-zero semesters for each students



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



#-------------------------------------------------------------------------------#

# returns a list where all the zero-point-semesters from input list is exluded
def remove_zero(list):
    return_list = []
    for item in list:
        if float(item["poang_p"]) > 0:
            return_list.append(item)
    return return_list

# Separates input list into girl and boys
def divide_sex(list):
    for l in list:
        if int(l["female"]) == 1:
            all_girls.append(l)
        else:
            all_boys.append(l)

# ----------------------------------------------------------------------------#

all_minus_zero = remove_zero(all) #populates all_minus_zero
divide_sex(all_minus_zero) #populates all_boys and all_girls with non-zero semesters

# ----------------------------------------------------------------------------#



# divides input list into sublists for each input program
def sort_program(list, program):
    return_list = []
    for l in list:
        if l["program"] == program:
            return_list.append(l)
    return return_list


# populate lists for each program
all_B = sort_program(all_minus_zero, "B")
all_C = sort_program(all_minus_zero, "C")
all_D = sort_program(all_minus_zero, "D")
all_E = sort_program(all_minus_zero, "E")
all_F = sort_program(all_minus_zero, "F")
all_G = sort_program(all_minus_zero, "G")
all_I = sort_program(all_minus_zero, "I")
all_K = sort_program(all_minus_zero, "K")
all_L = sort_program(all_minus_zero, "L")
all_M = sort_program(all_minus_zero, "M")
all_N = sort_program(all_minus_zero, "N")
all_Pi = sort_program(all_minus_zero, "P")
all_T = sort_program(all_minus_zero, "T")
all_V = sort_program(all_minus_zero, "V")
all_W = sort_program(all_minus_zero, "W")


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
year_list = sort_starting_year(remove_zero(all))
year_average = calc_points_average_per_starting_year(year_list)


# Returns all semesters where the points taken are over 80 from input list
def over_80():
    for l in all:
        if float(l["poang_p"]) > 80:
            over_80_list.append(l)

# Plots program average
def plot_program_histogram():
    average_list = [get_point_average(all_B)] + [get_point_average(all_C)] + [get_point_average(all_D)] + [get_point_average(all_E)] + [get_point_average(all_F)] + [get_point_average(all_G)] + [get_point_average(all_I)] + [get_point_average(all_K)] + [get_point_average(all_L)] + [get_point_average(all_M)] + [get_point_average(all_N)] + [get_point_average(all_Pi)] + [get_point_average(all_T)] + [get_point_average(all_V)] + [get_point_average(all_W)]
    np_list = np.asarray(average_list)
    program_names = ["B","C","D","E","F","MD","I","K","L","M","N","Pi","BME", "V", "W"]
    plt.bar(range(len(np_list)), np_list)
    plt.xticks(np.arange(15), program_names)
    plt.show()

#plot_program_histogram()

# Plots startyear average
def plot_startyear_histogram():
    np_list = np.asarray(year_average)
    year_names = [n[0]["kull"][:-1] for n in year_list]
    plt.bar(range(len(np_list)), np_list, width = 0.5)
    plt.xticks(np.arange(22), year_names)
    #tick.label.set_fontsize(8)
    plt.show()

#plot_startyear_histogram()

# prints contents of over_80-list
def print_over_80():
    for l in over_80_list:
        print(l)

# Populate over 80 list
#over_80()


def get_semester_average(list,semesterNbr): #return average points for a list, for the semester semesterNbr
    temp = []
    point_sum=0
    list=remove_zero(list)
    for i in range(1, 20):
        for l in list:
            if i == int(l["ptnr"]):
                temp.append(float(l["poang_p"]))

        semesters.append((temp.copy()))
        temp.clear();
    for l in semesters[semesterNbr]:
        point_sum += float(l)
    return point_sum/len((semesters[semesterNbr]))

#----------# List of lists of non-zero semesters for each students #----------#
students_minus_zero_list = sort_students(all_minus_zero)


# If input list is list of lists of semesters, removes all lists with only 1 semesters
# (returned list is used for calculating semester error)
def remove_lists_with_1_semester(list):
    return_list = []
    for l in list:
        if len(l) > 1:
            return_list.append(l)
    return return_list

# Calculates the mean_error from "guessing" the points taken one semester based on points taken previous semesters
# Zero-semesters are excluded
def calc_last_semester_error(list):
    mean_error = 0
    accumulative_error = 0
    for l in list:
        temp_mean_error = 0
        prev_points = 0
        for ll in l:
            if prev_points != 0:
                temp_mean_error += np.abs(float(ll["poang_p"]) - prev_points)/prev_points
            prev_points = float(ll["poang_p"])
        accumulative_error += temp_mean_error/(len(l)-1)
    mean_error = accumulative_error/len(list)
    return mean_error

print(calc_last_semester_error(remove_lists_with_1_semester(students_minus_zero_list)))


#all_M = print(get_semester_average(all_B,2))
