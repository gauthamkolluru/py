def change_coins(amount=None):
    denominations = {50: 5, 25: 5, 5: 10, 1: 20}
    if amount:
        for denomination in sorted(denominations, reverse=True):
            if amount >= denomination:
                if amount % denomination:
                    return (amount // denomination) + change_coins(amount - ((amount // denomination) * denomination))
                else:
                    return amount // denomination


print(change_coins(47))
