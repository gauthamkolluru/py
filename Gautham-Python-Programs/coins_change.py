def change_coins(amount=None):
    denominations = {50: 5, 25: 5, 5: 10, 1: 20}
    if amount:
        for denomination in sorted(denominations, reverse=True):
            if amount >= denomination:
                if amount % denomination:
                    return (amount // denomination) + change_coins(amount % denomination)
                else:
                    return amount // denomination


print(change_coins(85))


# amount - ((amount // denomination) * denomination)