def change_coins(amount = None):
    coins_draw = {50:5, 25:5, 5:10, 1:20}
    if amount:
        for i in sorted(coins_draw, reverse=True):
            if amount >= i:
                if amount % i:
                    return (amount // i) + change_coins(amount - ((amount // i) * i))
                else:
                    return amount // i


print(change_coins(47))