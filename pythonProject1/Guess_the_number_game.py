n = 10
num_of_guess = 5
guess_taken = 0
while num_of_guess:
    i = int(input("Guess the number:"))
    if i == n:
        print("You answer is correct")
        guess_taken = guess_taken + 1
        print("number of guess taken:", guess_taken)
        break
    elif i < n:
        print("your number is smaller")
        num_of_guess = num_of_guess - 1
        print("guess left", num_of_guess)
        guess_taken = guess_taken + 1
    elif i > n:
        print("your number is greater")
        num_of_guess = num_of_guess - 1
        print("guess left", num_of_guess)
        guess_taken = guess_taken + 1
    if num_of_guess == 0:
        print("Game Over")
