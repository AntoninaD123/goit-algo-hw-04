

#я зробила лише основне завдання, дякую 🤩 

import random
import timeit

# -------------------------------
# 1. Алгоритм сортування вставками
# -------------------------------
def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# -------------------------------
# 2. Алгоритм сортування злиттям
# -------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# -------------------------------
# 3. Timsort (вбудований sorted)
# -------------------------------
def timsort(arr):
    return sorted(arr)

# -------------------------------
# Генерація тестових даних
# -------------------------------
sizes = [100, 1000, 5000, 10000]
for n in sizes:
    data = [random.randint(0, 100000) for _ in range(n)]
    
    t_insertion = timeit.timeit(lambda: insertion_sort(data), number=1)
    t_merge = timeit.timeit(lambda: merge_sort(data), number=1)
    t_timsort = timeit.timeit(lambda: timsort(data), number=1)
    
    print(f"Масив розміром {n}:")
    print(f"  Insertion sort: {t_insertion:.5f} секунд")
    print(f"  Merge sort:     {t_merge:.5f} секунд")
    print(f"  Timsort:        {t_timsort:.5f} секунд")
    print("-" * 40)
