maximum_stories = 30
userstring = input("On what floor of the building is your office?")
usernum = int(userstring)
while usernum > maximum_stories:
    #print("You entered:",usernum,"but there are only",maximum_stories,"floors in this building.  Try again...")
    userstring = input(f'You entered: {usernum} but there are only {maximum_stories} floors in this building.  Try again...\n')
    usernum = int(userstring)

print("Congrats! You work on:",usernum)
