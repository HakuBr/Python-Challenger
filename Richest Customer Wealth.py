# Você recebe uma grade de contas inteiras m x n onde contas[i][j] é a
# quantidade de dinheiro que o i​​​​​​​​​​​ésimo​​​​ cliente tem no j​​​​​ésimo​​​​ banco. Devolva a
# riqueza que o cliente mais rico possui. A riqueza de um cliente é a quantidade
# de dinheiro que ele possui em todas as suas contas bancárias.
# O cliente mais rico é aquele que possui a riqueza máxima.

# Example 2:

# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
# Explanation:
# 1st customer has wealth = 6
# 2nd customer has wealth = 10
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.

def richest_customer_wealth(matriz):
  soma = []
  for x in matriz:
    soma.append(sum(x))
  sorted_sum = sorted(soma, reverse = True)
  return sorted_sum[0]

richest_customer_wealth([[1,2,3],[3,2,1]])