import conversor
exemplos = [
    "# Exemplo",
    "Este é um **exemplo** ...",
    "Este é um *exemplo* ...",
    "1. Primeiro item\n2. Segundo item\n3. Terceiro item",
    "Como pode ser consultado em [página da UC](http://www.uc.pt)",
    "Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ..."
]

for exemplo in exemplos:
    print("Markdown:")
    print(exemplo)
    print("\nHTML:")
    print(conversor.conversor(exemplo))
    print("-" * 50)