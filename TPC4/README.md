# **PL2025- TPC2**

## **Data:** 24/02/2025 

## **Autor:** Tomás Sousa Barbosa

## **Problema proposto**

### Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:

```
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
	?s a dbo:MusicalArtist.
	?s foaf:name "Chuck Berry"@en .
	?w dbo:artist ?s.
	?w foaf:name ?nome.
	?w dbo:abstract ?desc
} LIMIT 1000
```


## Metodologia

A implementação utiliza a biblioteca `ply`, que segue o modelo do popular gerador de analisadores léxicos LEX. O processo envolve:
1. Definir uma lista dos nomes dos tokens
2. Criar funções com o padrão `t_TOKENNAME` para cada token
3. Configurar o analisador léxico com `lexer = lex.lex()`
4. Processar o texto de entrada e extrair os tokens

## **Implementação**
 
Programa: [`lexicalanly.py`](https://github.com/a104532/PL2025-A104532/blob/main/TPC4/lexicalanly.py)

Execução: `python3 lexicalanly.py < exemplo.txt`


