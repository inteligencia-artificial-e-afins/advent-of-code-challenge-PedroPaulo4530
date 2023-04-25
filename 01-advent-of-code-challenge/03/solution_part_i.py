with open("input2.txt", encoding="utf-8", mode="r")as tabela:
  lines = [x.replace("\n", "") for x in tabela.readlines()]
  components = []
  priority = {}
  total = 0
  letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for x, y in enumerate(letras):
    priority[y] = x + 1
  for aux in lines:
    components.append(aux[:int(len(aux)/2)])
    components.append(aux[int(int(len(aux)/2)):int(len(aux))])
  for x in range(0, len(components), 2):
    for y in components[x]:
      if y in components[x+1]:
        total += priority[y]
        break;
  print(total)