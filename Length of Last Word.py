# Dada uma string s que consiste em palavras e espaços, retorne o comprimento da
# última palavra da string.
# Uma palavra é um máximo substring consistindo apenas em caracteres sem espaço.
# Exemplo 1:
# Entrada: s = "Hello World"
# Saída: 5
# Explicação: A última palavra é “World” com comprimento 5.

def length_of_last_word(string):
  splited = string.split(" ")
  for worlds in splited[-1:]:
    return len(worlds)

length_of_last_word(" ")