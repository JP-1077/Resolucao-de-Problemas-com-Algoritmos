# Algoritmos Recursivo

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

def soma_gols_recursiva(elenco, indice=0):
    if indice == len(elenco):
        return 0
    else:
        return elenco[indice]['gols'] + soma_gols_recursiva(elenco, indice + 1)
    
print(f"Total de gols marcados pelo elenco: {soma_gols_recursiva(dicionario_elenco)}")


