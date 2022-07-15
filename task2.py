x = 0
y = 0
z = 0
check = True

print("x   y   z res")
for x in range(2):  
    for y in range(2):
        for z in range(2):
            if ((not(x or y or z)) == (not(x) and not(y) and not(z))):  
                print(x," ",y," ",z," 1")  
                check = check and True  
            else: 
                print(x, " ", y, " ", z," 0")  
                check = check and False  

if (check): print("Выражение истинно ")
else: print("Выражение ложно ")