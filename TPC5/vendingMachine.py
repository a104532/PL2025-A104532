import json
import re
import datetime
import ply.lex as lex

stock = []
saldo = 0

tokens= [
    "LISTAR",
    "ADDMOEDA",
    "MOEDA",
    "SELECIONAR",
    "PRODUTO",
    "PONTO",
    "VIRGULA",
    "SAIR"
]

moedas= {
    "2e" : 2.00,
    "1e" : 1.00,
    "50c" : 0.50,
    "20c" : 0.20,
    "10c" : 0.10,
    "5c" : 0.05,
    "2c" : 0.02,
    "1c" : 0.01
}

def t_LISTAR(t):
    r'LISTAR'
    return t

def t_ADDMOEDA(t):
    r'MOEDA'
    return t

def t_MOEDA(t):
    r'\d+[ecEC]'
    return t

def t_SELECIONAR(t):
    r'SELECIONAR'
    return t

def t_PRODUTO(t):
    r'[A-Z]\d+'
    return t

def t_PONTO(t):
    r'\.'
    return t

def t_VIRGULA(t):
    r','
    return t

def t_SAIR(t):
    r'SAIR'
    return t

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def loadStock(file):
    global stock
    try:
        with open('stock.json', 'r') as json_file:
            stock = json.load(json_file)
            return True
    except Exception as e:
        print(f"maq: Erro ao carregar stock: {e}")
        return False

def saveStock(file):
    global stock
    try:
        with open(file, 'w', encoding='utf-8') as json_file:
            json.dump(stock, json_file, indent=2, ensure_ascii=False)
            return True
    except:
        return False

def formatarSaldo():
    global saldo
    euros = int(saldo)
    centimos = int(round((saldo - euros) * 100))

    if euros > 0 and centimos > 0:
        return f"{euros}e{centimos}c"
    elif euros > 0:
        return f"{euros}e"
    else:
        return f"{centimos}c"


def calcularTroco():
    global saldo
    if saldo == 0:
        return []

    troco = []
    valor_centimos = int(round(saldo * 100))

    for moeda, valor in moedas.items():
        valor_centimos_moeda = int(round(valor * 100))
        quantidade = valor_centimos // valor_centimos_moeda

        if quantidade > 0:
            troco.append((moeda, quantidade))
            valor_centimos -= quantidade * valor_centimos_moeda

    return troco

def listarProdutos():
    print("maq:")
    print("cod | nome | quantidade | preço")
    print("-" * 33)
    for produto in stock:
        print(f"{produto['cod']} {produto['nome']} {produto['quant']} {produto['preco']}")


def processarComandoMoeda(entrada):
    global saldo

    # Extrai as moedas para calcular o saldo
    moedas_encontradas = re.findall(r'(\d*[ec])', entrada)
    moedas_encontradas = [m for m in moedas_encontradas if m]

    for moeda in moedas_encontradas:
        if 'e' in moeda:
            valor = moeda.replace('e', '')
            valor = 1 if valor == '' else int(valor)
            saldo += valor
        else:
            valor = int(moeda.replace('c', ''))
            saldo += valor / 100

    print(f"maq: Saldo = {formatarSaldo()}")


def processarComandoSelecionar(codigo):
    global saldo, stock

    # Procura o produto no stock
    produto = next((p for p in stock if p["cod"] == codigo), None)

    if not produto:
        print(f"maq: Produto com código '{codigo}' não existe.")
        print(f"maq: Saldo = {formatarSaldo()}")
        return

    if produto["quant"] <= 0:
        print(f"maq: Produto '{produto['nome']}' esgotado.")
        print(f"maq: Saldo = {formatarSaldo()}")
        return

    preco = produto["preco"]

    if saldo < preco:
        print("maq: Saldo insufuciente para satisfazer o seu pedido")
        print(f"maq: Saldo = {formatarSaldo()}; Pedido = {preco}e")
        return

    #Faz a entrega do produto e retira o dinheiro do saldo
    saldo -= preco
    produto["quant"] -= 1
    print(f"maq: Pode retirar o produto dispensado \"{produto['nome']}\"")
    print(f"maq: Saldo = {formatarSaldo()}")


def processarComandoSair():
    global saldo

    troco = calcularTroco()

    if troco:
        texto_troco = []
        for moeda, quant in troco:
            texto_troco.append(f"{quant}x {moeda}")

        troco_formatado = ", ".join(texto_troco[:-1])
        if troco_formatado:
            troco_formatado += " e " + texto_troco[-1]
        else:
            troco_formatado = texto_troco[-1]

        print(f"maq: Pode retirar o troco: {troco_formatado}.")

    saldo = 0
    print("maq: Até à próxima")
    return True


def processarComando(comando):
    lexer = lex.lex()
    lexer.input(comando)

    token = lexer.token()

    if not token:
        print("maq: Comando não reconhecido.")
        return False

    if token.type == "LISTAR":
        listarProdutos()
    elif token.type == "ADDMOEDA":
        processarComandoMoeda(comando[5:])
    elif token.type == "SELECIONAR":
        token = lexer.token()
        if token and token.type == "PRODUTO":
            processarComandoSelecionar(token.value)
        else:
            print("maq: Código de produto não especificado ou inválido.")
    elif token.type == "SAIR":
        return processarComandoSair()
    else:
        print("maq: Comando não reconhecido.")

    return False


def main():
    # Carrega o stock
    if loadStock("stock.json"):
        print(f"maq: {datetime.datetime.now().strftime('%Y-%m-%d')}, Stock carregado, Estado atualizado.")
    else:
        print("maq: Erro ao carregar o stock.")
        return

    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    sair = False
    while not sair:
        try:
            comando = input(">> ")
            sair = processarComando(comando)
        except KeyboardInterrupt:
            print("\nmaq: Operação interrompida.")
            processarComandoSair()
            break
        except Exception as e:
            print(f"maq: Erro: {e}")

    # Salvar o stock atualizado
    saveStock("stock.json")


if __name__ == "__main__":
    main()