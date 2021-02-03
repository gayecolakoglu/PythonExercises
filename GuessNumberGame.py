from random import randint

key=1

while key==1:
    count=0
    number = randint(1, 50)
    x = int(input("Please enter 1 to continue the game, 0 to exit the program."))
    if x == 0:
        print("Logging out ...")
        key=0
    elif x==1:
        while count!=5:
            guess=int(input("Please enter a number between 1-50:"))
            if number==guess:
                print("Your",count + 1, ". guess is correct, the chosen number is:", number)
                break
            else:
                if count == 4:
                    print("Your right to guess has expired.")
                    break
                if guess<number :
                    print("Your",count + 1, ". guess is wrong, please enter a higher number!")
                elif guess>number :
                    print("Your",count + 1, ". guess is wrong, please enter a higher number!")
                count+=1