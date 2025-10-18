from collections import deque
import pandas as pd

def fifo(paginas, numero_quadros, pagina_consultada):
    # Verifica se o número de quadros é maior que o número de páginas
    if numero_quadros > len(paginas):
        print("Número de quadros maior que o número de páginas. Ajustando para o número de páginas.")
        numero_quadros = len(paginas)

    memoria = deque(maxlen=numero_quadros)
    historico = []
    contagem_falhas = 0

    print(f"Simulação FIFO - {numero_quadros} quadros")
    print(f"Sequência de páginas: {paginas}")
    print(f"Página consultada: {pagina_consultada}")
   
    for i, pagina in enumerate(paginas): # Inicia um loop para percorrer todas as páginas na sequência fornecida
        falha = False
        if pagina not in memoria:  # Verifica se a página não está na memória (não foi carregada nos quadros)
            falha = True
            contagem_falhas += 1
            if len(memoria) < numero_quadros: # Verifica se ainda há espaço na memória
                memoria.append(pagina)
            else:
                memoria.popleft() # Remove a página mais antiga da memória
                memoria.append(pagina) # Adiciona a nova página na memória 

        # Preenche quadros vazios com espaços vazios
        estado = list(memoria) + [""] * (numero_quadros - len(memoria))
        historico.append(estado + ["FALHA" if falha else "OK"])

    # Criação do DataFrame
    colunas = [f"Q{i+1}" for i in range(numero_quadros)] + ["Status"]
    tabela = pd.DataFrame(historico, columns=colunas)
    tabela.index = [f"{i+1:02d} - P{p}" for i, p in enumerate(paginas)]

    print(tabela.head(10))  # Exibe as 10 primeiras linhas do DataFrame
    print("\n----------------------------------")
    print(f"Total de faltas de página: {contagem_falhas}")

    # Verifica a posição da página consultada
    if pagina_consultada in memoria:
        quadro = list(memoria).index(pagina_consultada) + 1
        print(f"A página {pagina_consultada} está no quadro {quadro}.")
    else:
        print(f"A página {pagina_consultada} não está na memória ao final da execução.")

    return tabela


sequencia_a = [4,3,25,8,19,6,25,8,16,2,45,22,8,3,16,25,7]
fifo(sequencia_a, numero_quadros=8, pagina_consultada=7)


sequencia_b = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
fifo(sequencia_b, numero_quadros=8, pagina_consultada=11)


sequencia_c = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]
fifo(sequencia_c, numero_quadros=8, pagina_consultada=11)

