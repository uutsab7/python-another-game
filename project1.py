import random
lis = ['s','p','r']
chance = 4
no_of_chance = 0
computer_point = 0
timro_point = 0
print("\t \t \t this is scissor paper rock game")
print(" press s for scissor \n p for paper \n r for rock")

'''
0<4- t , 1<4-t 2<4 - t , 3<4- t , 4<4-f
'''

while(no_of_chance<chance):
    _input = input("Scisor, Paper, Rock:")
    _random = random.choice(lis)

    if(_input == _random):
        print("Its a tei bro , no one wins lol")

    elif(_input=="p" and _random=="s"):
        computer_point = computer_point+1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \ n")
        print(f" computer point is {computer_point} your point is {timro_point} \n")

    elif (_input == "p" and _random == "r"):
        timro_point = timro_point+1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print(" you win 1 point \ n")
        print(f" computer point is {computer_point} your point is {timro_point} \n")

    elif (_input == "s" and _random == "r"):
        computer_point = computer_point + 1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print(" computer wins 1 point \ n")
        print(f" computer point is {computer_point} your point is {timro_point} \n")

    elif (_input == "s" and _random == "p"):
        timro_point = timro_point + 1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print(" you wins 1 point \ n")
        print(f" computer point is {computer_point} your point is {timro_point} \n")

    elif (_input == "r" and _random == "s"):
        timro_point = timro_point+1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print(" you win 1 point \ n")
        print(f" computer point is {computer_point} your point is {timro_point} \n")

    elif (_input == "r" and _random == "p"):
        computer_point = computer_point + 1
        print(f"your guess is {_input} and computer guess is {_random} \n")
        print(" computer wins 1 point \ n")
        print(f" computer point is {computer_point} your point is {timro_point} \n")

    else:
        print(" its a wrong input \ n")


    no_of_chance = no_of_chance+1
    print(f"{no_of_chance} change is already played  out of {chance} chance for you now \n")

#out of while loop
print("game over")

if(computer_point == timro_point):
    print("its a tie")

elif(computer_point>timro_point):
    print("computer wins....you loose")

elif(timro_point>computer_point):
    print("you win....congratulations")

print(f" finally, your point is {timro_point} computer point is {computer_point}")


# python
# html,css
# django
# mysql/postgres
# django rest framework-api
# github-versin control
# aws-hostin
# -software developer- software engineer







