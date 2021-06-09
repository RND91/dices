import random
import sys
ans = "yes"

def rolling():
    for i in range (sys.maxsize**10):
        if i>=1:
            dice1=random.randint(1,6)
            print(dice1)
            ans=input("do you want to roll again? Answer in yes or no: ")
            
            if ans =="yes":
                dice1=dice1=random.randint(1,6)
                #print(dice1)
                
            else:
               print("ok byee")
               break
rolling()           

            


