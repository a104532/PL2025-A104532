import sys

def somador_on_off(texto):
    ligado = True
    soma = 0
    i = 0

    while i < len(texto):
        if texto[i] in "0123456789":
            valor = 0
            while i < len(texto) and texto[i] in "0123456789":
                valor = valor * 10 + int(texto[i])
                i += 1
            if ligado:
                soma += valor
        elif texto[i].lower() == 'o':
            if i + 1 < len(texto) and texto[i + 1].lower() == 'n':
                ligado = True
                i += 1
            elif i + 2 < len(texto) and texto[i + 1].lower() == 'f' and texto[i + 2].lower() == 'f':
                ligado = False
                i += 2
        elif texto[i] == '=':
            print(soma)
        i += 1  


for linha in sys.stdin:
    somador_on_off(linha)
