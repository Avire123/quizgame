print("Welcome to my Computer Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play: )")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('You are Correct!')
    score += 1
else:
    print('you are Wrong!')
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('You are Correct!')
    score += 1
else:
    print('you are Wrong!')
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('You are Correct!')
    score += 1
else:
    print('you are Wrong!')
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('You are Correct!')
    score += 1
else:
    print('you are Wrong!')
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('You are Correct!')
    score += 1
else:
    print('you are Wrong!')

print("You got " + str(score) + " questions correct! ")
print("You got " + str((score / 4) * 100) + "%.")