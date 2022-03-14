#input
input = int(input("Hoeveel priem getalle wil je? : "))

#variables
checkPriem = 0 
number = 1 
checkNum = 0
list1 = []

for j in range(100):
    list1.append(number)
    number += 1

#statements
for y in range(input):
    for x in range(len(list1)):    
        a = number%list1[x]
        if a == 0:
            checkNum += 1
            
    if checkNum == 2:
        checkNum = 0
        checkPriem += 1
    number+= 1

print(checkPriem)

#user defined functions
# def priem(num):
#     global number
#     for x in range(num):
#         a = number%list1[x]
#         if a == 0 :
#             print(number)
#         number += 1

priemGetal = []

def isPriem(x):
    if x == 2:
        return True
    for a in range(0, len(priemGetal)):
        if x % priemGetal[a] == 0:
            return False
    return True

teller = 0

for i in range(2,10):
    if isPriem(i):
        teller +=1
        print(f'Het {teller}e priemgetal is: {i}')
        priemGetal.append(i)

# priem(input)
