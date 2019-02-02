# Denna fil är till för att testa python-logik


dict = {
    "tjena": 1,
    "Tja": 2,
    "hej": 3
}

dict.update({"tjena": 2})
print(dict)



test = [2]*4

test[0] = "tja"
print(test)

tja = ["Tja"] + [3]
print(tja)

test = [1,2,2,3,"tja"]
test2 = ["hej,", 2]
print(test + test2)

a = "tja"
print(a[:-1])
