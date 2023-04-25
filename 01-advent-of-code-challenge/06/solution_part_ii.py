with open('input5.txt', encoding="utf-8",mode='r') as tabela:
    lines = tabela.readline().strip()#faz todo input em uma linha só
    total = []
    for x in range(len(lines)):
      total.append(lines[x:x+14])
    for x in total:
      if len(set(x)) == 14: # A função set() faz com que cada elemento de x se torne um elementos diferentes/isolados e não permite objetos repetidos
        print(total.index(x)+14)
        break;