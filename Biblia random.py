import random
import datetime

hoje = datetime.date.today()
hoje2 = hoje.strftime("%d/%m/%Y")

with open('Biblia.txt', 'r') as arq:
    conteudo = arq.readlines()
    conteudo_limpo = [item.strip() for item in conteudo]
    aleatorio = random.choice(conteudo_limpo)
    while aleatorio.endswith('(X)'):
        aleatorio = random.choice(conteudo_limpo)   
    index = conteudo_limpo.index(aleatorio)
    conteudo_limpo.pop(index)
    conteudo_limpo.insert(index, f'{aleatorio} (X)')
with open('Biblia.txt', 'w') as arq2:
    for item in conteudo_limpo:
        arq2.write(item + '\n')
    
print(f'{hoje2} - (x) {aleatorio}')

with open('Biblia já foi.txt' , 'a') as arq:
    arq.write(f'{hoje2} --- {aleatorio} (X)\n')
