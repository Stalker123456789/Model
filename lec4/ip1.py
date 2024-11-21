import random

flowers = ["роза", "тюльпан", "ромашка", "подсолнух"]
colors = ["красный", "синий", "желтый", "белый", "фиолетовый", "оранжевый"]
flower_colors = dict(zip(flowers, [random.choice(colors) for _ in flowers]))
print(flower_colors)
