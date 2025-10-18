def lru(lista,totalQuadros):
    memoria = []
    faltaPagina = 0

    for pagina in lista:
        if pagina in memoria:
            memoria.remove(pagina)
            memoria.append(pagina)
        else:
            faltaPagina += 1
            quadro = len(memoria)
            if quadro < totalQuadros:
                memoria.append(pagina)
            else:
                memoria.pop(0) 
                memoria.append(pagina)

    print(f"Resultado Final: {memoria}")
    print(f"Faltas de Página: {faltaPagina}")
    
lista = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
totalQuadros = 8
lru(lista,totalQuadros)
lista = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
lru(lista,totalQuadros)
lista = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11 ]
lru(lista,totalQuadros)