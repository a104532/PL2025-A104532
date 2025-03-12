# **PL2025- TPC3**

## **Data:** 24/02/2025 

## **Autor:** Tomás Sousa Barbosa

## **Problema proposto**

### Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet

## Metodologia

O código recebe um texto em Markdown e substitui os seus elementos por HTML usando expressões regulares.
Para os cabeçalhos, ele usa `^# (.+)$`, onde `^` indica início da linha, `#` identifica um cabeçalho de nível 1 e `(.+)$` captura o restante do texto, substituindo por `<h1>\1</h1>`. 
O mesmo padrão é aplicado para `##` e `###`. 
Para o negrito, a regex `\*\*(.+?)\*\*` busca texto entre `**`, garantindo que seja capturado de forma não gananciosa `(.+?)`. 
Para o itálico, a regex `(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)` evita capturar `**` dentro do padrão. 
Os links `[texto](url)` são transformados com `\[(.*?)\]\((.*?)\)`, onde `.*?` captura texto e URL separadamente. 
Imagens `![alt](url)` seguem um padrão semelhante, `!\[(.*?)\]\((.*?)\)`, mas gera uma tag `<img>`. 
As listas numeradas são mais complexas, pois precisam de múltiplas linhas; primeiro, `(?:^\d+\. .+$\n?)+` encontra blocos de itens começando com um número e um ponto. 
Depois, `^\d+\. (.+)$` extrai os textos individuais dos itens. Um novo bloco `<ol>` é montado iterando pelos itens e substituindo a versão Markdown pela estrutura HTML correspondente.

## **Implementação**
 
Programa: [conversor.py](https://github.com/a104532/PL2025-A104532/blob/main/TPC3/conversor.py)

Ficheiro de teste: [teste.py](https://github.com/a104532/PL2025-A104532/blob/main/TPC3/teste.py)

Execução de programa teste : `python3 teste.py`


