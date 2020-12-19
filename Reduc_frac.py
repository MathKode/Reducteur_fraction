"""
Ce code est un code permettant de donner la fraction réduite au max de 2 nombre
The aim of this code is to give the irreductible fraction of 2 numbers
"""

def reduc(nb1,nb2) :
    # Nb1 est le numérateur ; Nb2 est le dénominateur
    Ls_nb1 = [] # Liste contenant tous les diviseur du nb1
    Ls_nb2 = []
    nb = 1
    while True :
        if int(nb1) % nb == 0 :
            Ls_nb1.append(nb)
        if int(nb2) % nb == 0 :
            Ls_nb2.append(nb)
        if nb > int(nb1) and nb > int(nb2) :
            break
        nb+=1
    Ls_nb1 = Ls_nb1[::-1] #retourne la liste (grand -> petit)
    Ls_nb2 = Ls_nb2[::-1]
    print(Ls_nb1)
    print(Ls_nb2)
    #test pour les diviseur de nb1 lequel fonctionne avec nb2
    com_div = 0
    for div_nb1 in Ls_nb1 :
        if div_nb1 in Ls_nb2 :
            com_div = div_nb1
            break
    print(com_div) #diviseur commun
    nb1 = int(int(nb1) / com_div)
    nb2 = int(int(nb2) / com_div)
    print(nb1,'I',nb2)

if __name__ == "__main__":
    while True :
        nb1 = input("nb1 -> ")
        nb2 = input("nb2 -> ")
        reduc(nb1,nb2)