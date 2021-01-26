def fibonacci(total):
    anterior = 0
    proximo = 0

    while (proximo < total):
        proximo = proximo + anterior
        anterior = proximo - anterior
        if (proximo == 0):
            proximo = proximo + 1