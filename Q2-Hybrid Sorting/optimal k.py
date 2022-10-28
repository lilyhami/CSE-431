# This file is used to generate a graph that tells us the optimal k value to use
# in our hybrid timSort

import time
import random
import matplotlib.pyplot as plt

# https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# https://www.geeksforgeeks.org/insertion-sort/
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Python program for implementation of timSort heavily based on MergeSort and calls InsertionSort
# uses merge sort when length of array is > than k and insertion sort when 1<len(array)<=k
def timSort(arr, k):
    if len(arr) > 1 and len(arr) > k:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        timSort(L, k)

        # Sorting the second half
        timSort(R, k)

        insertionSort(L)
        insertionSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    elif len(arr) > 1:
        insertionSort(arr)


# determine optimal k
x_axis = []
y_axis = []
optimal_k = []
for num in range(1, 100):
    data_all_hybrid = []
    for k in range(1, 100):
        if k <= num:
            data_to_avg_hybrid = []
            for i in range(50):
                data = random.sample(range(1, 100), num)
                start_time = time.time()
                timSort(data, k)
                data_to_avg_hybrid.append(time.time()-start_time)
            hybrid_sort_avg = sum(data_to_avg_hybrid) / len(data_to_avg_hybrid)
            data_all_hybrid.append(hybrid_sort_avg)

    min_value = min(data_all_hybrid)
    min_index = data_all_hybrid.index(min_value)
    optimal_k.append(min_index)

    x_axis.append(num)

plt.plot(x_axis, optimal_k, label="optimal k value for lists of varying length")

plt.title('Determining Optimal K Values')
plt.xlabel('length of list')
plt.ylabel('optimal k value')
plt.tight_layout()
plt.legend()
plt.show()
plt.show()
