prices = list(map(float, input("\nВведите цены через пробел: ").split()))
K = float(input("Введите K: "))
M = float(input("Введите M: "))

discount = [price - (int(price // K) * M) for price in prices]

print("Цены до скидки:", prices)
print("Цены после скидки:", discount)
