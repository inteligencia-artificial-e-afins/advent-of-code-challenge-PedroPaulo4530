#tive ajuda do Bruno para a formatação do input
with open('input4.txt',encoding="utf-8", mode='r') as tabela:
  components = []
  for x in range(8):
    components.append(tabela.readline().replace('\n',''))
  stack = tabela.readline()
  tabela.readline()
  
  steps = []
  part1 = []
  for x in tabela.readlines():
    x = x.replace('\n', '').split(' ')
    steps.append({ 'move': int(x[1]), 'from': int(x[3]), 'to': int(x[5]) })
  for x in range(9):
    idx = stack.index(str(x+1))
    aux=[]
    for y in components[:8]:
      if not y[idx] == ' ':
        aux.append(y[idx])
    part1.append(aux.copy())
  #print(part1)
  for x in steps:
    for y in range(x['move']):
        part1[x['to']-1].insert(0, part1[x['from']-1].pop(0))
  for x in range(9):
    print(part1[x][0])