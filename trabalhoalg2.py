# Importações -----------------------------------------------------------------------------

from time import sleep
from cores import *
import pygame

# Contadores -------------------------------------------------------------------------------

cont_pontos = 0
cont_lista = 0

# Listas ----------------------------------------------------------------------------------

lista_respostas = []
lista_respostas_certas = [1, 3, 4, 3, 5, 2, 5, 3, 1, 4]
lista_correto_errado = []
lista_pontuacao_jogadores = []

# Função das Perguntas -----------------------------------------------------------------------

def pergunta(resposta_certa, pergunta, errada):
    while True:
        try:
            question = int(input(pergunta))

        except (IndexError, ValueError, TypeError):
            pygame.init()
            pygame.mixer.music.load('sirene.mp3')
            pygame.mixer.music.play()
            errado('ERRO: Por favor, digite um valor válido.')
            sleep(1.5)
            continue

        if question <= 0 or question > 5:
            pygame.init()
            pygame.mixer.music.load('sirene.mp3')
            pygame.mixer.music.play()
            errado('ERRO: Por favor, digite um valor válido.')
            sleep(1.5)
            continue
        else:
            if question == resposta_certa:

                pygame.init()
                pygame.mixer.music.load('Level Up! - Pokémon Diamond _ Pearl _ Platinum.mp3')
                pygame.mixer.music.play()

                lista_respostas.append(question)

                global cont_pontos
                cont_pontos += 1
                correto('Correto!')

                sleep(3)
                break
            else:

                pygame.init()
                pygame.mixer.music.load('Spongebob disappointed sound (Steel Sting).mp3')
                pygame.mixer.music.play()

                lista_respostas.append(question)

                errado('Errado!')

                sleep(2)

                print(errada)
                vermelho('---' * 30)

                sleep(5)
                break

def username(registrar, pergunta_usuario):
    while True:

        try:
            registro = str(input(registrar)).upper()[0]

        except (IndexError, ValueError, TypeError):
            vermelho('ERRO: por favor, digite uma resposta válida')
            continue

        else:

            if registro not in 'SN':
                vermelho('ERRO: por favor, digite uma resposta válida')
                continue

            elif registro == 'N':
                break

            elif registro == 'S':
                while True:
                    try:
                        usuario = str(input(pergunta_usuario))

                    except (IndexError, ValueError, TypeError):
                        vermelho('ERRO: por favor, digite um nome de usuário')
                        continue

                    else:
                        if usuario in lista_pontuacao_jogadores:
                            errado('ERRO: nome de usuário já existente. Por favor, digite outro nome.')
                            continue
                        else:
                            lista_pontuacao_jogadores.append([cont_pontos, usuario])
                            break
        break

def opcoes(opcoes):
    while True:
        azul('> MENU PRINCIPAL')
        print()
        print('Digite o número correspondente a opção que deseja.')
        try:
            global opcao
            opcao = int(input(opcoes))

        except (IndexError, ValueError, TypeError):
            errado('ERRO: Por favor, digite uma opção válida.')
            continue
        else:
            if opcao <= 0 or opcao > 5:
                errado('ERRO: Por favor, digite uma opção válida.')
                continue
            else:
                break

def retorno(msg):
    while True:
        try:
            retorno = int(input(msg))

        except (IndexError, ValueError, TypeError):
            vermelho('ERRO: Digite um valor válido.')
            continue

        else:
            if retorno != 0:
                vermelho('ERRO: Digite um valor válido.')
                continue
            else:
                break

# Menu Principal ---------------------------------------------------------------------------------

while True:

    titulo_2('QUIZ SOBRE FILMES')


    opcoes("""1) Jogar o Quiz
2) Ranking dos Jogadores
3) Créditos
4) Fechar o Jogo

> Opção: """
)

# Quiz dos Filmes ------------------------------------------------------------------------

    if opcao == 1:


        titulo_2('BEM VINDO AO QUIZ SOBRE FILMES!!')

        print("""

Descubra o filme através de uma breve descrição!

O objetivo do Quiz é avaliar seu conhecimento cultural sobre filmes!

Você terá que responder 10 perguntas e cada pergunta valerá 1 ponto!
Ao final do Quiz, será mostrada a sua classificação.

        """)

        sleep(5)

        preto('===' * 40)

        azul('--> REGRAS')

        print("""

- O jogador deverá responder as 10 perguntas, uma a uma;
- O jogador não poderá pular nenhuma pergunta;
- O jogador não poderá pesquisar a descrição do filme na internet. O jogo é justamente para avaliar o nível de 
conhecimento do entretenimento cinematográfico através dos anos de experiência com o cinema;
- Cada pergunta respondida de forma correta equivale à 1 ponto;
- A pontuação máxima será 10 pontos.


        """)

        sleep(10)

# Início do jogo -----------------------------------------------------------------------------

        preto('===' * 40)

        azul('> QUESTÃO 1')

        pergunta(1, """

- Um pai de família comum que vê sua vida virar de ponta a cabeça após ganhar na loteria. Levando uma vida de
ostentação ao lado da mulher, ele gasta todo o dinheiro em 15 anos. Ao se ver quebrado,
ele aceita a ajuda do vizinho, um consultor de finanças super burocrático e que por sinal vive seu próprio
drama ao enfrentar uma crise no casamento com sua esposa. Tentando evitar que sua esposa descubra a
nova situação financeira, afinal ela está grávida do terceiro filho não pode passar por fortes emoções, ele se
envolve em várias confusões para fingir que tudo continua bem. Para isso, conta com ajuda do melhor amigo, e dos filhos.

1) Até que a $orte nos Separe
2) Se Beber Não Case
3) Um Candidato Honesto
4) Até que a $orte nos Separe 2
5) Click

> Resposta: """, """Alternativa errada! A correta é a número 1. 
O filme Até que a $orte nos Separe de 2012 tem como protagonista Tino, interpretado por Leandro Hassum.""")

# ============================================================================

        preto('===' * 40)

        azul('> QUESTÃO 2')
        pergunta(3, """

- Um jovem que aceitou ser voluntário em uma série de experiências que visam criar o supersoldado americano. Os militares
conseguem transformá-lo em uma arma humana, mas logo percebem que o supersoldado é valioso demais para pôr em risco
na luta contra os nazistas. Desta forma, ele é usado como uma celebridade do exército, marcando presença em paradas
realizadas pela Europa no intuito de levantar a estima dos combatentes. Para tanto passa a usar uma vestimenta marcante.
Só que um plano nazista faz com que o soldado entre em ação e assuma a alcunha, usando seus dons para combatê-los em
plenas trincheiras da guerra.

1) Rambo: Programado Para Matar
2) Até o Último Homem
3) Capitão América: O Primeiro Vingador
4) Exterminador do Futuro
5) X-men Origens: Wolverine

> Resposta: """, """Alternativa errada! A correta é a número 3. O filme Capitão América: O Primeiro Vingador de 
2011 narra a origem do Capitão América, interpretado por Chris Evans.""")

# ============================================================================

        preto('===' * 40)

        azul('> QUESTÃO 3')
        pergunta(4, """

- Após ganhar a Copa Pistão um famoso carro e sua equipe retornam a Radiator Springs para descansar.
Lá ele reencontra seu amigo, que aguarda ansioso pelo retorno. Pouco depois de sua chegada ele é reconhecido
por um grandioso evento onde os competidores usam um combustível alternativo. Após ser provocado ele resolve competir.
Ele leva seu amigo como acompanhante, mas ele acaba sendo confundido com um espião. Agora seu amigo deve lidar com dois
carros que tentam descobrir um segredo.

1) Carros
2) Turbo
3) Need For Speed
4) Carros 2
5) Velozes e Furiosos 2

> Resposta: """, """Alternativa errada! A correta é a número 4. O filme Carros 2 de 2011 é a sequência do grande
sucesso Carros com seu protagonista icônico Lightning McQueen""")

# ============================================================================

        preto('===' * 40)

        azul('> QUESTÃO 4')
        pergunta(3, """

- No exuberante mundo alienígena de Pandora vivem os Na'vi, seres que parecem ser primitivos,
mas são altamente evoluídos. Como o ambiente do planeta é tóxico, foram criados os avatares,
corpos biológicos controlados pela mente humana que se movimentam livremente em Pandora. Jake Sully, um
ex-fuzileiro naval paralítico, volta a andar através de um avatar e se apaixona por uma Na'vi. Esta paixão leva
Jake a lutar pela sobrevivência de Pandora.

1) Elysium
2) Guardiões da Galáxia
3) Avatar
4) O Predador
5) Eternos

> Resposta: """, """Alternativa errada! A correta é a número 3. A maior bilheteria do mundo, Avatar de 2009 tem 
como protagonista o ex-fuzileiro naval Jake Sully.""")

# ============================================================================

        preto('===' * 40)

        azul('> QUESTÃO 5')
        pergunta(5, """

- Marty McFly, um adolescente de uma pequena cidade californiana, é transportado para a década de 1950 quando
a experiência do excêntrico cientista Doc Brown dá errado. Viajando no tempo em um carro modificado, Marty 
conhece versões jovens de seus pais e precisa fazer com que eles se apaixonem, ou então ele deixará de existir. 
Para complicar, Marty precisa voltar para casa a tempo de salvar o cientista. 


1) Efeito Borboleta
2) Efeito Dominó
3) O Mistério da Libélula
4) Click
5) De Volta para o Futuro

> Resposta: """, """Alternativa errada! A correta é a número 5. Um clássico, o filme De Volta para o Futuro de 1985""")

# ============================================================================

        preto('===' * 40)

        azul('> QUESTÃO 6')
        pergunta(2, """

- Crescer pode ser uma jornada turbulenta, e com Riley não é diferente. Conforme ela e suas emoções, Alegria, 
Medo, Raiva, Nojinho e Tristeza se esforçam para adaptar-se à uma nova vida, uma enorme agitação toma conta 
do centro de controle em sua mente.

1) Soul
2) Divertida Mente
3) Sempre ao Seu Lado
4) Marley e Eu
5) Dançando no Escuro

> Resposta: """, """Alternativa errada! A correta é a número 2. Um filme com várias profundidades, Divertidamente
é um filme sobre as emoções humanas estreado em 2015.""")

# ============================================================================

        preto('===' * 40)

        azul('> QUESTÃO 7')
        pergunta(5, """

- Após Thanos eliminar metade das criaturas vivas, os Vingadores têm de lidar com a perda de amigos e 
entes queridos. Com Tony Stark vagando perdido no espaço sem água e comida, Steve Rogers e 
Natasha Romanov lideram a resistência contra o titã louco.

1) Vingadores: Guerra Infinita
2) Vingadores
3) Vingadores: Era de Ultron
4) Capitão América: Guerra Civil
5) Vingadores: Ultimato

> Resposta: """, """Alternativa errada! A correta é a número 5. O filme Vingadores: Ultimato de 2019 é o filme
mais recente do universo Vingadores.""")

# ============================================================================

        preto('===' * 40)

        azul('> QUESTÃO 8')
        pergunta(3, """

- Com a ajuda de Jim Gordon e Harvey Dent, Batman tem mantido a ordem na cidade de Gotham. Mas um jovem e 
anárquico criminoso conhecido como Coringa ganha força e decide instaurar um verdadeiro caos na cidade. 
O justiceiro será testado psicologicamente e fisicamente como nunca fora antes em um confronto bastante 
pessoal. Cabe a Batman encontrar uma maneira de deter o sádico vilão antes que mais vidas sejam perdidas.

1) The Batman
2) Batman: O Cavaleiro das Trevas Ressurge
3) Batman: O Cavaleiro das Trevas
4) Batman: Begins
5) Liga da Justiça de Zack Snyder

> Resposta: """, """Alternativa errada! A correta é a número 3. O filme mais famoso do universo DC, 
Batman: O Cavaleiro das Trevas de 2008.""")

# ============================================================================

        preto('===' * 40)

        azul('> QUESTÃO 9')
        pergunta(1, """

- O adolescente Daniel LaRusso se envolve com a ex-namorada do valentão da escola e começa a ser atormentado 
por sua gangue. Para sua sorte, ele conta com os ensinamentos do senhor Miyagi, um mestre de karatê que o 
prepara para autodefesa e também para um importante campeonato.

1) Karatê Kid: A Hora da Verdade
2) Cobra Kai
3) Karatê Kid II: A Hora da Verdade Continua
4) Karatê Kid III: O Desafio Final
5) Kung Fu Panda

> Resposta: """, """Alternativa errada! A correta é a número 3. O filme Karatê Kid: A Hora da Verdade de 1986 é
a sequência do famoso filme Karatê Kid.""")

# ============================================================================

        preto('===' * 40)

        azul('> QUESTÃO 10')
        pergunta(4, """

- Chris enfrenta sérios problemas financeiros e Linda, sua esposa, decide partir. Ele agora é pai solteiro e 
precisa cuidar de Christopher, seu filho de 5 anos. Chris tenta usar sua habilidade como vendedor para 
conseguir um emprego melhor, mas só consegue um estágio não remunerado. Seus problemas financeiros não 
podem esperar uma promoção e eles acabam despejados. Chris e Christopher passam a dormir em abrigos ou 
onde quer que consigam um refúgio, mantendo a esperança de que dias melhores virão.

1) Lobo de Wall Street
2) Os Mercenários
3) Fome de Poder
4) À Procura da Felicidade
5) Eu Sou a Lenda

> Resposta: """, """Alternativa errada! A correta é a número 4. O Filme dramático protagonizado por Will Smith,
fazendo o papel de um pai de família, À Procura da Felicidade de 2006.""")


# Interface -----------------------------------------------------------------------------
        print()

        titulo_2('RESULTADOS')

        if 0 <= cont_pontos <= 3:
            qtde_pontos_5(cont_pontos)
            mal_desempenho("""Poxa, você possui muito pouco conhecimento sobre filmes! Se entretenha mais com os clássicos ou
            revolucionários do cinema, faz muito bem!""")
            sleep(3)


        if 4 <= cont_pontos <= 6:

            if cont_pontos == 4 or cont_pontos == 5:
                qtde_pontos_5(cont_pontos)
            if cont_pontos == 6:
                qtde_pontos_10(cont_pontos)

            bom_desempenho("""Parabéns :) , você possui um nível moderado de conhecimento cinematográfico!""")
            sleep(3)


        if 7 <= cont_pontos <= 9:
            qtde_pontos_10(cont_pontos)
            bom_desempenho("""Muito bem! Você possui um ótimo conhecimento sobre cinema!""")
            sleep(3)


        if cont_pontos == 10:
            qtde_pontos_10(cont_pontos)
            bom_desempenho("PARABENS! Você possui um conhecimento incrível sobre cinema!")
            sleep(3)

        print('---' * 38)
        print(f'|{"PERGUNTA":^40}|{"RESPOSTA DO JOGADOR":^40}|{"SITUAÇÃO":^30}|')
        print('---' * 38)

        for indice, resposta in enumerate(lista_respostas):

            if resposta == lista_respostas_certas[indice]:
                lista_correto_errado.append('\033[0;32mAcertou\033[m')
            else:
                lista_correto_errado.append('\033[0;31mErrou\033[m')

            print(f'|{indice + 1:^40}|{resposta:^40}|{lista_correto_errado[cont_lista]:^40}|')
            cont_lista += 1


        print('---' * 38)


        preto('===' * 38)
        azul('> REGISTRO')
        username('Gostaria de registrar sua pontuação? [S/N]: ', 'Digite seu nome de usuário: ')
        preto('===' * 38)

        maior_para_menor = list(reversed(sorted(lista_pontuacao_jogadores)))

        del lista_correto_errado
        del lista_respostas
        del cont_pontos
        del cont_lista

        lista_correto_errado = []
        lista_respostas = []
        cont_pontos = 0
        cont_lista = 0

        titulo('MUITO OBRIGADO POR TER JOGADO NOSSO QUIZ!')

        retorno('-> Digite e confirme 0 para retornar ao menu principal: ')

# Ranking dos jogadores ------------------------------------------------------------------

    if opcao == 2:

        if len(lista_pontuacao_jogadores) == 0:
            errado('Ainda não há jogadores no ranking! Registre seu resultado para aparecer nele!')

        else:

            print()
            titulo('RANKING DOS JOGADORES')

            print('--' * 47)
            print(f'|{"POSIÇÃO":^30}|{"JOGADOR":^30}|{"PONTUAÇÃO":^30}|')
            print('--' * 47)

            for index, jogador in enumerate(maior_para_menor):

                print(f'|{index + 1:^30}|{jogador[1]:^30}|{jogador[0]:^30}|')

        retorno('-> Digite e confirme 0 para retornar ao menu principal: ')

# Créditos -------------------------------------------------------------------------------

    if opcao == 3:
        titulo_2('CRÉDITOS')

        azul('> CRÉDITOS')

        print()

        print('--' * 41)
        print(f'|{"Nome do Integrante":^40}|{"TIA":^40}|')
        print('--' * 41)
        print(f'|{"Vitor Sampaio Nascimento":^40}|{"32249497":^40}|')
        print(f'|{"Tales de Campos Hernandes":^40}|{"42202639":^40}|')
        print('--' * 41)

        print()

        print("""> O jogo \"Quiz dos Filmes\", criado pelos alunos Vitor Sampaio e Tales Hernandes da Universidade Presbiteriana Mackenzie, 
possui o intuito de avaliar o conhecimento cinematográfico do respectivo jogador através da contagem de pontos em função da
quantidade de acertos.""")

        print()
        print()

        preto('===' * 40)

        retorno('-> Digite e confirme 0 para retornar ao menu principal: ')

# Fechar o jogo --------------------------------------------------------------------------

    if opcao == 4:
        break

    continue

# Finalização ---------------------------------------------------------------------------


print()

titulo_2('MUITO OBRIGADO POR TER ACESSADO NOSSO QUIZ! :)')

sleep(1)

print('--' * 41)
print(f'|{"Nome do Integrante":^40}|{"TIA":^40}|')
print('--' * 41)
print(f'|{"Vitor Sampaio Nascimento":^40}|{"32249497":^40}|')
print(f'|{"Tales de Campos Hernandes":^40}|{"42202639":^40}|')
print('--' * 41)