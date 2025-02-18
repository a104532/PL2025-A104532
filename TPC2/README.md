# **PL2025- TPC2**

## **Data:** 15/02/2025 

## **Autor:** Tomás Sousa Barbosa

---
## **Problema proposto**

### Realização de um programa em Python onde :

Ler um dataset e processá-lo de modo a obter os seguintes resultados: 
- Lista ordenada alfabeticamente dos compositores musicais;
- Distribuição das obras por período: quantas obras catalogadas em cada período;
- Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período;

Sabendo que é proibido usar o módulo CSV do Python.

## Metodologia

O programa lê e processa um ficheiro CSV do sys.stdin, garantindo que os resultados são obtidos mesmo quando existem `/n` dentro de campos entre aspas.
Como os campos podem conter `;` e `/n` dentro de aspas, a função `isCompleteRecord()` verifica se uma linha está completa, caso não esteja, então a linha é concatenada à próxima antes de ser processada
A função `process_line()` divide corretamente os campos do CSV, garantindo que os delimitadores dentro das aspas sejam ignorados.
Os dados são armazenados num dicionário (obra), onde vão estar os resultados pretendidos.
Construção dos resultados: 
- Os compositores são guardados num set, evitando duplicações, e depois ordenados.
- A distribuição das obras por período é armazenada num dicionário, contando quantas obras pertencem a cada período.
- As obras por período são agrupadas, garantindo que os títulos fiquem organizados alfabeticamente.
Por fim os resultados são apresentados através de um print.
---
## **Implementação**

Ficheiro csv: [obras.csv]()

Programa: [parser.py]()

Execução: `python3 parser.py < obras.csv`


