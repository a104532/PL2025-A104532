import re


def conversor(markdown_text):
    html_text = markdown_text

    # Converter cabeçalhos
    # Procura por linhas que começam com # seguido de espaço e texto
    html_text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html_text)
    html_text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html_text)
    html_text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html_text)

    # Converter texto em negrito
    # Procura por texto entre **
    html_text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', html_text)

    # Converter texto em itálico
    # Procura por texto entre * (mas não entre **)
    html_text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', html_text)

    # Converter links
    # Procura por [texto](url)
    html_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html_text)

    # Converter imagens
    # Procura por ![texto alternativo](url)
    html_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', html_text)

    # Converter listas numeradas
    # Esta é mais complexa, pois envolve múltiplas linhas
    lista_numerada = re.findall(r'(?:^\d+\. .+$\n?)+', html_text)

    for lista in lista_numerada:
        # Obtém cada item da lista
        itens = re.findall(r'^\d+\. (.+)$', lista)

        # Cria a nova lista em HTML
        nova_lista = "<ol>\n"
        for item in itens:
            nova_lista += f"<li>{item}</li>\n"
        nova_lista += "</ol>"

        # Substitui a lista original pela nova lista em HTML
        html_text = html_text.replace(lista, nova_lista)

    return html_text
