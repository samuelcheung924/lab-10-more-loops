userstring = input("Gimme a number that is greater than 100...")
usernum = int(userstring)

while usernum < 100:
    #print(usernum," is less than 100.  Try again, I've got all day...")
    userstring = input(f'{usernum} is less than 100.  Try again, I have got all day...\n')
    usernum = int(userstring)

print("Congratulations!",usernum,"is greater than 100! Great job!")
