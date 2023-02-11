


#  100C N  ====> F
# 100F ====> c
# valeur  invalide


#     if / efig,/ leif else 
#  for  /while


## ellaahashshhshjajjjajasjsjjajajajajajajjajajj   leleahahahhahjajajjakaksklslalallaklakakaklkalalalallaklaj

"""
liste = [23, 45, 56, 35, 4, 26, 78, 91, 25]


for i in liste :
    if i  % 2  != 0:
        print(i)
        


d = 23 in liste

nombre  =  int(input("donne un nombre a verifier si case trouve dans le liste "))


if nombre  in  liste:
    print("Oui")
else:
    print("Non")
 
 
 
 
 
for i in liste:
    if i == nombre:
        print("OUI")
    else:
        print("NON")

d = 0 
 
while d < 100:
    print("Gawonou",d)
    d = d+ 1
    
    
liste.append(345)
liste.append(234)

liste.append(345)

print(min(liste))



"""

"""
#  1000c
# y =  100c   y[0:3]

temp = input("Donne temperature  ne terminat par C ")
unite = temp[-1]
      
long = len(temp)
temp_v = temp[0:long-1]
       
if unite == "C":
    valeur  =int(temp_v) -100
    print(valeur)
elif unite == "F":
    print("conversion en c")
else:
    print("tu ............")
    
"""  

"345"
"""
567
valeur = "123448"
#valuer[1:3]
print(valeur[0:4])  #1234

#valeur[debut:fin]
 """   
    
#   123.56$US     b     
# 120.34EUR
#$SCN


""" 
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
    if conversion == "EUR" :
        montant_converti = montant1/660


elif montant.endswith("JPY")  :
    if conversion == "$US":
        montant_converti = montant1 *0.0073
    elif conversion == "EUR" :
        montant_converti = montant1 *0.0069    
           





print(f" {montant_converti}{conversion}")


"""
"""

x = [23,45,56,35,4,26,28,91,25,12, 46, 34, 50, 453, 12]


"""
  


"""
x_sum=0
x_min = x[0]
 
for i in x :
    if i < x_min:
        x_min =  i
        
print(x_min)

for i in x :
    x_sum = x_sum +  i


print(x_sum)
i  = 0

while i < 100:        #  for and while
    print(i)
    if i ==  50:
        break
    i = i + 1
"""    
#x_position = int(input("give me a number x:"))


#print(x.index(x_position))
"""

index_valeur = -1
index = 0

for i in x:
    if i == x_position:
        #print(i,   index)
        index_valeur = index
        
    index = index + 1


if index_valeur == -1:
    print("the given number is not in the list")
else:
    print(x_position, index_valeur)
"""
 
"""          
index_valeur =-1  
demande = True


while  True :
    index = 0
    x_position = int(input("give me a number x:"))
    for i in x:
        if i == x_position:
        #print(i,   index)
            index_valeur = index
        
        index = index + 1

    
    if index_valeur == -1:
        print("the given number is not in the list")
    else:
        print(x_position, index_valeur)
        break
"""  

"""
   
x = [23,45,56,35,4,26,28,91,25,12, 46, 34, 50, 453, 12]

sum_xpair = 0
nombre_elt = 0

#  somm / n



#############33333333

for i in x :
   if  i%2 == 0 : 
       sum_xpair = sum_xpair + i
       nombre_elt = nombre_elt + 1
       
       
moyenne_elt_pair  =  sum_xpair/nombre_elt


print (moyenne_elt_pair)

###====================

elt_pair_list = []

for i in x:
    if i%2 == 0:
        elt_pair_list.append(i)


print(elt_pair_list)

moyenn = sum(elt_pair_list)/len(elt_pair_list)

print(moyenn)

########################



##############################

mydic =  { "KOKOU": 23, "koffi" : 34, "Yao":45 }
yourdic =  {"Kokou": { "math" : 31, "franc":53 }, "Yao": {"math":30, "franc":34} }
# idc = cle, valeur 


print(mydic["KOKOU"])
print(yourdic["Kokou"]["franc"])



for g in  mydic.items():     # keys, values
    print(g)
    

print(mydic.get("KOKOU"))
print(yourdic.get("Kokou").get("math"))
myset = {1, 3 , 5, 6, 89}
d = dict()={}   # dictionaire vide
l = list() =[]    # list vide
s = {}    # set vid 





mydd = dict()

mydd["monton"] = 56
mydd["pimenty"] = 6


print(mydd)



# function

def  mysum_pair():
    pass




# affichie
def afficher_adrese():
    print("1210 Rue Quennevile \n app 200 \ CANADA ")
    


# CALCUL VALEWUER DE KLK CHOSE NEN PARAMETRE 
def moyenne_nombre_par(li):
    li_sum = 0
    n_elt = 0
    for i in li:
        if i%2 == 0:
            li_sum = li_sum +i
            n_elt = n_elt + 1
    
    moy = li_sum /n_elt
    return moy 
            



#  retour valeur 


def my_sum():
    return x + y 






afficher_adrese()
afficher_adrese()
frf =  moyenne_nombre_par(x)
print(frf)

#######################################################

mydic =  { "KOKOU": 23, "koffi" : 34, "Yao":45 }

print (mydic.items())
print (mydic.keys())

print (mydic.values())
"""


adress_1 = "MARCHE GHANACAN"
adress_2 = "549 , Avenue QGILVY"
adress_3 = "MONTREAL , QC H3N 1M9 "
adress_4 = "TEL : (514) 278-6987"
adress_5 = "DUPLICATA"

#adress = "\n MARCHE GHANACAN \n 549 , Avenue QGILVY \n MONTREAL , QC H3N 1M9 \n TEL : (514) 278-6987 \n DUPLICATA \n "
x_1 = "{: ^50}\n{: ^50}\n{: ^50}\n{: ^50}\n{: ^50}\n".format(adress_1, adress_2, adress_3, adress_4, adress_5)
print(x_1)

cas = "\tCAISSIER                           1 \n "

print(cas)

#####Achat = input("What do you want to buy?")

###### price = float(input("how much is it?"    ))


###### mydic = { "Sac":"$2" , "Yam": "$24" , "YUCA": "$7.05" , "KOTOKO FUFU": "$20" , "PEAK 386ML": "$5" , "Fruit/Legume Balance": "$9.52" , "Poulet": "$12" , "Tripes de boeuf": "$15.17 " , "CHevre" : "$42.13" , "Fruit/Legume": "$2" , "Boeuf": "30.39"}
 #  NO No no YES Yes  



####for k , v in mydic.items() :
    ###print ("\t{0:50}  {1}".format(k,v))
    
    
    
message = " d {0:15} {1:8} {2}".format("d", "c", 1)


achats = dict() 

while True:
    
    achat = input(" what you to buy ? " )
    price = float(input("\nhow much it is ?  "))
    
    achats[achat] =  price
    
    question = input(" \nanything else YES or NO ")
    if question.upper() == "NO" :
        break  
    

for k , v in achats.items() :
    print ("\t{0:50}  ${1:.2f}".format(k,v))
    

# adress = function
#  acaht  function
#total taxe cuntion 
# en bas function


    
    
subtotal = 0

for v in achats.values() :
    subtotal = subtotal + v
    SalesTax = (8.517/100)*subtotal
    Total = SalesTax + subtotal
    
totalsum =  "subtotal"  
Salessum = "SalesTax"   
Totalsum = "Total"

print ("\t{0:50}  ${1:.2f} ".format(totalsum, subtotal))   
print ("\t{0:50}  ${1:.2f}".format(Salessum, SalesTax)) 

print ("\t{0:50}  ${1:.2f}".format(Totalsum, Total))

          
      