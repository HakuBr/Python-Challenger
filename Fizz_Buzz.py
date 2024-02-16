# Dado um número inteiro n, retorne uma resposta de matriz de string
# (indexada em 1) onde:
# resposta[i] == "FizzBuzz" se i for divisível por 3 e 5.
# resposta[i] == "Fizz" se i for divisível por 3.
# resposta[i] == "Buzz" se i for divisível por 5.
# resposta[i] == i (como uma string) se nenhuma das condições acima for verdadeira.
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]

def FuzzBuzzChallenger(inteiro):
  lista = list()
  for i in range(1,inteiro+1):
    if i%3 == 0 and i%5==0:
      lista.append("FuzzBuzz")
    elif i%3 == 0:
      lista.append("Fizz")
    elif i%5 == 0:
      lista.append("Buzz")
    else:
      lista.append(str(i))
  print(lista)

FuzzBuzzChallenger(15)