from constants import coin_denominations


def find_coins_greedy(amount):
    coins_used = {}

    for coin in sorted(coin_denominations, reverse=True):
        if amount >= coin:
            num_coins = amount // coin

            coins_used[coin] = num_coins

            amount -= num_coins * coin

    return coins_used
