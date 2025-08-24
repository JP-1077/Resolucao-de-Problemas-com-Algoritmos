# Algoritmos Ordenação

informacoes_entrada_elenco = input("Digite a lista de informações do elencos de jogadores (nome, número camisa, gols) separados por ponto e virgula (;): ")
lista_jogadores = informacoes_entrada_elenco.split(';')

dicionario_elenco = []
for jogador in lista_jogadores:
    nome, numero_camisa, gols = jogador.strip().split(',')
    dicionario_elenco.append({
        'nome': nome,
        'numero_camisa': int(numero_camisa),
        'gols': int(gols)
    })

def ordernar_elenco_por_gols(elenco):
    n = len(elenco)

    for i in range(n):
        min_index = i

        for j in range( i + 1, n):
            if elenco[j] ['gols'] < elenco[min_index]['gols']:
                min_index = j   
        
        elenco[i], elenco[min_index] = elenco[min_index], elenco[i]

    return elenco

elenco_ordenado = ordernar_elenco_por_gols(dicionario_elenco)
print("Elenco ordernado por gols (menor para maior):")
for jogador in elenco_ordenado:
    print(f"{jogador['nome']} - Camisa {jogador['numero_camisa']} - Gols: {jogador['gols']}")



