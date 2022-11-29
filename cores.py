# Funções das Cores ------------------------------------------------------------------------

def titulo(msg):
    print('\033[1;30m===\033[m' * 31)
    print(f'\033[1;33;40m{msg:^93}\033[m')
    print('\033[1;30m===\033[m' * 31)


def titulo_2(msg):
    print('\033[1;30m===\033[m' * 40)
    print(f'\033[1;33;40m{msg:^120}\033[m')
    print('\033[1;30m===\033[m' * 40)


def vermelho(msg):
    print(f'\033[1;31m{msg}\033[m')


def azul(msg):
    print(f'\033[1;34m{msg}\033[m')


def preto(msg):
    print(f'\033[1;30m{msg}\033[m')


def errado(msg):
    print('\033[1;31m---\033[m' * 30)
    print(f'\033[1;31m{msg:^90}\033[m')
    print('\033[1;31m---\033[m' * 30)


def correto(msg):
    print('\033[1;32m---\033[m' * 30)
    print(f'\033[1;32m{msg:^90}\033[m')
    print('\033[1;32m---\033[m' * 30)


def qtde_pontos_5(pontos):
    print(f'\033[1;97m{"Quantidade total de pontos: ":^121}\033[m')
    print(f'\033[1;31m{pontos:^121}\033[m')
    print('\033[1;30m===\033[m' * 40)


def qtde_pontos_10(pontos):
    print(f'\033[1;97m{"Quantidade total de pontos: ":^121}\033[m')
    print(f'\033[1;32m{pontos:^121}\033[m')
    print('\033[1;30m===\033[m' * 40)


def mal_desempenho(msg):
    print()
    print('\033[1;30m===\033[m' * 40)
    print(f'\033[1;31;40m{msg:^120}\033[m')
    print('\033[1;30m===\033[m' * 40)
    print()


def bom_desempenho(msg):
    print()
    print('\033[1;30m===\033[m' * 40)
    print(f'\033[1;32;40m{msg:^120}\033[m')
    print('\033[1;30m===\033[m' * 40)
    print()