print("welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() !="yes":
    quit()

print("Okay! Let's play:)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct')
    score += 1
    
else:
    print("Incorrect!")




answer = input("Who is the best footballer in the world? ")
if answer.lower() == "cristiano ronaldo":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")




answer = input("What is the largest animal in the world? ")
if answer.lower() == "blue whale":

    print('Correct!')
    score += 1
else:
    print("Incorrect!")





answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")




answer = input("Which is the capital city of Nepal? ")
if answer.lower() == "kathmandu":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("you got" + str(score)+"questions correct!")
print("you got" + str((score/5)*100)+"questions correct")