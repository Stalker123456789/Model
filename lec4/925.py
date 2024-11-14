def srednee(arr):
    if len(arr) == 0:
        return 0 
    total_sum = sum(arr)
    avg = total_sum / len(arr)
    return avg
chisla = [1, 19, 81, 7, 27]
result = srednee(chisla)
print(f"Среднее арифметическое: {result}")
