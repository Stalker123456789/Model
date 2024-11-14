import math
def calculate_area():
    print("Выберите фигуру для расчета площади:")
    print("1. Круг")
    print("2. Прямоугольник")
    print("3. Треугольник")
    
    choice = input("Введите номер фигуры (1-3): ")
    
    if choice == '1':
        radius = float(input("Введите радиус круга: "))
        area = math.pi * (radius ** 2)
        print(f"Площадь круга: {area:.2f}")
    
    elif choice == '2':
        width = float(input("Введите ширину прямоугольника: "))
        height = float(input("Введите высоту прямоугольника: "))
        area = width * height
        print(f"Площадь прямоугольника: {area:.2f}")
    
    elif choice == '3':
        base = float(input("Введите основание треугольника: "))
        height = float(input("Введите высоту треугольника: "))
        area = 0.5 * base * height
        print(f"Площадь треугольника: {area:.2f}")
    
    else:
        print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")
calculate_area()
