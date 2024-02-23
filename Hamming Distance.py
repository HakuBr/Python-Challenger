def hamming_distance(number1,number2):
  def binario(number):
    count = 0
    dividendo  = [number]
    binario = []
    while True:
      dividendo.append((dividendo[count]/2))
      binario.append(int(dividendo[count]%2))
      count += 1
      if dividendo[count] < 1:
        break
    binario.reverse()
    return binario
  binario1, binario2 = binario(number1),  binario(number2)
  diferenca = []
  if len(binario1) > len(binario2):
    for x in range(0, len(binario1) - len(binario2)):
      binario2.insert(0,0)
  else:
    for x in range(0, len(binario2) - len(binario1)):
      binario1.insert(0, 0)
  for x,y in binario1, binario2:
    if x != y:
      diferenca.append(1)
  return sum(diferenca)