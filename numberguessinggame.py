import random 

number = random.randint(1,100)
attempts = 0

while True:
    guess = int(input("Guess a Number:"))
    attempts +=1

    if guess < number:
     print("Too Low")
     
    elif guess > number:
     print("Too High")
    else:
        print(f"Correct!, you got it in {attempts} attempts")
        break   
