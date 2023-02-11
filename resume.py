
#Les types immuables:
#vrai = True
#faux - False
#age = 56 integer(int)
#montant = 45.56 float (decimal)




m = "Hey Alawoe"  #string
n = "And everyone"
#print(m) 

#to find how many character we have in the string
#print(len(m)) 

#to access the character individualy or the location or the index
#print(m[-1])

#how to access a range of character
#print(m[0:4])

# how to have m all lower case
#print(m.lower())  , print(m.upper())

#to count how many charater we have in the string
#print(m.count("l"))

# how to find a string  of character
#print(m.find("Alawoe"))

#to replace a character with another charater
#m = m.replace("Hey", "Hello")
#print(m)

#how to add multipli string
#print(f"{m} {n} today") or print("{} {} today".format(m,n))

# les types modifiables

#LIST

#empty liste
list = []

tab =  [45,  1, 12, 31, 5, 8 , 8 , 45, 67, 78, 3.5]


#print(tab)
#print(tab[0])
#print(tab[4])
#print(tab[-1])
#print(tab[-2])
#print(tab[2:5])
#print(tab[:5])
#print(tab[5:])



#tab.append(56) to add
#print(tab)
#print(sum(tab)

#c = sorted(tab)  to order from small to the highest
#print(c) # or tab.sort() and print(tab)

#the difference betwen sort() and sorted() is that the sorted() return a new version


#to add to a liste in certain position
#tab.insert(2, "add")
#print(tab)

#how to remove something from a list
#tab.remove(45)
#print(tab)

# how to remove all element from a list
#tab.clear()
#print(tab)

#Operation  liste

#x in l
#x not in l
# l + t
#l[i]
#l[i:j]
#max(l)
#min(l)
#l.append(a)
#l.count (x)
#l.index (x)
#l.insert(i,x)
#l.remove (x)


# DICTIONARY

d = {} # empty dictionary or dict()

dic =  { "KOKOU": 23, "Abalo" : 34, "Yao":45 }
dic1 =  {"Kokou": { "math" : 31, "franc":53 }, "Yao": {"math":30, "franc":34} }
stud = {"name":"john","age":25, "courses": ["math", "physic"]}

#it is allowed us to work with key and value
# dic[key]= value to access the value of a key 

#to access the key 
#print(stud.keys())

# to access the values
#print(stud.values())

#to access items or a pair ie (key,value)
#print(stud.items())

# to get a value of a key we can also use 
#print(stud.get("name"))

#to add a new key to our dictionary
#stud["adress"] = "415 s 25th "
#print(stud)

#dict2 = sorted(stud)  to sort a dictionary alphabetic order
#print(dict2)

#to change a value of a key
#stud["name"]= "rico"
#print(stud)

#stud.update({"vrai":"True", "alawoe":"918-8411678", "age":38})  # to add multipli item or update
#print(stud)

#del stud["name"]   to remove  a specific key  from dictionary
#stud.pop("name")
#    print(stud)


#print(len(stud))  # to find how many keys we have in our dictionary

#x in d
#x not in d
#len(d)
#min(d)
#max(d)
#del l [i]
#list (d)
#dict (x)
#d.items()
#d.keys()
#d.values()
#d.clear()
#.update(d2)


#CONDITIONALS(if , elif, else, while)

#Condition             Symbol
#equal                  ==
#not equal             !=
#Greater than           >
#less than              <
#greater or equal      >=
#less or equal         <=

#example for one condition
def even_odd():
    
    n = int(input("Give me a number: "  ))  
    
    
    if n %2 == 0:
        print("number is even")
    else :
        print("number is odd") 
        
#example of more than 2 conditions  

      
def convert_speed():
    speed = input("give  the speed in mph:  ")
    speed_c = input("in which symbole you want to convert? ")

    unite = speed[len(speed)-3:]

    speed_r =float(speed[:len(speed)-3])

    if unite == "mph" :
        if speed_c== "km/h":
            Speeds = speed_r*1.60934
        elif speed_c =="ms":
            Speeds = speed_r/2.237
            
    print(f"{round(Speeds,2)}{speed_c}")       

#convert_speed()    
    
#‘While’ loop is used for recursive action, and the loop repeat itself until a certain condition is satisfied.


def recur():
    i=0
    while i< 9 :
        print(i)
        i+=1

#recur()

       
# FuNCTION : instruction package together to perform a specif  task and allow us to use the code without repeting ourself

# to create a function we use the def key word

#def hello_everyone():
    #pass    #mean we dont want to do anything with this function for now

# to run the function we need to call it in order to execute it example : hello_everyone()

#example

       
def list_end():
    
    a = [5, 10, 15, 20, 25]   
    
    g= [a[0],a[len(a)-1]]   
    print(g)            

#list_end() 


# librairy standart  et les non standard 


#import json
#import numpy

#from math import pi, sqrt, pow 
#import cours3
#from  cours3 import multiplier

#print(dir(json))


###print(math.pi)
###print(math.sqrt(16))



#print(math.pow(2,4))
#rint(pi, sqrt(6), pow(5,2))
#g = 5 * pow(10, 2)

#print(g)
#print(multiplier(4,3))



"""
xmax = liste[0]

for i in liste :
    if i>xmax :
        xmax=i
print(xmax)         
p = sorted(liste)
print(p)
"""

def find_num():
    
    liste = [23, 45, 56, 35, 4, 26, 78, 91, 25 ,-4,-100.23,-23,-23.1, 92.6]

    #index = -1
    
    Trouve = False
    
    num = float(input("give me a number: "))
    for i , v in enumerate(liste) :
        
        if v == num :
            index = i
            Trouve = True
        print(index, " +++ ",i)
   # if  not index == -1:     
   #     print(f"{num} is not in the liste")   
    if Trouve :
        print(f"{num} est a la position {index}")
        
    else :
        print("not found")
        


# FILE OBJECTS (READIND and WRITING)
       
#how to open file first methode       
#f  = C 
#print(f.name) #will give us the name of the file
#print(f.mode) #will give us read =r or writing = w
#f.close()

# how to properly open a file
#with open ("exercice.txt", "r") as f :
    #fcontent = f.read() #all the content in the file
    #print(fcontent)
    
    #fcontent = f.readlines() # we will get a list of all the lines we have in the file 
    #print(fcontent)
    
    #fcontent = f.readline() #will grab the first line of the file
    #print(fcontent)
    
    #for line in f :
        #print(line) # to remove the space betwen each line we can print(line, end=" ")
        #print(line, end =" ")
        
    #fcontent = f.read(100)   #to specify the amount of data we want  we can pass in the size as argument,and in this 100 is the size(100= 100 characters)
    #print(fcontent) 
    
    #how to read a long size
    
    #size_read = 1000
    #fcontent = f.read(size_read)


def mak_triangle() :
    

    num =int(input("Give me a number: "))
    for i in range(num,-1,-1):
        for j in range(1,1+i):
            print("*",end ="")
        print()    
        
def mak1_triangle() :
        
    num_1 = int(input("Give me a number: "))
    for i in range(num_1):
        for j in range(1+i):
            print("*",end ="")
        print()    


def pyramid_up():
    num_2 =int(input("Give a number: "))

    s= (2*num_2) - 2
    for i in range(num_2):
        for j in range(s):
            print(end=" ")
        s= s-1     
        for j in range(i+1):
            print("* ",end=" ")   
        print(" ")    

def pyramid_down() :
    num_3 =int(input("Give a number: "))

    s= (2*num_3) - 2
    for i in range(num_3,-1,-1):
        for j in range(s,0,-1):
            print(end=" ")
        s= s+1     
        for j in range(0,i+1):
            print("*",end=" ")   
        print("")    

pyramid_up()


          
    
    
    