from random import choice

def menu():
    print("---------------Welcome to Motus---------------")
    while(True):
        inp=int(input("1: 1 joueur\n2: 2 joueur\n3: help\n"))
        if( inp in range(1,4) ):
            break
    if(inp==1):
        soloplayer()
    if(inp==2):
        multiplayer()
    if(inp==3):
        help()
        
def help():
    print(" les lettres bien placées sont colorées en rouge, les lettres présentes mais mal placées sont en jaune.")
    inp=input("appuyer sur une touche pour continuer: ")
    menu()

def multiplayer():
    test=True
    while(test==True):
        inp=int(input("veuillez choisir le niveau de difficulté\n1: level 1\n2: level 2\n3: level 3\n4: level 4\n"))
        if( inp in range(1,5) ):
            test=False
    f=open("dicofinal.txt","r")
    lmot=f.readlines()
    f.close()
    
    lmot7=findmot(7,lmot)
    lmot8=findmot(8,lmot)
    lmot9=findmot(9,lmot)
    lmot10=findmot(10,lmot)

    if(inp==1):
        mot=choice(lmot7)
        two_level1(mot)
    if(inp==2):
        mot=choice(lmot8)
        two_level2(mot)
    if(inp==3):
        mot=choice(lmot9)
        two_level3(mot)
    if(inp==4):
        mot=choice(lmot10)
        two_level4(mot)


def two_level1(mot):
    n=7
    vie1=7
    vie2=7

    
    joueur=1
    for i in range(8) :

        if(vie1>0):
            print("\njoueur 1")
            linp1=saisie(n,vie1)
            inp1=linp1[0]
            vie1=linp1[1]

        if(vie2>0):
            print("\njoueur 2")
            linp2=saisie(n,vie2)
            inp2=linp2[0]
            vie2=linp2[1]
            
        if(joueur==1):
            if(vie1>0):
                ch1=verif(mot,inp1)
                vie1-=1
                if(mot==inp1):
                    print("Joueur 1 Vous avez gagner en ",7-vie1," essai")
                    exitt=input("tapez entré pour continuer...")
                    menu()
                    
                elif(vie1>0):
                    print("Joueur 1 il vous reste ",vie1," vie: ",ch1," ")
                    joueur=2

        if (joueur==2):
            if(vie2>0):
                ch2=verif(mot,inp2)
                vie2-=1
                if(mot==inp2):
                    print("Joueur 2 Vous avez gagner en ",7-vie2," essai")
                    exitt=input("tapez entré pour continuer...")
                    menu()
                elif(vie2>0):
                    print("Joueur 2 il vous reste ",vie2," vie: ",ch2," ")
                    joueur=1
        
        
    print("vous n'avez pas deviner le mot c'est: ",mot)
    exitt=input("tapez entré pour continuer...")
    menu()
        
        
def two_level2(mot):
    n=8
    vie1=8
    vie2=8

    
    joueur=1
    for i in range(9) :

        if(vie1>0):
            print("\njoueur 1")
            linp1=saisie(n,vie1)
            inp1=linp1[0]
            vie1=linp1[1]

        if(vie2>0):
            print("\njoueur 2")
            linp2=saisie(n,vie2)
            inp2=linp2[0]
            vie2=linp2[1]
            
        if(joueur==1):
            if(vie1>0):
                ch1=verif(mot,inp1)
                vie1-=1
                if(mot==inp1):
                    print("Joueur 1 Vous avez gagner en ",7-vie1," essai")
                    exitt=input("tapez entré pour continuer...")
                    menu()
                    
                elif(vie1>0):
                    print("Joueur 1 il vous reste ",vie1," vie: ",ch1," ")
                    joueur=2

        if (joueur==2):
            if(vie2>0):
                ch2=verif(mot,inp2)
                vie2-=1
                if(mot==inp2):
                    print("Joueur 2 Vous avez gagner en ",7-vie2," essai")
                    exitt=input("tapez entré pour continuer...")
                    menu()
                elif(vie2>0):
                    print("Joueur 2 il vous reste ",vie2," vie: ",ch2," ")
                    joueur=1
        
        
    print("vous n'avez pas deviner le mot c'est: ",mot)
    exitt=input("tapez entré pour continuer...")
    menu()

def two_level3(mot):
    n=9
    vie1=9
    vie2=9

    
    joueur=1
    for i in range(10) :

        if(vie1>0):
            print("\njoueur 1")
            linp1=saisie(n,vie1)
            inp1=linp1[0]
            vie1=linp1[1]

        if(vie2>0):
            print("\njoueur 2")
            linp2=saisie(n,vie2)
            inp2=linp2[0]
            vie2=linp2[1]
            
        if(joueur==1):
            if(vie1>0):
                ch1=verif(mot,inp1)
                vie1-=1
                if(mot==inp1):
                    print("Joueur 1 Vous avez gagner en ",7-vie1," essai")
                    exitt=input("tapez entré pour continuer...")
                    menu()
                    
                elif(vie1>0):
                    print("Joueur 1 il vous reste ",vie1," vie: ",ch1," ")
                    joueur=2

        if (joueur==2):
            if(vie2>0):
                ch2=verif(mot,inp2)
                vie2-=1
                if(mot==inp2):
                    print("Joueur 2 Vous avez gagner en ",7-vie2," essai")
                    exitt=input("tapez entré pour continuer...")
                    menu()
                elif(vie2>0):
                    print("Joueur 2 il vous reste ",vie2," vie: ",ch2," ")
                    joueur=1
        
        
    print("vous n'avez pas deviner le mot c'est: ",mot)
    exitt=input("tapez entré pour continuer...")
    menu()

def two_level4(mot):
    n=10
    vie1=10
    vie2=10

    
    joueur=1
    for i in range(11) :

        if(vie1>0):
            print("\njoueur 1")
            linp1=saisie(n,vie1)
            inp1=linp1[0]
            vie1=linp1[1]

        if(vie2>0):
            print("\njoueur 2")
            linp2=saisie(n,vie2)
            inp2=linp2[0]
            vie2=linp2[1]
            
        if(joueur==1):
            if(vie1>0):
                ch1=verif(mot,inp1)
                vie1-=1
                if(mot==inp1):
                    print("Joueur 1 Vous avez gagner en ",7-vie1," essai")
                    exitt=input("tapez entré pour continuer...")
                    menu()
                    
                elif(vie1>0):
                    print("Joueur 1 il vous reste ",vie1," vie: ",ch1," ")
                    joueur=2

        if (joueur==2):
            if(vie2>0):
                ch2=verif(mot,inp2)
                vie2-=1
                if(mot==inp2):
                    print("Joueur 2 Vous avez gagner en ",7-vie2," essai")
                    exitt=input("tapez entré pour continuer...")
                    menu()
                elif(vie2>0):
                    print("Joueur 2 il vous reste ",vie2," vie: ",ch2," ")
                    joueur=1
        
        
    print("vous n'avez pas deviner le mot c'est: ",mot)
    exitt=input("tapez entré pour continuer...")
    menu()




        

def findmot(n,lmot):
    res=[]
    for i in lmot:
        if(len(i)==n):
            res.append(i.strip("\n"))
    return res

def soloplayer():
    test=True
    while(test==True):
        inp=int(input("veuillez choisir le niveau de difficulté\n1: level 1\n2: level 2\n3: level 3\n4: level 4\n"))
        if( inp in range(1,5) ):
            test=False
    f=open("dico.txt","r")
    lmot=f.readlines()
    f.close()
    
    lmot7=findmot(7,lmot)
    lmot8=findmot(8,lmot)
    lmot9=findmot(9,lmot)
    lmot10=findmot(10,lmot)

    if(inp==1):
        mot=choice(lmot7)
        one_level1(mot)
    if(inp==2):
        mot=choice(lmot8)
        one_level2(mot)
    if(inp==3):
        mot=choice(lmot9)
        one_level3(mot)
    if(inp==4):
        mot=choice(lmot10)
        one_level4(mot)

def saisie(n,vie):
    test=False
    while(test==False):
        print("saisir un mot de ",n," caractére: ")
        inp=input()
        if(len(inp)==n):
            test=True
        else:
            vie-=1
            print("il vous reste ",vie," vie.")
    linp=[inp,vie]
    return linp

def verif(mot,inp):
    j=0
    ch=""
    d={}
    for elem in mot:
        #parcours de mot
        if elem in d.keys():
            d[elem]+=1
        else:
            d[elem]=1
    for i in inp:
        x=mot[j]
        #print(x)
        if i==x:
            #red
            ch=ch+i.upper()
            if d[i]>1:
                d[i]-=1
            else:
                del d[i]
        elif i in d.keys():
            #yellow
            ch=ch+i
            if d[i]>1:
                d[i]-=1
            else:
                del d[i]
        else:
            #-
            ch=ch+"-"
        j+=1
    
    return ch

def one_level1(mot):
    vie=7
    n=7
    linp=saisie(n,vie)
    inp=linp[0]
    vie=linp[1]
    
    while(vie>0):
        ch=verif(mot,inp)
        vie-=1
        if(mot==inp):
            print("Vous avez gagner en ",7-vie," essai")
            exitt=input("tapez entré pour continuer...")
            menu()
        elif(vie>0):
            print("il vous reste ",vie," vie: ",ch," ")
            linp=saisie(n,vie)
            inp=linp[0]
            vie=linp[1]
    print("vous n'avez pas deviner le mot c'est: ",mot)
    exitt=input("tapez entré pour continuer...")
    menu()
        
def one_level2(mot):
    vie=8
    n=8
    linp=saisie(n,vie)
    inp=linp[0]
    vie=linp[1]
    
    while(vie>0):
        ch=verif(mot,inp)
        vie-=1
        if(mot==inp):
            print("Vous avez gagner en ",7-vie," essai")
            exitt=input("tapez entré pour continuer...")
            menu()
        elif(vie>0):
            print("il vous reste ",vie," vie: ",ch," ")
            linp=saisie(n,vie)
            inp=linp[0]
            vie=linp[1]
    print("vous n'avez pas deviner le mot c'est: ",mot)
    exitt=input("tapez entré pour continuer...")
    menu()

def one_level3(mot):
    vie=9
    n=9
    linp=saisie(n,vie)
    inp=linp[0]
    vie=linp[1]
    
    while(vie>0):
        ch=verif(mot,inp)
        vie-=1
        if(mot==inp):
            print("Vous avez gagner en ",7-vie," essai")
            exitt=input("tapez entré pour continuer...")
            menu()
        elif(vie>0):
            print("il vous reste ",vie," vie: ",ch," ")
            linp=saisie(n,vie)
            inp=linp[0]
            vie=linp[1]
    print("vous n'avez pas deviner le mot c'est: ",mot)
    exitt=input("tapez entré pour continuer...")
    menu()

def one_level4(mot):
    vie=10
    n=10
    linp=saisie(n,vie)
    inp=linp[0]
    vie=linp[1]
    
    while(vie>0):
        ch=verif(mot,inp)
        vie-=1
        if(mot==inp):
            print("Vous avez gagner en ",7-vie," essai")
            exitt=input("tapez entré pour continuer...")
            menu()
        elif(vie>0):
            print("il vous reste ",vie," vie: ",ch," ")
            linp=saisie(n,vie)
            inp=linp[0]
            vie=linp[1]
    print("vous n'avez pas deviner le mot c'est: ",mot)
    exitt=input("tapez entré pour continuer...")
    menu()

#__________________________________________________________Main__________________________________    
menu()




