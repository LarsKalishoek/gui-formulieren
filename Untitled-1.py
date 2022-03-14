import time


# Tuples: ordered, unchangeable, allows duplicates
tuple = ("peer", "kers")


# Sets: unordered, unchangeable, duplicates not allowed
set = {"salami", "brood"}


# Lists: ordered, changeable, allows duplicates
list = ["kaas", "appel"]


# Dictionary: ordered, changeable, duplicates not allowed
dic = {
   "brand" : "Ford",
   "model" : "Focus",
   "year"  : 2017,
}

# tuple.append("telefoon")
print(tuple)
time.sleep(10)

print(set)
time.sleep(10)

list.append("telefoon")
print(list)
print(list[1])
time.sleep(10)

dic.update({"telefoon" : "iPhone"})
dic["year"]= 1991
print(dic)