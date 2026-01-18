# Função para criar o arquivo
def bible_start(book, chapter):
    content = []
    for c in range(1, chapter + 1):
        content.append(f'{book} {c}\n')
    with open('Bible.txt', 'w') as arq:
        for item in content:
            arq.writelines(item)
    
# Função para adicionar ao arquivo existente
def bible(book, chapter):
    content = []
    for c in range(1, chapter +1):
        content.append(f'{book} {c}\n')
    with open('Bible.txt', 'a') as arq:
        for item in content:
            arq.writelines(item)
        
# genesis = [50]
bible_start('Genesis', 50)

# exodo = [40]
bible('Exodus', 40)

# levitico = [27]
bible('Leviticus', 27)

# numeros = [36]
bible('Numbers', 36)

# deut = [34]
bible('Deuteronomy', 34)

# josué = [24]
bible('Joshua', 24)

# juízes = [21]
bible('Judges', 21)

# rute = [4]
bible('Ruth', 4)

# samuel1 = [31]
bible('1 Samuel', 31)

# samuel2 = [24]
bible('2 Samuel', 24)

# ##reis1 = [22]
bible('1 Kings', 22)

# ##reis2 = [25]
bible('2 Kings', 25)

# ##cronicas1 = [29]
bible('1 Chronicles', 29)

# ##cronicas2 = [36]
bible('2 Chronicles', 36)

# ##esdras = [10]
bible('Ezra', 10)

# ##neemias = [13]
bible('Nehemiah', 13)

# ##ester = [10]
bible('Esther', 10)

# ##jó = [42]
bible('Job', 42)

# ##salmos = [150]
bible('Psalms', 150)

# ##provérbios = [31]
bible('Proverbs', 31)

# ##eclesiastes = [12]
bible('Ecclesiastes', 12)

# ##cantares = [8]
bible('Song of Solomon', 8)

# ##isaias = [66]
bible('Isaiah', 66)

# ##jeremias = [52]
bible('Jeremiah', 52)

# ##lamentação = [5]
bible('Lamentations', 5)

# ##ezequiel = [48]
bible('Ezekiel', 48)

# ##daniel = [12]
bible('Daniel', 12)

# ##oseias = [14]
bible('Hosea', 14)

# ##joel = [3]
bible('Joel', 3)

# ##amós = [9]
bible('Amos', 9)

# ##obadias = [1]
bible('Obadiah', 1)

# ##jonas = [4]
bible('Jonah', 4)

# ##miqueias = [7]
bible('Micah', 7)

# ##naum = [3]
bible('Nahum', 3)

# ##habacuque = [3]
bible('Habakkuk', 3)

# ##sofonias = [3]
bible('Zephaniah', 3)

# ##ageu = [2]
bible('Haggai', 2)

# ##zacarias = [14]
bible('Zechariah', 14)

# ##malaquias = [4]
bible('Malachi', 4)

# ##mateus = [28]
bible('Matthew', 28)

# ##marcos = [16]
bible('Mark', 16)
    
# ##lucas = [24]
bible('Luke', 24)

# ##joão = [21]
bible('John', 21)

# ##atos = [28]
bible('Acts', 28)

# ##romanos = [16]
bible('Romans', 16)

# ##corintios1 = [16]
bible('1 Corinthians', 16)

# ##corintios2 = [13]
bible('2 Corinthians', 13)

# ##galatas = [6]
bible('Galatians', 6)

# ##efésios = [6]
bible('Ephesians', 6)

# ##filipenses = [4]
bible('Philippians', 4)

# ##colossenses = [4]
bible('Colossians', 4)

# ##tessa1 = [5]
bible('1 Thessalonians', 5)

# ##tessa2 = [3]
bible('2 Thessalonians', 3)

# ##timoteo1 = [6]
bible('1 Timothy', 6)

# ##timoteo2 = [4]
bible('2 Timothy', 4)

# ##tito = [3]
bible('Titus', 3)

# ##filemon = [1]
bible('Philemon', 1)

# ##hebreus = [13]
bible('Hebrews', 13)

# ##tiago = [5]
bible('James', 5)

# ##pedro1 = [5]
bible('1 Peter', 5)

# ##pedro2 = [3]
bible('2 Peter', 3)

# ##joão1 = [5]
bible('1 John', 5)

# ##joão2 = [1]
bible('2 John', 1)

# ##joão3 = [1]
bible('3 John', 1)

# ##judas = [1]
bible('Jude', 1)

# ##apocalipse = [22]
bible('Revelation', 22)
