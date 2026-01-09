tasks = ["Wake up", "Brush teeth", "Study Python", "Go to gym", "Sleep"]
#declaring function in py
def myfunc(giveIndex,Values):
    print(giveIndex,Values)
for i , items in enumerate(tasks,start=1):
     myfunc(i,items)
answer = int(input("Which task number do you want to mark as done?"))
print(f"Task {answer} is completed")
# error during prohrams 
# range only works with integeres range(list) ,range(dict) gives error 
# if want to work with varibles use enumerate;

#2] Prime number 
import math
n =19
if(n ==1 ):
   True
if(n<1):
    False
for i in range(2,int(math.sqrt(n)) +1 ):
    if(n%i==0):
        print("not prime")
        break
    else:
     print("prime ")
        