with open("input3.txt", encoding="utf-8", mode="r")as tabela:
  lines = [(x.replace('\n', "")) for x in tabela.readlines()]
  components = []
  total = []
  counter = 0
  for x in lines:
    rangeA, rangeB = x.split(",")
    start1, end1 = map(int, rangeA.split("-"))
    start2, end2 = map(int, rangeB.split("-"))
    if (start1 >= start2 and end1 <= end2) or (start1 <= start2 and end1 >= end2):
      counter += 1
  print(counter)