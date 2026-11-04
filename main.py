import random
print("Hello, Guesser!")
low = 1
high = 10
win = random.randint(low, high)
while True:
    guess = int(input(f"Ange din gissning mellan {low} och {high} ---->"))
    if guess == win:
        print("Du vann!")
        break
    elif guess < low or guess > high:
        print(f"Gissning utanför {low} och {high} eller ej siffra.")
        continue
    else:
        print("Försök igen!")
        continue

print(guess)