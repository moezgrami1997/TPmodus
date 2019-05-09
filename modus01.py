def menu():
    print("---------------Welcome to Motus---------------")
    test=True
    while(test==True):
        inp=int(input("1: 1 joueur\n2: 2 joueur\n3: help\n"))
        if( inp in range(1,4) ):
            test=False
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

def findmot(n,mot):
    res=[]
    for i in mot:
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
    mot=f.readlines
    f.close()
    
    mot7=findmot(7,mot)
    mot8=findmot(8,mot)
    mot9=findmot(9,mot)
    mot10=findmot(10,mot)

    if(inp==1):
        mot=cherchemot(7)
        one_level1(mot)
    if(inp==2):
        mot=cherchemot(8)
        one_level2(mot)
    if(inp==3):
        mot=cherchemot(9)
        one_level3(mot)
    if(inp==4):
        mot=cherchemot(10)
        one_level4(mot)

def saisie(n):
    test=False
    while(test==False):
        print("saisir un mot de ",n," caractére: ")
        inp=input()
        if(len(inp)==n):
            test=True
    return inp

def verif(mot,inp):
    j=0
    ch=""
    for i in inp:
        if(i==mot[j]):
            #red
            ch=ch+i
        elif(i in mot):
            #yellow
            ch=ch+i
        else:
            #-
            ch=ch+"-"
    
    return ch

def one_level1(mot):
    vie=5
    n=7
    inp=saisie(n)
    
    while(vie>0):
        ch=verif(mot,inp)
        vie-=1
        print("il vous reste ",vie," vie: ",ch," ")
        if(mot==inp):
            print("Vous avez gagner en ",5-vie," essai")
            exitt=input("tapez entré pour continuer...")
            menu()
        elif(vie>0):
            inp=saisie(n)
    print("vous n'avez pas deviner le mot c'est: ",mot)
    exitt=input("tapez entré pour continuer...")
    menu()
        
def one_level2(mot):
    vie=7
    n=8
    inp=saisie(n)
    
    while(vie>0):
        ch=verif(mot,inp)
        vie-=1
        print("il vous reste ",vie," vie: ",ch," ")
        if(mot==inp):
            print("Vous avez gagner en ",7-vie," essai")
            exitt=input("tapez entré pour continuer...")
            menu()
        elif(vie>0):
            inp=saisie(n)
    print("vous n'avez pas deviner le mot c'est: ",mot)
    exitt=input("tapez entré pour continuer...")
    menu()

def one_level3(mot):
    vie=9
    n=9
    inp=saisie(n)
    
    while(vie>0):
        ch=verif(mot,inp)
        vie-=1
        print("il vous reste ",vie," vie: ",ch," ")
        if(mot==inp):
            print("Vous avez gagner en ",9-vie," essai")
            exitt=input("tapez entré pour continuer...")
            menu()
        elif(vie>0):
            inp=saisie(n)
    print("vous n'avez pas deviner le mot c'est: ",mot)
    exitt=input("tapez entré pour continuer...")
    menu()

def one_level4(mot):
    vie=12
    n=10
    inp=saisie(n)
    
    while(vie>0):
        ch=verif(mot,inp)
        vie-=1
        print("il vous reste ",vie," vie: ",ch," ")
        if(mot==inp):
            print("Vous avez gagner en ",12-vie," essai")
            exitt=input("tapez entré pour continuer...")
            menu()
        elif(vie>0):
            inp=saisie(n)
    print("vous n'avez pas deviner le mot c'est: ",mot)
    exitt=input("tapez entré pour continuer...")
    menu()

menu()
