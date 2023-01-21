import random
import time
from math import floor

def play():

    play = True
    campo = geraCampo()
    minas = 0
    acertos = 0
    erros = 0
    for i in range(0, 10): #verifica quantas minas tem no campo
        for j in range(0, 10):
            if (campo[i][j] == "@"):
                minas = minas + 1
    marcacoes = minas
    inicio = time.time()
    while(play):
        mostraCampo(campo, play)
        print("\t\tMarcações restantes: {}".format(marcacoes))

        print("\t\t+======== MENU ========+")
        print("\t\t| 1 - Marcar Campo     |")
        print("\t\t| 2 - Marcar Mina      |")
        print("\t\t| 3 - Desmarcar Mina   |")
        print("\t\t+======================+")
        opc = int(input("\t\tEscolha uma opção: "))

        if(opc == 1):
            while (opc == 1):
                mostraCampo(campo, play)
                print("\tMarcações restantes: {}".format(marcacoes))
                print("\t+============= MARCAR CAMPO =============+")
                print("\t| Digite 0 (ZERO) para sair dessa opção  |")
                print("\t| Digite as coordenadas para marcar      |")
                linha = int(input("\t| Linha: "))
                if(verificaLinha(linha) == "VALIDO"): #chama a funcao verificaLinha
                    coluna = int(input("\t| Coluna: "))
                    if(verificaColuna(coluna) == "VALIDO"): #chama a funcao verificaColuna
                        linha = linha-1
                        coluna = coluna-1
                        if (campo[linha][coluna] == "@"): #verifica se campo selecionado contem mina
                            fim = time.time()
                            milesegundos = minutos = (fim - inicio) / 60
                            milesegundos = (milesegundos - floor(milesegundos)) * 100
                            segundos = minutos - floor(minutos)
                            segundos = 60 * segundos
                            campo[linha][coluna] = "X"
                            play = False
                            mostraCampo(campo, play)
                            print("\t+=========== PERDEU ============+")
                            print("\t| VOCÊ PISOU NA MINA E EXPLODIU |")
                            print("\t+========= FIM DE JOGO =========+")
                            print("\t+--------------------")
                            print("\t| Acertos: {}".format(acertos))
                            print("\t| Erros: {}".format(erros))
                            print("\t| Tempo de jogo: {:.0f}:{:.0f}:{:.0f}".format(minutos, segundos, milesegundos))
                            print("\t+--------------------")
                            break
                        elif (campo[linha][coluna] != "."): #verifica se campo selecionado é vazio (onde estiver o ".", quer dizer que esse campo é vazio)
                            print("\t* Você não pode marcar um campo que ja foi marcado ou revelado *") #se nao for vazio, nao pode marca-lo
                        else:
                            campo = verificarMina(campo, linha, coluna) #chama a funcao verificarMina
                    elif(verificaColuna(coluna) == "SAIR"): #chama a funcao verificaColuna
                        print("\t* SAIU *")
                        break
                    else:
                        print("\t* O número {} é inválido *".format(coluna))
                elif(verificaLinha(linha) == "SAIR"): #chama a funcao verificaLinha
                    print("\t* SAIU *")
                    break
                else:
                    print("\t* O número {} é inválido *".format(linha))

        if(opc == 2):
            while(opc == 2):
                if (marcacoes == 0):
                    print("\t* Suas marcações acabaram, desmarque um campo para poder marcar mais *")
                    break
                else:
                    mostraCampo(campo, play)
                    print("\tMarcações restantes: {}".format(marcacoes))
                    print("\t+============= MARCAR MINA =============+")
                    print("\t| Digite 0 (ZERO) para sair dessa opção |")
                    print("\t| Digite as coordenadas para marcar     |")
                    linha = int(input("\t| Linha: "))
                    if (verificaLinha(linha) == "VALIDO"): #chama a funcao verificaLinha
                        coluna = int(input("\t| Coluna: "))
                        if(verificaColuna(coluna) == "VALIDO"): #chama a funcao verificaColuna
                            linha = linha-1
                            coluna = coluna-1
                            if(campo[linha][coluna] == "@"): #verifica se o campo marcado contem mina
                                campo[linha][coluna] = "A" #se o campo tiver mina, é atribuido o "A", como acerto
                                marcacoes = marcacoes - 1
                                acertos = acertos + 1
                                if(acertos == minas): #verifica se a quantidade de acertos é igual a quantidade de minas
                                    fim = time.time()
                                    play = False
                                    milesegundos = minutos = (fim - inicio) / 60
                                    milesegundos = (milesegundos - floor(milesegundos)) * 100
                                    segundos = minutos - floor(minutos)
                                    segundos = 60 * segundos
                                    mostraCampo(campo, play)
                                    print("\t+========== VENCEU ==========+")
                                    print("\t| VOCÊ MARCOU TODAS AS MINAS |")
                                    print("\t+======= FIM DE JOGO ========+")
                                    print("\t+--------------------")
                                    print("\t| Acertos: {}".format(acertos))
                                    print("\t| Erros: {}".format(erros))
                                    print("\t| Tempo de jogo: {:.0f}:{:.0f}:{:.0f}".format(minutos, segundos, milesegundos))
                                    print("\t+--------------------")
                                    break
                            elif (campo[linha][coluna] != "."): #verifica se campo selecionado é vazio (onde estiver o ".", quer dizer que esse campo é vazio)
                                print("\t* Você não pode marcar um campo que ja foi marcado ou revelado *") #se nao for vazio, nao pode marca-lo
                            else:
                                campo[linha][coluna] = "E" #se o campo selecionado nao contem mina e é vazio, entao é atribuido o "E", como erro
                                marcacoes = marcacoes - 1
                                erros = erros + 1
                        elif(verificaColuna(coluna) == "SAIR"): #chama a funcao verificaColuna
                            print("\t* SAIU *")
                            break
                        else:
                            print("\t* O número {} é inválido *".format(coluna))
                    elif (verificaLinha(linha) == "SAIR"): #chama a funcao verificaLinha
                        print("\t* SAIU *")
                        break
                    else:
                        print("\t* O número {} é inválido *".format(linha))

        if(opc == 3):
            while(opc == 3):
                mostraCampo(campo, play)
                print("\tMarcações restantes: {}".format(marcacoes))
                print("\t+============ DERMARCAR MINA ============+")
                print("\t| Digite 0 (ZERO) para sair dessa opção  |")
                print("\t| Digite as coordenadas para marcar      |")
                linha = int(input("\t| Linha: "))
                if (verificaLinha(linha) == "VALIDO"): #chama a funcao verificaLinha
                    coluna = int(input("\t| Coluna: "))
                    if(verificaColuna(coluna) == "VALIDO"): #chama a funcao verificaColuna
                        linha = linha-1
                        coluna = coluna-1
                        if(campo[linha][coluna] == "A"): #verifica se campo selecionado contem "A", um acerto
                            campo[linha][coluna] = "@" #ao desmarcara um campo que continha mina, é atribuido o "@"
                            marcacoes = marcacoes + 1
                            acertos = acertos - 1
                        elif(campo[linha][coluna] == "E"): #verifica se campo selecionado contem "E", um erro
                            campo[linha][coluna] = "." #ao desmarcara um campo que não continha mina, é atribuido o "." (vazio)
                            marcacoes = marcacoes + 1
                            erros = erros - 1
                        else:
                            print("\t* Você não pode desmarcar um campo que não esteja marcado *") #se o campo ja estiver vazio, voce nao pode desmarca-lo
                    elif(verificaColuna(coluna) == "SAIR"): #chama a funcao verificaColuna
                        print("\t* SAIU *")
                        break
                    else:
                        print("\t* O número {} é inválido *".format(coluna))
                elif (verificaLinha(linha) == "SAIR"): #chama a funcao verificaLinha
                    print("\t* SAIU *")
                    break
                else:
                    print("\t* O número {} é inválido *".format(linha))

def geraCampo(): #funcao que gera o campo minado
    campo = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

    for i in range(0, 10): #percorre a matriz campo
        for j in range(0, 10):
            posicao = random.randrange(1, 5) #gera um numero aleatorio do 1 ao 4
            if(posicao == 2): #se o numero gerado for 2, entao esse campo tera uma mina
                campo[i][j] = "@"

    return campo

def mostraCampo(campo, play): #funcao que printa o campo
    print("\n\n     1   2   3   4   5   6   7   8   9   10")  # printa os números das colunas
    # print("   -----------------------------------------") #descomente para printar a linha do topo
    for i in range(0, 10):
        if (i + 1 < 10):
            print(" {} |".format(i + 1), end="")  # printa os números das linhas do 1 ao 9
        else:
            print("{} |".format(i + 1), end="")  # printa o número 10 da ultima linha
        for j in range(0, 10):
            if(play == False): #verifica se o jogo acabou
                if(campo[i][j] == "."): #se o jogo ja terminou, entao revela todos os campos, printando os "A" de acertos, os "E" de erros e as "@" de minas
                    print("   |", end="")
                else:
                    print(" {} |".format(campo[i][j]), end="")
            elif(campo[i][j] == "A" or campo[i][j] == "E"): #verifica se o campo contem um "A" acerto ou um "E" erro
                print(" # |", end="") #printa o "#" para mostrar um local que o jogador marcou como uma mina, estando ele certo ou errado
            elif(campo[i][j] == "@" or campo[i][j] == "."): #verifica se o campo contem uma mina ou se esta vazio
                print("   |", end="")
            else:
                print(" {} |".format(campo[i][j]), end="")

        print("")
        # print("   -----------------------------------------") #descomente para printar uma linha entre os campos

def verificarMina(campo, linha, coluna): #funcao que verifica quantas minas tem ao redor da posicao selecionada
    count = 0
    for i in range(linha - 1, linha + 2): #percorre uma matriz 3x3 da posicao selecionada, sendo a posicao selecionada o centro
        for j in range(coluna - 1, coluna + 2):
            if (i >= 0 and j >= 0 and i < 10 and j < 10): #verifica se esta percorrendo dentro do campo minado
                if (campo[i][j] == "@" or campo[i][j] == "A"): #se tiver uma mina ou um acerto, entao soma + 1
                    count = count + 1

    if(count == 0): #se nao houver nenhuma mina ao lado, verifica quantas minas tem ao redor das posicoes vizinhas
        campo[linha][coluna] = "=" #atribui o "=", para dizer que é um campo limpo
        for i in range(linha - 1, linha + 2):
            for j in range(coluna - 1, coluna + 2):
                if (i >= 0 and j >= 0 and i < 10 and j < 10):
                    if(campo[i][j] == "."): #se o campo estiver vazio, entao chama a funcao verificarMina novamente
                        campo = verificarMina(campo, i, j) #chama a funcao passando as posicoes vizinhas como parametro
    else:
        campo[linha][coluna] = str(count) #se houver uma ou mais minas ao redor, atribui o valor da quantidade de minas que tem ao redor do campo selecionado
    return campo

def verificaLinha(linha): #verifica a linha digitada
    if (linha == 0): #se for 0 (zero) entao retorna "SAIR"
        return "SAIR"
    elif (linha < 0 or linha > 10): #se for fora do campo minado, retorna "INVALIDO"
        return "INVALIDO"
    else:
        return "VALIDO"

def verificaColuna(coluna): #verifica a coluna digitada
    if (coluna == 0): #se for 0 (zero) entao retorna "SAIR"
        return "SAIR"
    elif (coluna < 0 or coluna > 10): #se for fora do campo minado, retorna "INVALIDO"
        return "INVALIDO"
    else:
        return "VALIDO"

if (__name__ == "__main__"):
        play()
