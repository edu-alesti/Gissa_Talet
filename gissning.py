import random
points = 0
guess = 0
q1 = ["Oslo", "Stockholm", "Köpenhamn"]
q2 = ["1914", "1939", "1945"]
q3 = ["Atlanten","Indiska oceanen","Stilla havet"]
random.shuffle(q1)
random.shuffle(q2)
random.shuffle(q3)
print("Vilken huvudstad har sverige?\n", "1. ", q1[0], "\n", "2. " ,q1[1], "\n", "3. ", q1[2])
answer = int(input(""))
for i in range(len(q1)):
    if q1[i] == "Stockholm":
        q1a=i
if answer-1 == q1a:
    print("Rätt!\n")
else:
    print(f"Fel! Rätt svar var {q1[q1a-1]}")

print("Vilket år började 1a världskriget?\n", "1. ", q2[0], "\n", "2. " ,q2[1], "\n", "3. ", q2[2])
answer = int(input(""))
for i in range(len(q2)):
    if q2[i] == "1914":
        q2a=i
if answer-1 == q2a:
    print("Rätt!\n")
else:
    print(f"Fel! Rätt svar var {q2[q2a-1]}")

print("Vad heter världens största hav?\n", "1. ", q3[0], "\n", "2. " ,q3[1], "\n", "3. ", q3[2])
answer = int(input(""))
for i in range(len(q3)):
    if q3[i] == "Stilla havet":
        q3a=i
if answer-1 == q3a:
    print("Rätt!")
else:
    print(f"Fel! Rätt svar var {q3[q3a-1]}")

