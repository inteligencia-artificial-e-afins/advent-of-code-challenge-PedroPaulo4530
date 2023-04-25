with open("input3.txt", encoding="utf-8", mode="r")as tabela:
  lines = [(x.replace('\n', "")) for x in tabela.readlines()]
  components = []
  total = []
  counter = 0
  for x in lines:
    rangeA, rangeB = x.split(",")
    start1, end1 = map(int, rangeA.split("-"))
    start2, end2 = map(int, rangeB.split("-"))
    if start2 in range(start1, end1+1) or end2 in range(start1, end1+1) or start1 in range(start2, end2+1) or end1 in range(start2, end2+1):
      counter += 1
  print(counter)