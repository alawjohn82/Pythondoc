


liste = [23, 45, 56, 35, 4, 26, 78, 91, 25 ,-4,-100.23,-23,-23.1, 92.6]

def liste_min():

    x_min = liste[0]
    for i in liste :
       if i < x_min :
            x_min=i
    print(x_min)  
    return x_min    
            
        
def liste_max() : 

    x_max = liste[0]   

    for i in liste :
        if i > x_max :
         x_max = i
        
    print(x_max)
    return x_max
    
def multiple():
    a = liste_min()
    b = liste_max()
    c= (a * b)/2
    
    print("{:#^21}".format(c))
    return c


def sum():
    k = liste_min()
    f = liste_max()
    l = [k, f]
    
    sum = 0
    for i in l :
        sum = sum + i
    print(sum)

#how to find the index of each element in a list      

def position() : 
    index = 0

    for i in liste :
        print(index, i) 
        index = index + 1 #or index += 1

               
 
    
  

def position_2():
    
    
    index_valeur =-1 

    while  True :
        index = 0
        liste_position = int(input("give me a number :"))
        for i in liste:
            if i == liste_position:
            #print(i,   index)
                index_valeur = index
       
        index = index + 1
  
    
        if index_valeur == -1:
            print("the given number is not in the list")
        else:
            print(liste_position, index_valeur)
            break
    
def montant():
    
    montant = input("give me the amount with the symbol ")
    conversion = input("\ndo you want to convert in witch courrency ? : ")
  
    unite = montant[len(montant)-3:]

    print(unite) 
    montant1 =float(montant[0:len(montant)-3])



    print("=========================", montant.endswith("$US"))



    if   montant.endswith("$US"):    # unite ==  "$US":
        if conversion == "EUR":
            montant_converti =  montant1 * 0.97
        elif conversion == "CFA":
            montant_converti =  montant1 * 550
        elif conversion == "$CA":
            montant_converti = montant1 * 1.33
        elif conversion == "$US":
            montant_converti = montant1        
        elif conversion == "GBP" :
            montant_converti = montant1 * 0.82 
        elif conversion == "JPY" :
            montant_converti = montant1 * 136.75
            
            
    elif unite == "EUR":
        if conversion == "$US":
            montant_converti = montant1*1.03
        elif conversion == "JPY":
            montant_converti = montant1 * 144.41 
        elif conversion == "$CA" :
            montant_converti = montant1 * 1.44  
        elif conversion == "GBP" :
            montant_converti = montant1 * 0.86 
        elif conversion == "CFA" :
            montant_converti = montant1 * 660      
        
    elif unite == "CFA":
        if conversion == "$US":
            montant_converti = montant1/550  
        elif conversion == "EUR" :
            montant_converti = montant1/660


    elif montant.endswith("JPY")  :
        if conversion == "$US":
            montant_converti = montant1 *0.0073
        elif conversion == "EUR" :
            montant_converti = montant1 *0.0069          
            
            
            
            
            
    print(f" {montant_converti}{conversion}")        

def make_tab():
    names =["Abalo Alawoe", "Afi Gawonou", "john Akakpo","Kokou Akakpo"]
    french = [10, 5, 2, 4]
    math = [15, 10, 7, 15]
    english = [4, 4, 4, 10]
    n = "Names"


    print("\n{:<20}{:^20}{:^20}{:^20}{:^15}\n".format(n, 'French','Math','English','Moyenne'))
          
    for i in range(0,4):
        print("{:<20}{:^20}{:^20}{:>12}\n".format(names[i],french[i],math[i],english[i]))   

def characters():

    name = input("\nwhat is your name?:" )
    age = int(input("\nwhat is your age? :" ))


    y_100 = 2023 - age + 100

    print(f"{name} in {y_100} will be 100 years old")
    
def even_odd():
    
    n = int(input("Give me a number: "  ))  
    
    
    if n %2 == 0:
        print("number is even")
    else :
        print("number is odd") 
        
       
def liste_a():
    
     a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
     b = []
     for i in a :
         if i < 5 :
             b.append(i)
             
     print(b)                    
           
                        
def liste_b():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    c = []
    number = int(input("give me a number:  "))     
    for i in a :
        if i<number :
            c.append(i) 
    print(c)
    
def divisor():   
    
    #Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number
                                                                                                                          
    num = int(input("give me a number: ")) 
    g =[]   # or g = list(  )


    for i in range(1, num+1) :
        if num%i == 0 :
            g.append(i)
       
    print(g)
    return g
    
def union():
    
    #write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes    
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]   
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]       
    c = []

    for i in a and b:
        if i  in a and b:
            c.append(i)

    print(c)


def no_divisor():
    
    #Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).  
    num =int(input("give me anumber : "))
    
    for i in range(2,num):
       if num % i == 0:
           print(num,"is not a prime number")
           break
    else:
        print(num,"is a prime number")
        
       
def list_end():
    
    a = [5, 10, 15, 20, 25]   
    
    g= [a[0],a[len(a)-1]]   
    print(g)            


def addsum(a, b):
    c=a*b
    print(c)
    return c
    
    
def check():    
    liste = [23, 45, 56, 35, 4, 26, 78, 91, 25 ]

    number = int(input("give me a number: " ))

    if number in liste :
        print("number is in liste")
    else :
        print("bye bye")    
    
def check_1():    
    liste = [23, 45, 56, 35, 4, 26, 78, 91, 25 ]
    m=[]
    z=[]
    k=[]
    l=[]
    for i in liste:
    
        if i%2==0:
            if i%3==0 :
                k.append(i)        
            elif i%3!=0 :
                l.append(i)       
        elif i%2!=0:
            if i%3==0:
                z.append(i)
            else:
                m.append(i)    
    print(k)
    print(l) 
    print(z)       
    print(m)        
      
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
    
def num_divisor():
         
    # Find the number of divisors of a given integer is even or odd    
    m = int(input("give me any number: "))
    g =[] 
    
    for i in range(1, m+1) :
        if m%i == 0 :
            g.append(i)
            
    print(len(g))      
 
def cal_sum():
    
    g = divisor()
    
    sum_g = 0
    n_elts = 0  
    for i in g :
        sum_g = sum_g + i
        n_elts = n_elts + 1 #or len(g)
    print(round(sum_g/n_elts , 2)) 
    
    
def lim_1(aba , af) :
    sum = 0
    for i in aba :
        sum = sum + i 
        af= sum
    return af  

def find_index(ens,result):
    
    for i , v in enumerate(ens) :       
        if v == result :
            return i
    return -1    
 
def fib():               
    # Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
    #The Fibonacci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence
    
    number =int(input("give me a number :"))
    
    
def sum_4():       
    g=[]  
    for i in range(100,201):
        if i%2== 0 :
            g.append(i) 
    return g 
        
def tot():      
    total = sum_4()
    elt = 0
    sum =0
    while(elt < len(total)):
        sum = sum  + total[elt]
        elt += 1
    print(sum)    
    
 
tot()





