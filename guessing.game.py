'''Building a Guessing Game'''

secret_word = "works on my computer"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("Guess the phrase:\nIt's not working...")

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input ("Enter Guess:")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print(" Out of guesses, You Lose! \nCorrect response is \n works on my computer")
else:
    print("You Win!")

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
hints = {1: "Has Spots",
         2: "Is Tall"}
print("Guess The Animal")
while guess != secret_word and not (out_of_guesses):
    # print("guess_count: "+str(guess_count))
    if guess_count < guess_limit:
        if guess_count > 0:
            print(hints[guess_count])
        guess = input ("Enter Guess:")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print(" Out of guesses, You Lose!")
else:
    print("You Win!")