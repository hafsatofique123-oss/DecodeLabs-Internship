print("Welcome to my computer quiz!")
playing=input("Do you want to play?")
if playing!="yes":
    quit()
print("Okay! Let's play:-)")
score=0
answer=input("What is the capital of Pakistan?")
if answer.lower()=="islamabad":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
answer=input("Which plnet is known as the Red Planet?")
if answer.lower()=="mars":
    print("Correct")
    score+=1
else:
    print("Incorrect")
answer=input("What is the largest ocean on the earth?")
if answer.lower()=="pacific Ocean":
    print("Correct")
    score+=1
else:
    print("Incorrect") 
answer=input("Who invented the telephone?")
if answer=="alexander graham bell":
    print("Correct")
    score+=1
else:
    print("Incorrect")
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "%.") 
