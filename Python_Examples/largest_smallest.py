import random
a = (1,2,6,7,4,-7)

guess = random.choice(a)
guess1 = random.choice(a)

def min_number():
    global a, guess
    print("Guess")
    print(guess)
    for x in range(len(a)):
        if (guess>a[x]):
            guess = a[x]
        elif (guess<a[x]):
            pass

    return guess
def max_number():
    global a, guess1
    print("Guess1")
    print(guess1)
    maximum = 0
    for x in range(len(a)):
        if (guess1<a[x]):
            maximum = a[x]
        elif (guess1>a[x]):
            pass
        elif (guess1 == a[x]):
            maximum = guess1
    return maximum
def main():
    global a, guess, guess1

    guess = min_number()
    maximum = max_number()

    print ("the smallest number is")
    print(guess)
    print("Largest")
    print(maximum)
main()
