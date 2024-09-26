import random
import secrets
import time
from collections import Counter

random_numbers = [random.randint(1, 16) for _ in range(100)]

secrets_numbers = [secrets.randbelow(16) + 1 for _ in range(100)]

random_counts = Counter(random_numbers)
secrets_counts = Counter(secrets_numbers)

print("Random counts:", random_counts)
print("Secrets counts:", secrets_counts)

random_large_numbers = [random.randint(1, 65535) for _ in range(100)]
random_large_counts = Counter(random_large_numbers)
print("Random large counts:", random_large_counts)

secrets_large_numbers = [secrets.randbelow(65535) + 1 for _ in range(100)]
secrets_large_counts = Counter(secrets_large_numbers)
print("Secrets large counts:", secrets_large_counts)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

start_time = time.time()
bubble_sort(random_numbers.copy())
print("Bubble sort time (1-16):", time.time() - start_time)

start_time = time.time()
bubble_sort(random_large_numbers.copy())
print("Bubble sort time (1-65535):", time.time() - start_time)

start_time = time.time()
random_numbers.copy().sort()
print("Built-in sort time (1-16):", time.time() - start_time)

start_time = time.time()
random_large_numbers.copy().sort()
print("Built-in sort time (1-65535):", time.time() - start_time)

random_large_list_16 = [random.randint(1, 16) for _ in range(500)]

start_time = time.time()
bubble_sort(random_large_list_16.copy())
print("Bubble sort time (500 elements, 1-16):", time.time() - start_time)

start_time = time.time()
random_large_list_16.copy().sort()
print("Built-in sort time (500 elements, 1-16):", time.time() - start_time)

random_large_list_65535 = [random.randint(1, 65535) for _ in range(500)]

start_time = time.time()
bubble_sort(random_large_list_65535.copy())
print("Bubble sort time (500 elements, 1-65535):", time.time() - start_time)

start_time = time.time()
random_large_list_65535.copy().sort()
print("Built-in sort time (500 elements, 1-65535):", time.time() - start_time)
