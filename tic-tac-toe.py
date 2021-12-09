from random import choice
import os

class TicTacToe:


    def __init__(self, player_option, bot_play):

        self.player_option = player_option
        self.bot_play = bot_play

    def play_tic_tac_toe(self):

        #creating matriz
        self.matriz = []
        for y in range(3): 
            row = []
            for x in range(3):
                row.append('')
            self.matriz.append(row)

        def print_clear():
            os.system('cls')
            for row in self.matriz:
                    print(row)


        def player_time(type_str): #Put 'X' or 'O' in matriz
            if player == 'A1': #first collum
                if self.matriz[0][0] == '': 
                    self.matriz[0][0] = type_str      
            elif player == 'A2':
                if self.matriz[0][1] == '': 
                    self.matriz[0][1] = type_str   
            elif player == 'A3':
                if self.matriz[0][2] == '': 
                    self.matriz[0][2] = type_str 
            elif player == 'B1': #second collum
                if self.matriz[1][0] == '': 
                    self.matriz[1][0] = type_str
            elif player == 'B2':
                if self.matriz[1][1] == '': 
                    self.matriz[1][1] = type_str
            elif player == 'B3':
                if self.matriz[1][2] == '': 
                    self.matriz[1][2] = type_str  
            elif player == 'C1': #third collum
                if self.matriz[2][0] == '': 
                    self.matriz[2][0] = type_str
            elif player == 'C2':
                if self.matriz[2][1] == '': 
                    self.matriz[2][1] = type_str
            elif player == 'C3':
                if self.matriz[2][2] == '': 
                    self.matriz[2][2] = type_str

        print('   A   B   C')
        cont = 1
        for collum in self.matriz:
            print(cont ,collum)
            cont += 1

        array_play = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'] #possible plays

        possibilidades = set()
        for i in array_play:
            possibilidades.add(i)

        while True:

            player = input(f'Position to put "{self.player_option}": ').upper()
            if player in possibilidades:
                possibilidades.remove(player)
                index = array_play.index(player)
                array_play.pop(index)
                player_time(self.player_option)
            else:
                print('try again! The possibilitys are: ', possibilidades)
                player = input('Position to put "X": ').upper()
                if player not in possibilidades:
                    print('You error 2 times! You lose!')
                    break
                else:
                    possibilidades.remove(player)
                    player_time(self.player_option)

            print_clear()

            if len(possibilidades) == 0:
                break
            
            player = choice(array_play)
            index = array_play.index(player)
            array_play.pop(index)
            possibilidades.remove(player)
            player_time(self.bot_play)

            print_clear()

            if self.matriz[0][0] == self.player_option and self.matriz[1][0] == self.player_option and self.matriz[2][0] == self.player_option or self.matriz[0][0] == self.player_option and self.matriz[0][1] == self.player_option and self.matriz[0][2] == self.player_option or self.matriz[1][0] == self.player_option and self.matriz[1][1] == self.player_option and self.matriz[1][2] == self.player_option or self.matriz[2][0] == self.player_option and self.matriz[2][1] == self.player_option and self.matriz [2][2] == self.player_option or self.matriz[0][1] == self.player_option and self.matriz[1][1] == self.player_option and self.matriz[2][1] == self.player_option or self.matriz[0][2] == self.player_option and self.matriz[1][2] == self.player_option and self.matriz [2][2] == self.player_option or self.matriz[0][0] == self.player_option and self.matriz[1][1] == self.player_option and self.matriz [2][2] == self.player_option or self.matriz[0][2] == self.player_option and self.matriz[1][1] == self.player_option and self.matriz[2][0] == self.player_option:
                print('Player Wins')
                break
            elif self.matriz[0][0] == self.bot_play and self.matriz[1][0] == self.bot_play and self.matriz[2][0] == self.bot_play or self.matriz[0][0] == self.bot_play and self.matriz[0][1] == self.bot_play and self.matriz[0][2] == self.bot_play or self.matriz[1][0] == self.bot_play and self.matriz[1][1] == self.bot_play and self.matriz[1][2] == self.bot_play or self.matriz[2][0] == self.bot_play and self.matriz[2][1] == self.bot_play and self.matriz [2][2] == self.bot_play or self.matriz[0][1] == self.bot_play and self.matriz[1][1] == self.bot_play and self.matriz[2][1] == self.bot_play or self.matriz[0][2] == self.bot_play and self.matriz[1][2] == self.bot_play and self.matriz [2][2] == self.bot_play or self.matriz[0][0] == self.bot_play and self.matriz[1][1] == self.bot_play and self.matriz [2][2] == self.bot_play or self.matriz[0][2] == self.bot_play and self.matriz[1][1] == self.bot_play and self.matriz[2][0] == self.bot_play:
                print('Bot Wins')
                break
            else:
                if len(possibilidades) == 0:
                    print('Velha')
                    break


player_option = input('Do You want "O" or "X": ').upper()
if player_option == 'X': 
    bot_play = 'O' 
elif player_option == 'O': 
    bot_play = 'X' 
else: 
    print('Options is invalid')

if __name__ == '__main__':
    p1 = TicTacToe(player_option, bot_play)
    p1.play_tic_tac_toe()
