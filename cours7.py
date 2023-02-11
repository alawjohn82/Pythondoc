"""

donne moi un nombre  x, y

loop du plus petit au plus grand x a y ou y a x
 
 il va affichier nombre pair ou afficher impair  desc ou cro

python fff.py -p  == affiche pair decr  ===> python fff.py -p -d
python fff.py 

python fff.py -i -c

"""

import sys

def valeurs():
    x = int(input("Give me a number :" ))
    y = int(input("Give me a number :" ))
    
    val = x
    if x > y :
        x = y
        y = val
    
    return x, y


def pair(x, y):
    li =  []
    for i in range(x, y+1):
        if i%2 == 0 :
            li.append(i)

    return li

def impair(x, y):
    li =  []
    for i in range(x, y+1):
        if i% 2 != 0:
            li.append(i)

    return li
        
        
def decroissant(x, y):
    
   k = pair(x, y)
   k.reverse()

   return k
    
     

def decroissant_(x, y):
    k = impair(x, y)
    k.reverse()
    return k
    
    
        
def main():
    #print(valeurs())
    #print(len(sys.argv))
    
    x, y = valeurs()
    if  len(sys.argv) == 1:
        for i in pair(x,y):
            print(i)
    elif  len(sys.argv) == 3:
        if sys.argv[1] == "-p":
        #print(pair(x, y))
        
            if sys.argv[2] == "-d":
                for i in decroissant(x, y):
                    print(i)
            elif sys.argv[2] =="-c" :
                for i in pair(x, y):
                    print(i)  
        
                     
        if sys.argv[1] == "-i":
        #print(impair(x, y))
            if sys.argv[2]== "-d" :
                for i in decroissant_(x, y):
                    print(i)
            
            elif sys.argv[2]== "-c" :
                for i in impair(x, y) :
                    print(i)   
            else :
                print("not found!!!")
    
                      
            
        
               
            
                       
                
            
                                   
    
main()    

