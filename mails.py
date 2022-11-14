import random, csv

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

with open("data.csv",'w',newline='') as saida:
    escrever = csv.writer(saida)
    for i in range(20):
        letra1 = random.choice(letters)
        letra2 = random.choice(letters)
        letra3 = random.choice(letters)
        letra4 = random.choice(letters)
        letra5 = random.choice(letters)
        nome = letra1 + letra2 + letra3 + letra4 + letra5
        escrever.writerow([nome])
        i =+ 1
