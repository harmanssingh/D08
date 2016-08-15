import random
import sys

def generate_random_number(numberofdigits):
    randnum=0
    for num in range(numberofdigits):
        randnum*=10
        randnum+=random.randint(0,9)
    return randnum

def guess_random_number(randnum,guess):
    if guess == randnum:
        return 0
    elif guess < randnum:
        return -1
    else:
        return 1

def main():
    try:
        numdigits=int(sys.argv[1])
    except:
        numdigits=1
    random_number=generate_random_number(numdigits)
    n=0
    prompt="\nEnter a {}-digit integer: ".format(repr(numdigits))
    while True:
        try:
            guess=int(input(prompt))
        except:
            prompt="Enter an integer value only. Try again: "
            n+=1
            continue
        if 10**(numdigits-1) <= guess < 10**numdigits:
            guesscheck=guess_random_number(random_number,guess)
            n+=1
            if guesscheck == 0:
                if n == 1:
                    print("\nCongratulations. You guessed the correct number in 1 try")
                else:
                    print("\nCongratulations. You guessed the correct number in {} tries".format(repr(n)))
                break
            elif guesscheck == -1:
                prompt="\nTry again. Guess a higher number: "
            else:
                prompt="\nTry again. Guess a lower number: "
        else:
            prompt="Enter a valid {}-digit integer: ".format(repr(numdigits))
            n+=1

if __name__ == "__main__":
        main()
