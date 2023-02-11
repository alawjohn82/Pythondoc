

# DICTIONARY AND LOOP OF PROGRAM

def introDuction():
    
    print("""\n This program ask the user to enter an abbreviation of a phrase 
 or common name in a dictionary and it gives the definition\n""")
    

def abbrevDict():
    
    
    dictWords = {
        "lol": "laugh out loud",
        "fwl": "you kwon what it mean",
        "rofl": "rolling on floor laughing",
        "lmao": "laughing my ass off",
        "hbu": "how about you?",
        "tnt": "tonight",
        "gtg": " got to go",
        "brb": " be right back",
        "afk": "away from keyborad",
        "ty" : "thank you"               
    }
    return dictWords

def loopInputs():
    x = abbrevDict()
    
   
    
    while True :
        user = input("\n what abbreviation you want to know ? ")
       
        question = input("Do you want to continue?(yes or no) ")
        if question.upper() == "NO" :
           print("Goodbye")
           break
        for k, v in x.items():
            if x[user]== v :
                print(f"{user} mean {v}")
              
        
loopInputs()        
       
  

def main():
    pass
"""
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
"""

