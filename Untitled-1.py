# Завдання 1. 
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))
num4 = float(input("Введіть четверте число: "))

# Завдання 2. 
addition = num1 + num2 + num3 + num4
subtraction = num1 - num2 - num3 - num4
multiplication = num1 * num2 * num3 * num4
division = num1 / num2 / num3 / num4 if num2 != 0 and num3 != 0 and num4 != 0 else "Ділення на нуль!"
power = num1 ** num2
integer_division = num1 // num2 if num2 != 0 else "Ділення на нуль!"
modulus = num1 % num2 if num2 != 0 else "Ділення на нуль!"


results = [addition, subtraction, multiplication, division, power, integer_division, modulus]

# Завдання 3.
number_of_elements = len(results)


print("Парні елементи списку:")
for i, result in enumerate(results):
    if isinstance(result, (int, float)) and result % 2 == 0:
        print(f"Елемент {i+1}: {result}")

# Завдання 4.
results[1], results[4] = results[4], results[1]


print("Список після зміни місцями другого і п’ятого елементів:")
print(results)

# Завдання 5. 
name = input("Введіть ваше прізвище та ім’я: ")


print(f"Виконавець: {name}")
print("Висновок по лабораторній роботі:")
print("Було створено чотири змінні з цілими та дробовими числами.")
print("Було виконано основні арифметичні операції над числами.")
print("Результати операцій були записані у список та були знайдені парні елементи.")
print("Другий і п’ятий елементи списку були поміняні місцями.")

