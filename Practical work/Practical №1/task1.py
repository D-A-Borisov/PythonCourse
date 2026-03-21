N = int(input("Введите количество имен: "))
names = []

for _ in range(N):
    names.append(input("Введите имя: "))

uni = []
lengths = set()

for name in names:
    if len(name) not in lengths:
        uni.append(name)
        lengths.add(len(name))

print("Исходный список:", names)
print("Список уникальной длины:", uni)
