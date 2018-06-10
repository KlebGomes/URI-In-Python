saque = int(input())
print(saque)
if 0 < saque < 1000000:
    nota_cem = saque // 100
    saque = saque % 100

    notas_cinquenta = saque // 50
    saque = saque % 50

    notas_vinte = saque // 20
    saque = saque % 20

    notas_dez = saque // 10
    saque = saque % 10

    notas_cinco = saque // 5
    saque = saque % 5

    notas_dois = saque // 2
    saque = saque % 2

    notas_um = saque // 1

    print('{} nota(s) de R$ 100,00'.format(nota_cem))
    print('{} nota(s) de R$ 50,00'.format(notas_cinquenta))
    print('{} nota(s) de R$ 20,00'.format(notas_vinte))
    print('{} nota(s) de R$ 10,00'.format(notas_dez))
    print('{} nota(s) de R$ 5,00'.format(notas_cinco))
    print('{} nota(s) de R$ 2,00'.format(notas_dois))
    print('{} nota(s) de R$ 1,00'.format(notas_um))