
# DECREMENT PATTERN OR INVERTED HALF PYRAMID

for i in range (1,6):
    for j in range (i,6):
        print("*",end="  ")
    print()
    

# INCREMENT PATTERN OR INVERTED HALF PYRAMID

for i in range (1,6):
    for j in range (i):
        print("*",end=" ")
    print()
    
    
# FULL PYRAMID
   
for i in range(6):
    for j in range(i,6):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
    

# INVERTED FULL PYRAMID    
    
for i in range (6):
    for j in range (i+1):
        print (" ",end=" ")
    for j in range (i,6):
        print ("*",end=" ")
    for j in range (i,6-1):
        print ("*",end=" ")
    print()



#heart pattern

for i in range(6):
    for j in range(7):
        if (i == 0 and j % 3 != 0) or \
           (i == 1 and j % 3 == 0) or \
           (i - j == 2) or \
           (i + j == 8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()











