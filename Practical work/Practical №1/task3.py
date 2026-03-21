input_numbers = input("Введите числа через пробел: ").split()
K = int(input("Введите число K: "))

# Преобразуем строки в целые числа и фильтруем кратные K
numbers_list = [int(x) for x in input_numbers if int(x) % K == 0]

print("Числа, кратные K:", numbers_list)
print()
