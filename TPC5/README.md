# **PL2025- TPC5**

## **Data:** 12/03/2025 

## **Autor:** Tomás Sousa Barbosa

## **Problema proposto**

### Construir um programa que simule uma máquina de vending. A máquina tem um stock de produtos: uma lista de triplos, nome do produto, quantidade e preço.

```
stock = [
{"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
...
]
```
### Interação com a máquina

```
maq: 2024-03-08, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
>> LISTAR
maq:
cod | nome | quantidade | preço
---------------------------------
A23 água 0.5L 8 0.7
...
>> MOEDA 1e, 20c, 5c, 5c .
maq: Saldo = 1e30c
>> SELECIONAR A23
maq: Pode retirar o produto dispensado "água 0.5L"
maq: Saldo = 60c
>> SELECIONAR A23
maq: Saldo insufuciente para satisfazer o seu pedido
maq: Saldo = 60c; Pedido = 70c
>> ...
...
maq: Saldo = 74c
>> SAIR
maq: Pode retirar o troco: 1x 50c, 1x 20c e 2x 2c.
maq: Até à próxima
```

## Metodologia

Para a resolução deste programa, decidi basear-me num analisador léxico com foi ensinado nas aulas.
Para isso foi necessário criar os tokens, as suas expressões regulares.
Para o stock ser atualizado corretamente com o inicio e encerramento de programa foram necessárias criar duas funções, uma para dar load do stock e outra para salvar o mesmo no fim do programa.
Foi feita uma função para processar o pedido dependendo do tipo de comandos : `LISTAR` , `MOEDA` , `SELECIONAR`, `SAIR`, onde chama a respetiva função específica para tratar do pedido.


## **Implementação**
 
Programa: [`vendingMachine.py`](https://github.com/a104532/PL2025-A104532/blob/main/TPC5/vendingMachine.py)

JSON : [`stock.json`](https://github.com/a104532/PL2025-A104532/blob/main/TPC5/stock.json)

Execução: `python3 vendingMachine.py` - necessário ter o ply instalado (pip install ply)



