from collections import deque
import pandas as pd

def fifo(paginas, num_quadros, pagina_consulta):
    # Verifica se o número de quadros é maior que o número de páginas
    if num_quadros > len(paginas):
        print("Número de quadros maior que o número de páginas. Ajustando para o número de páginas.")
        num_quadros = len(paginas)

    memoria = deque(maxlen=num_quadros)
    historico = []
    page_faults = 0

    print(f"Simulação FIFO - {num_quadros} quadros")
    print(f"Sequência de páginas: {paginas}")
    print(f"Página consultada: {pagina_consulta}")
   
    for i, pagina in enumerate(paginas): # Inicia um loop para percorrer todas as páginas na sequência fornecida
        falha = False
        if pagina not in memoria:  # Verifica se a página não está na memória (não foi carregada nos quadros)
            falha = True
            page_faults += 1
            if len(memoria) < num_quadros: # Verifica se ainda há espaço na memória (se o número de quadros é menor que o total de páginas na memória)
                memoria.append(pagina)
            else:
                memoria.popleft() # Remove a página que foi carregada primeiro (a mais antiga) da memória
                memoria.append(pagina) # Adiciona a nova página na memória 

        # Preenche quadros vazios com espaços vazios
        estado = list(memoria) + [""] * (num_quadros - len(memoria))
        historico.append(estado + ["FALTA DE PAGINA" if falha else "OK"])

    # Criação do DataFrame
    colunas = [f"Q{i+1}" for i in range(num_quadros)] + ["Status"]
    df = pd.DataFrame(historico, columns=colunas)
    df.index = [f"{i+1:02d} - P{p}" for i, p in enumerate(paginas)]

    print(df.head(10))  # Exibe as 10 primeiras linhas do DataFrame
    print("\n----------------------------------")
    print(f"Total de falhas de página: {page_faults}")

    # Verifica a posição da página consultada
    if pagina_consulta in memoria:
        quadro = list(memoria).index(pagina_consulta) + 1
        print(f" A página {pagina_consulta} está no quadro {quadro}.")
    else:
        print(f" A página {pagina_consulta} não está na memória ao final da execução.")

    return df


seq_a = [4,3,25,8,19,6,25,8,16,2,45,22,8,3,16,25,7]
fifo(seq_a, num_quadros=8, pagina_consulta=7)

# b) Sequência (8 quadros)
seq_b = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
fifo(seq_b, num_quadros=8, pagina_consulta=11)

# c) Sequência (8 quadros)
seq_c = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]
fifo(seq_c, num_quadros=8, pagina_consulta=11)

