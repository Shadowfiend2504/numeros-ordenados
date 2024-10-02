
for i in range(9):
    for b in range (i):
        print(end=" ")
    for a in range (i, 9):
        print(a, end="")
    print("")

for i in range(7,-1,-1):
    for b in range (i):
        print(end=" ")
    for a in range (i, 9):
        print(a, end="")
    print("")
print("_________________________________________")    

for i in range(9):
    print(" " * i, end="")
    for a in range (i, 9):
        print(a, end=" ")
    print("")

for i in range(7,-1,-1):
    print(" "*i, end="")
    for a in range (i, 9):
        print(a, end=" ")
    print("")
print("_________________________________________")   

for i in range(9):
    print(" " * i, end="")
    for a in range (i, 9):
        print(a, end=" ")
    print("")

for i in range(7,-1,-1):
    print(" "*i, end="")
    for a in range (8,i-1,-1):
        print(a, end=" ")
    print("")
print("_________________________________________")
