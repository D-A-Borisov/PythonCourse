N = int(input("\nВведите число N: "))

numbers = list(range(N, N**2 + 1))
roots = [x**0.5 for x in numbers]

print("Числа:", numbers)
print("Квадратные корни:", roots)
