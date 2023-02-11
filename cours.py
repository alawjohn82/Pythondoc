#age = 19
#montant = 23.56
#nom = " Alawoe"

"""
print(age,montant, nom)

print(f"{nom} a  {age} ans et {montant} $")
print(nom.upper())


age2 = int(input("\ndonne moi ton age ? "))

age3 = age2 + age

montant2 = float(input("\ndonne um montant "))
montant3 = montant2 + montant

nom2 = input("\nquel est ton nom ")

nom_complet  = nom2  + nom 


print(f"\n{nom_complet} a {age3} ans et {montant3}")

"""
"""
#  LES TYOE MODIFIALBLE




tableau =  [45,  1, 12, 31, 5, 8 , 8 , 45, 67, 78, 3.5]


print(tableau)
print(tableau[0])
print(tableau[4])
print(tableau[-1])
print(tableau[-2])
print(tableau[2:5])
print(tableau[:5])
print(tableau[5:])

[0:5] ET [:5] 

tableau.append(56)
print(tableau)

print(sum(tableau))


for elt in tableau:
    print(elt)
    

print(12 in  tableau)



"""
     
#liste = [23, 45, 56, 35, 4, 26, 78, 91, 25]



#for i , n in enumerate(liste) :
    
#    print(i, n)
    
n = int(input("Enter the number of rows: "))  
m = (2 * n) - 2  
for i in range(0, n):  
    for j in range(0, m):  
        print(end=" ")  
    m = m - 1  # decrementing m after each loop  
    for j in range(0, i + 1):  
        # printing full Triangle pyramid using stars  
        print("* ", end=' ')  
    print(" ")  


 
