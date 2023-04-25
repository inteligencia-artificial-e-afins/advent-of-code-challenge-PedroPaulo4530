with open("input.txt", encoding="utf-8", mode="r")as tabela:
  lines = [(a.replace('\n', " ")) if a =="\n" else int(a.replace('\n', "")) for a in tabela.readlines()]
  arr = []
  total = []
  aux = 0
  for x in lines:
    if x == " ":    
      for i in arr:
        aux = aux + i;
      arr.clear()
      total.append(aux)
      aux = 0  
    else:
      arr.append(x)
  print(max(total))
