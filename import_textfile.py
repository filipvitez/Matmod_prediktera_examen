import numpy as np
import matplotlib.pyplot as plt

all = []
before_change = []
after_change = []
boys_after = []
girls_after = []

with open("terminsstatus_17.txt") as f:
    for i, line in enumerate(f):
        if i < 1:
            keys = line.split()
        else:
            if i < 10000000000:
                res = {}
                v = line.split()
                for k, item in enumerate(keys):
                    res[item] = v[k]
                all.append(res)
            else:
                break


for a in all:
    if int(a["kull"]) >= 20072:
        after_change.append(a)
    else:
        before_change.append(a)

for a in after_change:
    if int(a["female"]) == 1:
        girls_after.append(a)
    else:
        boys_after.append(a)

# Returns average points per semester for inputed list
def get_point_average(list):
    point_sum = 0
    for l in list:
        point_sum += float(l["poang_p"])
    return point_sum / len(list)

over_100 = []

for a in all:
    if float(a["poang_p"]) > 80:
        over_100.append(a)

#print(len(all))
#print(len(over_100))

print(get_point_average(before_change))
print(get_point_average(after_change))


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

#print(len(sort_students(boys_after)))
