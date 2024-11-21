name = "Ivanov Andrew Alekseevich"  
upper_case_chars = [ord(char) for char in name.upper()]
lower_case_chars = [ord(char) for char in name.lower()]
sum_upper = sum(upper_case_chars)
sum_lower = sum(lower_case_chars)
print(f"Строка: {name}")
print(f"Список символов в верхнем регистре: {upper_case_chars}")
print(f"Список символов в нижнем регистре: {lower_case_chars}")
print(f"Сумма ASCII кодов (верхний регистр): {sum_upper}")
print(f"Сумма ASCII кодов (нижний регистр): {sum_lower}")
