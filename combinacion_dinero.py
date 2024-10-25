money = [1, 5, 10, 20, 50, 100]
suma = 0
comb = []

def start(num_init, suma, comb):
    if suma == num_init:
        print(comb)
        return
    if suma > num_init:
        return
    for coin in money:
        if not comb or coin >= comb[-1]:
            start(num_init, suma + coin, comb + [coin])

start(20, suma, comb)
