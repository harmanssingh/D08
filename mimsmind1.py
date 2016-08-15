import random
import sys

import copy

def generate_random_number(numberofdigits):
    randnum=0
    for num in range(numberofdigits):
        randnum*=10
        randnum+=random.randint(0,9)
    return randnum

def digits_of_number(num):
    list1=[]
    while num >= 1:
        num1=num%10
        num=int(num/10)
        list1.append(num1)
    list1.reverse()
    return list1

def guess_random_number(randnumlist,guesslist):
    bulls=0
    cows=0
    randnumcheck=copy.deepcopy(randnumlist)
    guesscheck=copy.deepcopy(guesslist)
    for n in range(len(randnumcheck)):
        if guesscheck[n] == randnumcheck[n]:
            bulls+=1
            randnumcheck[n] = 'checked'
    for n in range(len(randnumcheck)):
        if not randnumcheck[n] == 'checked':
            if guesscheck[n] in randnumcheck:
                cows+=1
    cowsbulls=(bulls,cows)
    return cowsbulls

def main():
    try:
        numdigits=int(sys.argv[1])
    except:
        numdigits=3
    random_number=generate_random_number(numdigits)
    n=0
    prompt="\nEnter a {}-digit integer: ".format(repr(numdigits))
    maxtries=2**numdigits+numdigits
    while n < maxtries:
        try:
            guess=int(input(prompt))
        except:
            prompt="Enter an integer value only. Try again: "
            n+=1
            continue
        if 10**(numdigits-1) <= guess < 10**numdigits:
            guesscheck=guess_random_number(digits_of_number(random_number),digits_of_number(guess))
            n+=1
            if guesscheck[0] == numdigits:
                if n == 1:
                    print("\nCongratulations. You guessed the correct number in 1 try")
                else:
                    print("\nCongratulations. You guessed the correct number in {} tries".format(repr(n)))
                break
            else:
                prompt="\n{} bull(s), {} cow(s). Try again: ".format(repr(guesscheck[0]),repr(guesscheck[1]))
        else:
            prompt="Enter a valid {}-digit integer: ".format(repr(numdigits))
            n+=1
    else:
        print("\nYou have exceeded the maximum number of trials. Good luck next time.")

if __name__ == "__main__":
        main()
