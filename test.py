import math
import linecache

#Punkts A
x1 = float(linecache.getline("dati_in.txt", 2))
y1 = float(linecache.getline("dati_in.txt", 4))
#Punkts B
x2 = float(linecache.getline("dati_in.txt", 6))
y2 = float(linecache.getline("dati_in.txt", 8))
#Punkts C
x3 = float(linecache.getline("dati_in.txt", 10))
y3 = float(linecache.getline("dati_in.txt", 12))

#a^2 + b^2 = c^2
ax = (x2-x3)**2 + (y2-y3)**2
bx = (x1-x3)**2 + (y3-y1)**2
cx = (x1-x2)**2 + (y2-y1)**2

#Pārbauda vai trīssturis ir iespējams
if ax <= 0 or  bx <= 0 or cx <= 0:
    file = open("dati_out.txt", "w")

    file.write("Trīsstūri nevar izveidot.")

    file.close()

else:
    #Malu garumi iegūti no kvadrātsaknēm
    a = math.sqrt(ax)
    b = math.sqrt(bx)
    c = math.sqrt(cx) 

    Perimiter = (a+b+c)

    #Laukuma iegūšana
    s = (a + b + c) / 2  
    Area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

    #Aprēķina m ar formulu m = "(y2-y1) / (x2 - x1)"
    m = (x3 - y3) / (x2 - y2)

    #Aprēķina t ar forumlu "y = mx + t", nav nepieciešams šajā piemērā
    #t = -x3 * m + y3

    #Aprēķina t no punkta A ar formulu "y = mx + t"
    ta = -(m*x1)+y1

    file = open("dati_out.txt", "w")
    
    file.write("Trīsstūri var izveidot." + "\n")
    file.write("Mala a = " + str(a) + "\n")
    file.write("Mala b = " + str(b) + "\n")
    file.write("Mala c = " + str(c) + "\n") 
    file.write("Perimetrs P = " + str(Perimiter) + "\n")
    file.write("Laukums S = " + str(Area) + "\n")
    file.write("y = " + str(m) + "x + " + str(ta))

    file.close()