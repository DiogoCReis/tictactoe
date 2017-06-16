class tictactoe:
    def __init__(self,jogador1,jogador2):
        self.jogadas_total = 0
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.tabela = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
        self.jogo()

    def tabela_jogo (self):
        print('  ',self.tabela [1],'|',\
        	self.tabela [2],'|',self.tabela [3] ,"\n",\
        	' ---|---|---','\n',' ',self.tabela[4],\
        	'|',self.tabela [5],'|',self.tabela [6],'\n',' ---|---|---','\n',\
        	' ',self.tabela[7],'|',self.tabela [8],'|',self.tabela [9],'\n')
    def jogo(self):
        i = 0
        vitoria = False
        while not vitoria and i < 9:
            self.jogadas = i
            self.jogadas_total += 1
            self.impar = self.jogadas_total % 2 == 1
            self.jogador_joga()
            if i > 3:
                vitoria = self.check_ganhar()
            i += 1
        self.fim(vitoria)
    def jogador_joga (self):
        self.clear()
        self.tabela_jogo()
        def loop_escolha():
            escolha = input()
            if escolha>'0' and escolha <='9' and len(escolha)==1:
                escolha = eval(escolha)
                if isinstance(self.tabela[escolha],int):
                    return escolha
                else:
                    print('Escolha invalida.\nEscolha uma posição da tabela disponivel.')
                    return loop_escolha()
                    
            else :
                print('Escolha invalida.\nEscolha uma posição da tabela disponivel.')
                return loop_escolha()

        print('\nÉ a vez da/o ', self.meaning_impar(),' jogar.\nEscolha uma posição.')
        escolha = loop_escolha()

        if self.jogadas%2==0:
            self.tabela[int(escolha)]= 'X'
        else:
            self.tabela[int(escolha)]= 'O'


    def check_ganhar(self):
        i = 0
        ganhou = False
        if self.tabela[1] == self.tabela[5] == self.tabela[9]:
            return True
        elif self.tabela [3] == self.tabela[5] == self.tabela[7]:
            return True
        else:
            while not ganhou and i < 3 :
                if self.tabela [3*i+1] == self.tabela [3*i+2] == self.tabela [3*i+3] :
                    ganhou = True
                elif self.tabela [i+1] == self.tabela [3+(i+1)] == self.tabela [6+i+1] :
                    ganhou = True
                i += 1
            return ganhou


    def fim(self,vitoria):
        self.clear()
        self.tabela_jogo()
        if vitoria:
            print ('O jogador ',self.meaning_impar(),' venceu a partida\n')
        else:
            print("Empate\n")
        self.play_again()
        

    def play_again(self):
        escolha = ''
        while escolha != 's' and escolha != 'n':
            escolha = input ('Querem jogar outra vez? s/n\n')
            if escolha == 's':
                self.tabela = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
                self.jogo()
            elif escolha == 'n':
                quit()
            else:
                print ("Resposta invalida tente novamente (s/n)\n")

    def meaning_impar(self):
        if self.impar:
            return self.jogador1
        else:
            return self.jogador2

    def clear(self):
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    

player1 = input("Entrer player  1's name\n")
player2 = input("Enter the second player' name\n")

tictactoe (player1,player2)
