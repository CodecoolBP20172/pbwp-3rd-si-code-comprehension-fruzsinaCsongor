import random  # imports the "random" module

guessesTaken = 0  # assigns 0 to "guessesTaken" variable

print('Hello! What is your name?')  # prints (outputs) "Hello! What is your name?"
myName = input()  # waits until an input is entered, then it is assigned to "myName" variable

number = random.randint(1, 20)  # assigns a (pseudo-)random integer (from 1 to 20, endpoints included) to "number" variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # outputs the strings in the brackets, "myName" substituted with the input name

while guessesTaken < 6:  # repeatedly executes the statements of the loop while the guesses are less than 6
    print('Take a guess.')  # outputs "Take a guess"
    guess = input()  # waits until an input is entered, then it is assigned to "guess" variable
    guess = int(guess)  # the "guess" input is converted to an integer (from string)

    guessesTaken += 1  # increments "guessesTaken" variable's value by one

    if guess < number:  # if the "guess" input is less than the randomly generated number,
        print('Your guess is too low.')  # then "Your guess is too low" is printed out

    if guess > number:  # if the "guess" input is more than the randomly generated number,
        print('Your guess is too high.')  # then "Your guess is too high" is printed out

    if guess == number:  # if the "guess" input equals the randomly generated number,
        break  # then the while loop is terminated by a break statement

if guess == number:  # if the "guess" input equals to the randomly generated number,
    guessesTaken = str(guessesTaken)  # then the "guessesTaken" variable (which is an integer) is cast to a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # prints out the strings with the input name and the actual number of guesses substituted

if guess != number:  # if the "guess" input does not equal to the randomly generated number,
    number = str(number)  # then number (which is an integer) is cast to a string
    print('Nope. The number I was thinking of was ' + number)  # prints out the strings in the brackets, "number" being substituted with the actual randomly generated number
