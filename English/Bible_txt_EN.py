# Function to create the file
def bible_start(book, num_chapters):
    content = []
    for c in range(1, num_chapters + 1):
        content.append(f'{book} {c}\n')
    with open('Bible.txt', 'w') as arq:
        for item in content:
            arq.writelines(item)

# Function to add to existing file
def bible(book, num_chapters):
    content = []
    for c in range(1, num_chapters +1):
        content.append(f'{book} {c}\n')
    with open('Bible.txt', 'a') as arq:
        for item in content:
            arq.writelines(item)
        
bible_start('Genesis', 50)

bible('Exodus', 40)

bible('Leviticus', 27)

bible('Numbers', 36)

bible('Deuteronomy', 34)

bible('Joshua', 24)

bible('Judges', 21)

bible('Ruth', 4)

bible('1 Samuel', 31)

bible('2 Samuel', 24)

bible('1 Kings', 22)

bible('2 Kings', 25)

bible('1 Chronicles', 29)

bible('2 Chronicles', 36)

bible('Ezra', 10)

bible('Nehemiah', 13)

bible('Esther', 10)

bible('Job', 42)

bible('Psalms', 150)

bible('Proverbs', 31)

bible('Ecclesiastes', 12)

bible('Song of Solomon', 8)

bible('Isaiah', 66)

bible('Jeremiah', 52)

bible('Lamentations', 5)

bible('Ezekiel', 48)

bible('Daniel', 12)

bible('Hosea', 14)

bible('Joel', 3)

bible('Amos', 9)

bible('Obadiah', 1)

bible('Jonah', 4)

bible('Micah', 7)

bible('Nahum', 3)

bible('Habakkuk', 3)

bible('Zephaniah', 3)

bible('Haggai', 2)

bible('Zechariah', 14)

bible('Malachi', 4)

bible('Matthew', 28)

bible('Mark', 16)
    
bible('Luke', 24)

bible('John', 21)

bible('Acts', 28)

bible('Romans', 16)

bible('1 Corinthians', 16)

bible('2 Corinthians', 13)

bible('Galatians', 6)

bible('Ephesians', 6)

bible('Philippians', 4)

bible('Colossians', 4)

bible('1 Thessalonians', 5)

bible('2 Thessalonians', 3)

bible('1 Timothy', 6)

bible('2 Timothy', 4)

bible('Titus', 3)

bible('Philemon', 1)

bible('Hebrews', 13)

bible('James', 5)

bible('1 Peter', 5)

bible('2 Peter', 3)

bible('1 John', 5)

bible('2 John', 1)

bible('3 John', 1)

bible('Jude', 1)

bible('Revelation', 22)
