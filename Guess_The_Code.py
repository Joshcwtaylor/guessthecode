import random

TRIES = 5
CODE_LENGTH = 3
LETTERS = ["A", "B"]


def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        selected_letter = random.choice(LETTERS)
        code.append(selected_letter)
    
    return code


def guess_code():    
    while True:
        guess = input("Guess the code: ").upper().split(" ")
        return guess  
    

def check_code(guess, code):
    correct_pos = 0
    for guess_letter, real_letter in zip(guess, code):
        if guess_letter == real_letter:
            correct_pos += 1

    return correct_pos

def main():
    print(f"Can you guess the correct code? You have {TRIES} to guess it correctly or else this program will self destruct!")
    print(f"The code will be {CODE_LENGTH} letters long made up of the letters{LETTERS}, GOOD LUCK!")
    print("There must be a space between each letter! ")
    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos = check_code(guess, code)
        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries! Visual Studio is safe for another day!")
            break
            
        print("That is incorrect guess again")
        
    else:
        print("You ran out of tries, the code was:", *code)
        print("Visual studio will explode in 5 seconds!")
            
print("Thanks for playing!")


main()
