import sys

def process_csv():

    linhas = sys.stdin.readlines()

    cabecalhos = linhas[0].strip().split(';')

    compositores = set()
    distribuicao_periodo = {}
    obras_periodo = {}

    linha_atual = ""
    for i in range(1, len(linhas)):
        linha = linhas[i].strip()

        if linha_atual and not isCompleteRecord(linha_atual, cabecalhos):
            linha_atual += " " + linha
        else:
            if linha_atual:
                obra = process_line(linha_atual, cabecalhos)

                compositores.add(obra['compositor'])

                periodo = obra['periodo']
                distribuicao_periodo[periodo] = distribuicao_periodo.get(periodo, 0) + 1

                if periodo not in obras_periodo:
                    obras_periodo[periodo] = []
                obras_periodo[periodo].append(obra['nome'])

            linha_atual = linha

    if linha_atual:
        obra = process_line(linha_atual, cabecalhos)
        compositores.add(obra['compositor'])
        periodo = obra['periodo']
        distribuicao_periodo[periodo] = distribuicao_periodo.get(periodo, 0) + 1
        if periodo not in obras_periodo:
            obras_periodo[periodo] = []
        obras_periodo[periodo].append(obra['nome'])

    compositores_ordenados = sorted(list(compositores))
    for periodo in obras_periodo:
        obras_periodo[periodo].sort()

    return compositores_ordenados, distribuicao_periodo, obras_periodo


def isCompleteRecord(linha, cabecalhos):
    "Verifica se todos os campos estão na mesma linha"
    dentro_aspas = False
    contador_campos = 1

    for char in linha:
        if char == '"':
            dentro_aspas = not dentro_aspas
        elif char == ';' and not dentro_aspas:
            contador_campos += 1

    return contador_campos == len(cabecalhos)


def process_line(linha, cabecalhos):
    valores = []
    valor_atual = ""
    dentro_aspas = False

    for char in linha:
        if char == '"':
            dentro_aspas = not dentro_aspas
            valor_atual += char
        elif char == ';' and not dentro_aspas:
            valores.append(valor_atual.strip())
            valor_atual = ""
        else:
            valor_atual += char

    valores.append(valor_atual.strip())

    if len(valores) != len(cabecalhos):
        raise ValueError(
            f"Erro no processamento da linha. Número de valores ({len(valores)}) não corresponde ao número de cabeçalhos ({len(cabecalhos)})")

    obra = dict(zip(cabecalhos, valores))
    return obra


def main():
    compositores, distribuicao, dicionario_periodos = process_csv()

    print("1. Lista ordenada alfabeticamente dos compositores musicais:")
    for compositor in compositores:
        print(f"   - {compositor}")

    print("\n2. Distribuição das obras por período:")
    for periodo, contagem in distribuicao.items():
        print(f"   {periodo}: {contagem} obra(s)")

    print("\n3. Dicionário de períodos e suas obras:")
    for periodo, titulos in dicionario_periodos.items():
        print(f"   {periodo}:")
        for titulo in titulos:
            print(f"     - {titulo}")


if __name__ == "__main__":
    main()

