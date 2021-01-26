cpdef int fibonacci(int x):
    cdef int anterior = 0
    cdef int proximo = 0

    while (proximo < total):
        proximo = proximo + anterior
        anterior = proximo - anterior
        if (proximo == 0):
            proximo = proximo + 1