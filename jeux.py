import random
a = random.randint (1,100)
tentatives = 0
while 1 :
    tentatives = tentatives + 1
    guess = int(input("Devine le chiffre entre 1 et 100\n"))
    if a == guess :
        print ("gagné au bout de", tentatives,"tentatives, il s'agissait de", a)
        break
    elif guess >= a :
        print ("trop grand")
    elif guess <= a :
        print ("trop petit")
