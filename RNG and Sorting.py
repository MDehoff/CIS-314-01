import random
import secrets
import time
from collections import Counter

randnum_1to16 = [random.randint(1, 16) for _ in range(100)]
countsrand_1to16 = Counter(randnum_1to16)

print("Counts using random:")
print(countsrand_1to16)

randnumsecrets_1to16 = [secrets.randbelow(16) + 1 for _ in range(100)]
countssecret_1to16 = Counter(randnumsecrets_1to16)

print("Counts using secrets:")
print(countssecret_1to16)

print("Is there a difference in counts?")
print("Random Counts:", countsrand_1to16)
print("Secrets Counts:", countssecret_1to16)

random_numbers_1_to_65535 = [random.randint(1, 65535) for _ in range(100)]
counts_random_1_to_65535 = Counter(random_numbers_1_to_65535)

print("Counts using random (1-65535):")
print(counts_random_1_to_65535)

random_numbers_secrets_1_to_65535 = [secrets.randbelow(65535) + 1 for _ in range(100)]
counts_secrets_1_to_65535 = Counter(random_numbers_secrets_1_to_65535)

print("Counts using secrets (1-65535):")
print(counts_secrets_1_to_65535)

def bubble_sort(arr):
    # Simple implementation of bubble sort
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

start_time = time.time()
bubble_sort(random_numbers_1_to_16)
print("Custom sort time (1-16):", time.time() - start_time)

start_time = time.time()
sorted_random_1_to_16 = sorted(random_numbers_1_to_16)
print("Built-in sort time (1-16):", time.time() - start_time)

start_time = time.time()
bubble_sort(random_numbers_1_to_65535)
print("Custom sort time (1-65535):", time.time() - start_time)

start_time = time.time()
sorted_random_1_to_65535 = sorted(random_numbers_1_to_65535)
print("Built-in sort time (1-65535):", time.time() - start_time)

random_numbers_1_to_16_500 = [random.randint(1, 16) for _ in range(500)]

start_time = time.time()
bubble_sort(random_numbers_1_to_16_500)
print("Custom sort time (500 elements, 1-16):", time.time() - start_time)

start_time = time.time()
sorted_random_1_to_16_500 = sorted(random_numbers_1_to_16_500)
print("Built-in sort time (500 elements, 1-16):", time.time() - start_time)

random_numbers_1_to_65535_500 = [random.randint(1, 65535) for _ in range(500)]

start_time = time.time()
bubble_sort(random_numbers_1_to_65535_500)
print("Custom sort time (500 elements, 1-65535):", time.time() - start_time)

start_time = time.time()
sorted_random_1_to_65535_500 = sorted(random_numbers_1_to_65535_500)
print("Built-in sort time (500 elements, 1-65535):", time.time() - start_time)
