# Algoritmos Busca Binária

informacoes_entrada_elenco = input("Digite a lista de informações do elencos de jogadores (nome, número camisa, gols) separados por ponto e virgula (;): ")
informacao_alvo_busca = int(input("Informe o número da camisa do jogador que deseja buscar: "))

lista_jogadores = informacoes_entrada_elenco.split(';')

dicionario_elenco = []
for jogador in lista_jogadores:
    nome, numero_camisa, gols = jogador.strip().split(',')
    dicionario_elenco.append({
        'nome': nome,
        'numero_camisa': int(numero_camisa),
        'gols': int(gols)
    })

dicionario_elenco.sort(key=lambda x: x['numero_camisa'])

def busca_binaria_jogador(elenco, numero_camisa):
    esquerda, direita = 0, len(elenco) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        if elenco[meio]['numero_camisa'] == numero_camisa:
            return meio
        elif elenco[meio]['numero_camisa'] < numero_camisa:
            esquerda = meio + 1
        else:
            direita = meio -1
    
    return -1

indice = busca_binaria_jogador(dicionario_elenco, informacao_alvo_busca)


if indice != -1:
    jogador = dicionario_elenco[indice]
    print(f"Jogador encontrado: {jogador['nome']} - Camisa {jogador['numero_camisa']} - Gols: {jogador['gols']}")
else:
    print("Jogador não encontrado")
