


def adresse():
    
    adress_1 = "MARCHE GHANACAN"
    adress_2 = "549 , Avenue QGILVY"
    adress_3 = "MONTREAL , QC H3N 1M9 "
    adress_4 = "TEL : (514) 278-6987"
    adress_5 = "DUPLICATA"
    
    
    x_1 = "{: ^70}\n{: ^70}\n{: ^70}\n{: ^70}\n{: ^70}\n".format(adress_1, adress_2, adress_3, adress_4, adress_5)
    
    cas = "\tCAISSIER                                              n*1 \n "
    print(x_1)
    print(cas)
    

def make_receipt(): 
    
    achats = dict() 

    while True:
    
        achat = input(" what you to buy ? " )
        price =  float(input("how much it is ?  "))
    
        achats[achat] =  price
    
        question = input(" anything else YES or NO ")
        if question.upper() == "NO" :
            break 
    
    adresse()
    for k , v in achats.items() :
            print ("\t{0:50}  ${1:.2f}\n".format(k,v))
    return achats    

def achat_total():

    
    achats = make_receipt()
    
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
        

    print ("\t{0:50}  ${1:.2f}\n".format(Totalsum, Total))
    
    bas_1 = "SANI"
    bas_2 = "001 001 000262 0001 02/12/2022 12:55"
    bas_3 = "IPS:143826998RT001 TVQ:1086786661TQ001"
    bas_4 = "*MERCI * THANK YOU "
    bas_5 = "A LA PROCHAINE . SEE YOU NEXT TIME "

    x_2 = "{: ^70}\n{: ^70}\n{: ^70}\n{: ^70}\n{: ^70}\n ".format(bas_1, bas_2, bas_3, bas_4, bas_5)

    print(x_2)   
      
   
achat_total()
    
    
#import cours6 as mo

#LIST = [20, 25, 36, 74]

#z = mo.find_index(LIST, 25)


#print (z)

person = {"age":40, "maison":"home", "montant":"$12325.58", "nom":"Gawonou", "ville":"Montreal" }

dic = {"vrai":"True", "faux":"False"}    


#message = "{0[nom]} est dans une ville qui s'appelle {0[ville]}, il a {0[age]} et a une somme {0[montant]} dans son compte c est {1[vrai]} ".format(person,dic)
#message1 = "%s est dans une ville qui s appelle %s et a %f  %d "%(nom, ville, age, montant)


#person.update({"vrai":"True", "alawoe":"918-8411678", "age":38})   to add or update
#del person["montant"] or person.pop("montant") to remove key value from dictionary
#len(person) to find how many keys we have in our dictionary

#print(len(person))
