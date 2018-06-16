n = float(input())

if 0 <= n <= 1000000.00:
    notas_cem = int(n // 100)
    n = n % 100

    notas_cinqueta = int(n // 50)
    n = n % 50

    notas_vinte = int(n // 20)
    n = n % 20

    notas_dez = int(n // 10)
    n = n % 10

    notas_cinco = int(n // 5)
    n = n % 5

    notas_dois = int(n // 2)
    n = n % 2




    print(notas_cem, notas_cinqueta, notas_vinte, notas_dez, notas_cinco, notas_dois)
