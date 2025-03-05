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



## **Implementação**
 
Programa: lexicalanly.py

Execução: `python3 lexicalanly.py < exemplo.txt`


