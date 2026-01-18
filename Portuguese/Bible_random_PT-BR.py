import random
import datetime

hoje = datetime.date.today().strftime("%d/%m/%Y")

with open('Biblia.txt', 'r') as arq:
    conteudo = arq.readlines()
    conteudo_limpo = [item.strip() for item in conteudo]
    aleatorio = random.choice(conteudo_limpo)
    
    while aleatorio.endswith('(X)'):
        aleatorio = random.choice(conteudo_limpo)   
        
    index = conteudo_limpo.index(aleatorio)
    conteudo_limpo.pop(index)
    conteudo_limpo.insert(index, f'{aleatorio} (X)')
    
with open('Biblia.txt', 'w') as arq:
    for item in conteudo_limpo:
        arq.write(item + '\n')

definido = f'{hoje} ---- {aleatorio} (X)'
print(definido)

with open('Biblia_done.txt' , 'a') as arq:
    arq.write(definido + '\n')
