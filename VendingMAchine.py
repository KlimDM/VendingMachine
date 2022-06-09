def banknote_inserting(banknote, banknotes_counter):
    global balance
    if banknote in banknotes_counter:
        banknotes_counter[banknote] += 1
        balance += banknote
    else:
        return 'Insert a valid banknote!!!'
    return 'Your balance {}$'.format(balance)


def product_sell(product_name):
    global balance, current_assortment
    if product_name in current_assortment:
        if balance >= current_assortment[product_name]['price']:
            balance -= current_assortment[product_name]['price']
            current_assortment[product_name]['quantity'] -= 1
            if current_assortment[product_name]['quantity'] == 0:
                del current_assortment[product_name]
            return 'You bought {}'.format(product_name)
        else:
            return 'Not enough balance, need {}$ more '.format(current_assortment[product_name]['price'] - balance)
    else:
        return 'No {} in stock, check available products'.format(product_name)


def get_change(change_coins):
    global balance
    change = {}
    for value in sorted(change_coins, reverse=True):
        quant = min(balance // value, change_coins[value]['quantity'])
        if quant > 0:
            change[value] = quant
        change_coins[value]['quantity'] -= quant
        balance -= value * quant
        if balance == 0: break
    return change


max_quant = 15

original_assortment = {'snickers': {'price': 20, 'quantity': max_quant}, 'sprite': {'price': 35, 'quantity': max_quant},
                       '7day\'s': {'price': 35, 'quantity': max_quant},
                       'ritter sport': {'price': 100, 'quantity': max_quant}}

current_assortment = original_assortment.copy()

banknotes_counter = {50: 0, 100: 0, 200: 0, 500: 0}

original_change_coins = {10: {'quantity': 400}, 5: {'quantity': 400}, 2: {'quantity': 400}, 1: {'quantity': 400}}

change_coins = original_change_coins.copy()

balance = 0

while True:
    button = input('''
                   1. Insert a banknote
                   2. Show available products
                   3. Select a product
                   4. Get the change
                   ''')
    if button == '1':
        banknote = input('Insert a banknote > ')
        try:
            int(banknote)
        except ValueError:
            continue
        print(banknote_inserting(int(banknote), banknotes_counter))
    elif button == '2':
        print('Your balance is {}$\n'.format(balance))
        for key in current_assortment:
            print('{0} --> {1}$'.format(key, current_assortment[key]['price']), end=', ')
    elif button == '3':
        print('Your balance is {}$\n'.format(balance))
        avail_products = {key: value for key, value in
                          current_assortment.items() if balance >= current_assortment[key]['price']}
        if not avail_products:
            print('Not enough cash')
            continue
        for key in avail_products:
            print('{0} --> {1}$'.format(key, avail_products[key]['price']), end=', ')
        product = input('\nSelect a product --> ')
        print(product_sell(product))
    elif button == '4':
        final_change = get_change(change_coins)
        for value in final_change:
            print('{0}$ --> {1} coins'.format(value, final_change[value]))
    elif button == 'srvop17':
        current_assortment = original_assortment.copy()
        change_coins = original_change_coins.copy()
        sum_cash = 0
        for value in banknotes_counter:
            sum_cash += value * banknotes_counter[value]
            print('{0} --> {1} banknotes'.format(value, banknotes_counter[value]))
            banknotes_counter[value] = 0
        print('Yor total cash is {0}$\n'.format(sum_cash))
        key = input('press any key to continue')
        if key:
            continue
