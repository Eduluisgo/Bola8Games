import random

question = input("Pregunta!  ")
random_n = random.randint(1,4)

if random_n == 1:
    print("Claro que si")
elif random_n == 2:
    print("tal lvez")
elif random_n == 3:
    print("No sabria responderte")
else:
    print("No")