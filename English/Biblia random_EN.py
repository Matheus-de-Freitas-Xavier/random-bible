import random
import datetime

today = datetime.date.today().strftime("%d/%m/%Y")

with open('Bible.txt', 'r') as arq:
    content = arq.readlines()
    content_clear = [item.strip() for item in content]
    aleatory = random.choice(content_clear)
    
    while aleatory.endswith('(X)'):
        aleatory = random.choice(content_clear)   
        
    index = content_clear.index(aleatory)
    content_clear.pop(index)
    content_clear.insert(index, f'{aleatory} (X)')
    
with open('Bible.txt', 'w') as arq:
    for item in content_clear:
        arq.write(item + '\n')

defined = f'{today} ---- {aleatory} (X)'
print(defined)

with open('Bible_done.txt' , 'a') as arq:
    arq.write(defined + '\n')
