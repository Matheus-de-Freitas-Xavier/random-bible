# Função para criar o arquivo
def biblia_inicio(livro, capitulo):
    conteudo = []
    for c in range(1, capitulo + 1):
        conteudo.append(f'{livro} {c}\n')
    with open('Biblia.txt', 'w') as arq:
        for item in conteudo:
            arq.writelines(item)
    
# Função para adicionar ao arquivo existente
def biblia(livro, capitulo):
    conteudo = []
    for c in range(1, capitulo +1):
        conteudo.append(f'{livro} {c}\n')
    with open('Biblia.txt', 'a') as arq:
        for item in conteudo:
            arq.writelines(item)
        
# genesis = [50]
biblia_inicio('Genêsis', 50)

# exodo = [40]
biblia('Êxodo', 40)

# levitico = [27]
biblia('Levítico', 27)

# numeros = [36]
biblia('Números', 36)

# deut = [34]
biblia('Deuteronômio', 34)

# josué = [24]
biblia('Josué', 24)

# juízes = [21]
biblia('Juízes', 21)

# rute = [4]
biblia('Rute', 4)

# samuel1 = [31]
biblia('1 Samuel', 31)

# samuel2 = [24]
biblia('2 Samuel', 24)

# ##reis1 = [22]
biblia('1 Reis', 22)

# ##reis2 = [25]
biblia('2 Reis', 25)

# ##cronicas1 = [29]
biblia('1 Crônicas', 29)

# ##cronicas2 = [36]
biblia('2 Crônicas', 36)

# ##esdras = [10]
biblia('Esdras', 10)

# ##neemias = [13]
biblia('Neemias', 13)

# ##ester = [10]
biblia('Ester', 10)

# ##jó = [42]
biblia('Jó', 42)

# ##salmos = [150]
biblia('Salmos', 150)

# ##provérbios = [31]
biblia('Provérbios', 31)

# ##eclesiastes = [12]
biblia('Eclesiastes', 12)

# ##cantares = [8]
biblia('Cantares', 8)

# ##isaias = [66]
biblia('Isaías', 66)

# ##jeremias = [52]
biblia('Jeremias', 52)

# ##lamentação = [5]
biblia('Lamentações', 5)

# ##ezequiel = [48]
biblia('Ezequiel', 48)

# ##daniel = [12]
biblia('Daniel', 12)

# ##oseias = [14]
biblia('Oseias', 14)

# ##joel = [3]
biblia('Joel', 3)

# ##amós = [9]
biblia('Amós', 9)

# ##obadias = [1]
biblia('Obadias', 1)

# ##jonas = [4]
biblia('Jonas', 4)

# ##miqueias = [7]
biblia('Miqueias', 7)

# ##naum = [3]
biblia('Naum', 3)

# ##habacuque = [3]
biblia('Habacuque', 3)

# ##sofonias = [3]
biblia('Sofonias', 3)

# ##ageu = [2]
biblia('Ageu', 2)

# ##zacarias = [14]
biblia('Zacarias', 14)

# ##malaquias = [4]
biblia('Malaquias', 4)

# ##mateus = [28]
biblia('Mateus', 28)

# ##marcos = [16]
biblia('Marcos', 16)
    
# ##lucas = [24]
biblia('Lucas', 24)

# ##joão = [21]
biblia('João', 21)

# ##atos = [28]
biblia('Atos', 28)

# ##romanos = [16]
biblia('Romanos', 16)

# ##corintios1 = [16]
biblia('1 Coríntios', 16)

# ##corintios2 = [13]
biblia('2 Coríntios', 13)

# ##galatas = [6]
biblia('Gálatas', 6)

# ##efésios = [6]
biblia('Efésios', 6)

# ##filipenses = [4]
biblia('Filipenses', 4)

# ##colossenses = [4]
biblia('Colossenses', 4)

# ##tessa1 = [5]
biblia('1 Tessalonicenses', 5)

# ##tessa2 = [3]
biblia('2 Tessalonicenses', 3)

# ##timoteo1 = [6]
biblia('1 Timóteo', 6)

# ##timoteo2 = [4]
biblia('2 Timóteo', 4)

# ##tito = [3]
biblia('Tito', 3)

# ##filemon = [1]
biblia('Filemon', 1)

# ##hebreus = [13]
biblia('Hebreus', 13)

# ##tiago = [5]
biblia('Tiago', 5)

# ##pedro1 = [5]
biblia('1 Pedro', 5)

# ##pedro2 = [3]
biblia('2 Pedro', 3)

# ##joão1 = [5]
biblia('1 João', 5)

# ##joão2 = [1]
biblia('2 João', 1)

# ##joão3 = [1]
biblia('3 João', 1)

# ##judas = [1]
biblia('Judas', 1)

# ##apocalipse = [22]
biblia('Apocalipse', 22)
