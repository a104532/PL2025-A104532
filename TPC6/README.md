# **PL2025- TPC6**

## **Data:** 21/03/2025 

## **Autor:** Tomás Sousa Barbosa

## **Problema proposto**

### Baseado nos materiais fornecidos na aula, cria um parser LL(1) recursivo descendente que reconheça expressões aritméticas e calcule o respetivo valor.

Exemplos de algumas frases:

```
2+3
67-(2+3*4)
(9-2)*(13-4)

``` 

## Metodologia

Para a implementação deste programa reaproveitei o analisador léxico feito durante as aulas práticas `calc_lex.py`
Para criar um parser LL(1) recursivo descendente foi feito o analisador léxico para definir os tokens e as regras para os reconhecer. Foi feita a função `get_tokens()` para converter a string na lista de tokens para serem usados no analisador sintático.
No analisador sintático contém a classe Parser que implementa as regras gramaticais.
Esta separação apenas foi feita porque foi mostrada assim durante as aulas práticas, de modo a facilitar a compreensão.

## **Implementação**
 
Analisador Léxico: [`calc_lex.py`](https://github.com/a104532/PL2025-A104532/blob/main/TPC6/calc_lex.py)

Analisador Sintático [`anasin.py`](https://github.com/a104532/PL2025-A104532/blob/main/TPC6/anasin.py)

