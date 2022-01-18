from random import choice

matriz = []

for i in range(3):
    row= []
    for x in range(3):
        row.append('')
    matriz.append(row)

bot1 = 'X'
bot2 = 'O'

chooses = ['A1','A2', 'A3','B1', 'B2', 'B3', 'C1', 'C2', 'C3']

counter = 1
print('    A   B   C')
for i in matriz:
    print(counter, i)
    counter += 1



while True:
    bot1_choice = choice(chooses)
    chooses.remove(bot1_choice)

    if bot1_choice == 'A1': #first collum
        matriz[0][0] = bot1      
    elif bot1_choice == 'A2':
        matriz[0][1] = bot1   
    elif bot1_choice == 'A3':
        matriz[0][2] = bot1 
    elif bot1_choice == 'B1': #second collum
        matriz[1][0] = bot1
    elif bot1_choice == 'B2':
        matriz[1][1] = bot1
    elif bot1_choice == 'B3':
        matriz[1][2] = bot1  
    elif bot1_choice == 'C1': #third collum
        matriz[2][0] = bot1
    elif bot1_choice == 'C2':
        matriz[2][1] = bot1
    elif bot1_choice == 'C3':
        matriz[2][2] = bot1
    
    for i in matriz:
        print(i)
    print()


    if matriz[0][0] == bot1 and matriz[1][0] == bot1 and matriz[2][0] == bot1 or matriz[0][0] == bot1 and matriz[0][1] == bot1 and matriz[0][2] == bot1 or matriz[1][0] == bot1 and matriz[1][1] == bot1 and matriz[1][2] == bot1 or matriz[2][0] == bot1 and matriz[2][1] == bot1 and matriz [2][2] == bot1 or matriz[0][1] == bot1 and matriz[1][1] == bot1 and matriz[2][1] == bot1 or matriz[0][2] == bot1 and matriz[1][2] == bot1 and matriz [2][2] == bot1 or matriz[0][0] == bot1 and matriz[1][1] == bot1 and matriz [2][2] == bot1 or matriz[0][2] == bot1 and matriz[1][1] == bot1 and matriz[2][0] == bot1:
        print('Bot1 Wins')
        break
    elif matriz[0][0] == bot2 and matriz[1][0] == bot2 and matriz[2][0] == bot2 or matriz[0][0] == bot2 and matriz[0][1] == bot2 and matriz[0][2] == bot2 or matriz[1][0] == bot2 and matriz[1][1] == bot2 and matriz[1][2] == bot2 or matriz[2][0] == bot2 and matriz[2][1] == bot2 and matriz [2][2] == bot2 or matriz[0][1] == bot2 and matriz[1][1] == bot2 and matriz[2][1] == bot2 or matriz[0][2] == bot2 and matriz[1][2] == bot2 and matriz [2][2] == bot2 or matriz[0][0] == bot2 and matriz[1][1] == bot2 and matriz [2][2] == bot2 or matriz[0][2] == bot2 and matriz[1][1] == bot2 and matriz[2][0] == bot2:
        print('Bot2 Wins')
        break
    else:
        if len(chooses) == 0:
            print('Velha')
            break

    bot2_choice = choice(chooses)
    chooses.remove(bot2_choice)

    if bot2_choice == 'A1': #first collum
        matriz[0][0] = bot2      
    elif bot2_choice == 'A2':
        matriz[0][1] = bot2   
    elif bot2_choice == 'A3':
        matriz[0][2] = bot2 
    elif bot2_choice == 'B1': #second collum
        matriz[1][0] = bot2
    elif bot2_choice == 'B2':
        matriz[1][1] = bot2
    elif bot2_choice == 'B3':
        matriz[1][2] = bot2  
    elif bot2_choice == 'C1': #third collum
        matriz[2][0] = bot2
    elif bot2_choice == 'C2':
        matriz[2][1] = bot2
    elif bot2_choice == 'C3':
        matriz[2][2] = bot2

    for i in matriz:
        print(i)
    print()
