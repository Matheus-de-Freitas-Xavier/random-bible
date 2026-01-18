# Função para criar o arquivo
def biblia_inicio(livro, qntd_capitulo):
    conteudo = []
    for c in range(1, qntd_capitulo + 1):
        conteudo.append(f'{livro} {c}\n')
    with open('Biblia.txt', 'w') as arq:
        for item in conteudo:
            arq.writelines(item)

# Função para adicionar ao arquivo existente
def biblia(livro, qntd_capitulo):
    conteudo = []
    for c in range(1, qntd_capitulo +1):
        conteudo.append(f'{livro} {c}\n')
    with open('Biblia.txt', 'a') as arq:
        for item in conteudo:
            arq.writelines(item)

biblia_inicio('Gênesis', 50)

biblia('Êxodo', 40)

biblia('Levítico', 27)

biblia('Números', 36)

biblia('Deuteronômio', 34)

biblia('Josué', 24)

biblia('Juízes', 21)

biblia('Rute', 4)

biblia('1 Samuel', 31)

biblia('2 Samuel', 24)

biblia('1 Reis', 22)

biblia('2 Reis', 25)

biblia('1 Crônicas', 29)

biblia('2 Crônicas', 36)

biblia('Esdras', 10)

biblia('Neemias', 13)

biblia('Ester', 10)

biblia('Jó', 42)

biblia('Salmos', 150)

biblia('Provérbios', 31)

biblia('Eclesiastes', 12)

biblia('Cantares', 8)

biblia('Isaías', 66)

biblia('Jeremias', 52)

biblia('Lamentações', 5)

biblia('Ezequiel', 48)

biblia('Daniel', 12)

biblia('Oseias', 14)

biblia('Joel', 3)

biblia('Amós', 9)

biblia('Obadias', 1)

biblia('Jonas', 4)

biblia('Miqueias', 7)

biblia('Naum', 3)

biblia('Habacuque', 3)

biblia('Sofonias', 3)

biblia('Ageu', 2)

biblia('Zacarias', 14)

biblia('Malaquias', 4)

biblia('Mateus', 28)

biblia('Marcos', 16)

biblia('Lucas', 24)

biblia('João', 21)

biblia('Atos', 28)

biblia('Romanos', 16)

biblia('1 Coríntios', 16)

biblia('2 Coríntios', 13)

biblia('Gálatas', 6)

biblia('Efésios', 6)

biblia('Filipenses', 4)

biblia('Colossenses', 4)

biblia('1 Tessalonicenses', 5)

biblia('2 Tessalonicenses', 3)

biblia('1 Timóteo', 6)

biblia('2 Timóteo', 4)

biblia('Tito', 3)

biblia('Filemon', 1)

biblia('Hebreus', 13)

biblia('Tiago', 5)

biblia('1 Pedro', 5)

biblia('2 Pedro', 3)

biblia('1 João', 5)

biblia('2 João', 1)

biblia('3 João', 1)

biblia('Judas', 1)

biblia('Apocalipse', 22)
