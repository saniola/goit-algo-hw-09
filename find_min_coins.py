from constants import coin_denominations


def find_min_coins(amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    coin_used = [-1] * (amount + 1)

    for coin in coin_denominations:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    coins = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in coins:
            coins[coin] += 1
        else:
            coins[coin] = 1
        current_amount -= coin

    return coins
