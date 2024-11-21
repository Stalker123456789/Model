name = "Andrew Ivanov" 

def process_name(name):
    modified_name = "".join([char + "_" for char in name])
    ascii_codes = [ord(char) for char in modified_name]
    return ascii_codes
upper_ascii_codes = process_name(name.upper())
lower_ascii_codes = process_name(name.lower())
all_ascii_codes = upper_ascii_codes + lower_ascii_codes
max_ascii = max(all_ascii_codes)
min_ascii = min(all_ascii_codes)
print(f"Исходная строка: {name}")
print(f"ASCII-коды в верхнем регистре: {upper_ascii_codes}")
print(f"ASCII-коды в нижнем регистре: {lower_ascii_codes}")
print(f"Наибольший ASCII-код: {max_ascii}")
print(f"Наименьший ASCII-код: {min_ascii}")
