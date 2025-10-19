def mru(lista, totalQuadros):
    memoria = []
    faltaPagina = 0

    for pagina in lista:
        if pagina in memoria:
            # se a pagina ja esta na memoria, tiramos e colocamos novamente para a pag ir para o final da lista
            memoria.remove(pagina)
            memoria.append(pagina)
        else:
            # se a pagina nao esta na memoria, entao adicionamos ela
            faltaPagina += 1
            quadro = len(memoria)
            # verificando se tem quadro disponivel: 
            if quadro < totalQuadros:
                # se tiver apenas aloca
                memoria.append(pagina)
            else:
                # senao tira a pag mais recente da memoria e depois aloca
                memoria.pop()  
                memoria.append(pagina)

    print(f"Resultado Final (MRU): {memoria}")
    print(f"Faltas de Página: {faltaPagina}")

lista = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
totalQuadros = 8
mru(lista, totalQuadros)
lista = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
mru(lista, totalQuadros)
lista = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]
mru(lista, totalQuadros)