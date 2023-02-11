#mydic =  { "KOKOU": 23, "koffi" : 34, "Yao":45 }

#print(mydic)





def  function_name():
    pass




def multiplier(x,y):
    z = x * y 
    return z 




def affiche():
    print("introduction programme python")
    
    
    
    
def affiche_message(message):
    print(message)
    
    
def calcul(x,y):
    z = x+ y 
    
    

v = 6
b = 7 
    
    
(#d = multiplier(3, 6)
#affiche()
#affiche_message("allo Gawonou")
#calcul(v, b)
#print(d)
)



def make_receipt(): 
    
    achats = dict() 

    while True:
    
        achat = input(" what you to buy ? " )
        price =  input("\nhow much it is ?  ")
    
        achats[achat] =  price
    
        question = input(" anything else YES or NO ")
        if question.upper() == "NO" :
            break 
        
    for k , v in achats.items() :
            print ("\t{0:50}  ${1:.2f}".format(k,v))
    return achats



def adresse():
    adress = "\n  MARCHE GHANACAN \n 549 , Avenue QGILVY \n MONTREAL , QC H3N 1M9 \n TEL : (514) 278-6987 \n DUPLICATA \n "
    print(adress)
    
# ahahahahhahahahah
    
    
def achat_total():
    cas = "\tCAISSIER                           1 \n "
    
    achats = dict()
    
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
        print(cas)

        print ("\t{0:50}  ${1:.2f}".format(Totalsum, Total))


def bas_message() :
    message_bas = "\n SANI \n 001 001 000262 0001 02/12/2022 12:55 \n IPS:143826998RT001 TVQ:1086786661TQ0001 \n *MERCI * THANK YOU \n A LA PROCHAINE . SEE YOU NEXT TIME"
    print(bas_message)

    
#import sys
#print(sys.path)


w = "elle"  

k = "lele" 




