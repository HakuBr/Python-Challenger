# Você recebe uma matriz de preços onde os preços[i] são o preço de uma determi
# nada ação no i-ésimo dia. Você deseja maximizar seu lucro escolhendo um único
# dia para comprar uma ação e escolhendo um dia diferente no futuro para vendê-la.
# Retorne o lucro máximo que você pode obter com esta transação. Se você não
# conseguir obter nenhum lucro, retorne 0.
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Observe que não é permitido comprar no dia 2 e vender no dia 1 porque você deve comprar antes de vender.
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
def best_time_to_buy_and_sell_stock(prices):
 print(prices[prices.index(max(prices[prices.index(min(prices)):]))]-prices[prices.index(min(prices))])

best_time_to_buy_and_sell_stock([7,6,4,3,1])

# Testando para a conexão entre as plataformas
# Aqui escrevi outra linha