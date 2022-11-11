import random

print("I challenge you to the game of hand cricket!")
print("You will be batting first.")
usermaxball = int(input("How many runs do you want to fix as the maximum? "))
userin = 0
pcin = 0
userscore = 0
pcscore = 0

print("\n\n")
#User batting 
while True:
    userin = int(input("Enter ur num: "))
    pcin = random.randint(1,usermaxball)
    userscore += userin
    print(f"User: {userscore}")
    print(f"PC: {pcin}")
        
    if userin > usermaxball:
        print("invalid input")
        break
        
    if userin == pcin:
        print("OUTTT")
        print(f"User: {userscore}")
        break

print("\n\n")
#User Bowling
print("Now you will be bowling")
while True:
    userin = int(input("Enter ur num: "))
    pcin = random.randint(1,usermaxball)
    pcscore += pcin
    print(f"User: {userscore}")
    print(f"PC: {pcin}")
        
    if userin > usermaxball:
        print("invalid input")
        break
        
    if userin == pcin:
        print("End of the Battle")
        print(f"PC: {pcscore}")
        break

print("Final Scores")
print(f"User: {userscore}")
print(f"PC: {pcscore}")
print("\n\n")

if userscore > pcscore:
    print("You won the game!")
elif userscore < pcscore:
    print("You lost the game!")
else:
    print("It's a tie!")