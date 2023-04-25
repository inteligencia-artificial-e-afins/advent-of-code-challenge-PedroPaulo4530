with open("input2.txt", encoding="utf-8", mode="r")as tabela:
  lines = [x.replace("\n", "")for x in tabela.readlines()]
  priority = {}
  total = 0
  letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for x, y in enumerate(letras):
    priority[y] = x + 1
  for x in range(0, len(lines), 3):
    for y in lines[x]:
      if y in lines[x+1] and y in lines[x+2]:
        total += priority[y]
        break;
  print(total)