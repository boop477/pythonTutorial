def greeting(name, uppercase=False, smile=False, repeat=1):
    greet_str = "Hello, {}.".format(name)
    if uppercase == True:
        greet_str = greet_str.upper()
    if smile == True: # What will happen if I use 'elif', not 'if' ?
        greet_str = greet_str + " :)"
        
    greet_str = "{} ".format(greet_str) * repeat
    print (greet_str)

def sing():
    print ("Give me chOcOlAte")
