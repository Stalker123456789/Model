n = int(input("Введите n: ")) 
a = 0 
b = 1 
i = 0 
if n <= 0: 
    print("Введите положительное число") 
else: 
    print("Первые", n, "чисел Фибоначчи:") 
    while i < n: 
        print(a, end=" ") 
        c = a + b 
        a = b 
        b = c 
        i += 1 
