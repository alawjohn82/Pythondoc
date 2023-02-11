

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
        "ty": "thank you"
    }
    return dictWords


def loopInputs():
    x = abbrevDict()
    z = list(x.keys())
    index_z = -1

    while True:

        #z =list(x.keys())
        index = 0

        user = input("""\n 
        Tap "exit" to exit the program,
        what abbreviation you want to know ?: """
                     )

        # for k, v in x.items():
        for k in z:
            if k == user:
                #x[user]= v
                #print(f"{user} mean : {x[user]}")
                index_z = index
                #print(k, index)

            index = index + 1

        if index_z == -1:
            print(f"{user} cannot be found,try again")
        else:
            print(f"{user} mean : {x[user]}")

        question = input("Do you want to continue?(yes or no)?: ")

        if question.upper() == "NO":
            print("\n Goodbye!")

            break
        print("\n\t ok, let us start again")


def main():
    introDuction()
    loopInputs()


"""
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
"""
