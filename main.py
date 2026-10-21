''' 
-1 for water
0 for gun
1 for snake
'''
import random

computer=random.choice([-1,0,1])
youstr=input("enter your choice : ")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}

you=youdict[youstr]

print(f"your choice = {reversedict[you]}\ncomputer choice = {reversedict[computer]}")

if(computer==you):
    print("its a draw")
else:
    if(computer==-1 and you==1):
        print("comgratulations,you won !")
    elif(computer==-1 and you==0):
        print("bad luck,you lose")
    elif(computer==1 and you==-1):
        print("bad luck, you lose")
    elif(computer==1 and you==0):
        print("congratulations,you won!")
    elif(computer==0 and you==-1):
        print("comgratulations,you won !")
    elif(computer==0 and you==1):
        print("bad luck,you lose")
    else:
        print("something went wrong")