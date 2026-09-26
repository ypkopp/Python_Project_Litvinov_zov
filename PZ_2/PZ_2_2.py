number = input("Ввод числа: ")
number = int(number)
result = number % 100 * 10 + number // 100
print("Полученное число:", result)