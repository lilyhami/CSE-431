# This file is used to generate a graph that plots the average runtimes for sorting lists of varying lengths using
# merge sort, insertion sort, and a hybrid tim-sort

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


# now graph using optimal k and compare to insertion and merge sort graphs
# test using mulitples of 8 up to 64 for k
x_merge = []
y_merge = []
x_insert = []
y_insert = []
x_hybrid = []
y_hybrid = []

for num in range(1, 100):
    data_to_avg_hybrid = []
    for i in range(50):
        data = random.sample(range(1, 100), num)
        start_time = time.time()
        timSort(data, 32)
        data_to_avg_hybrid.append(time.time()-start_time)
    hybrid_sort_avg = sum(data_to_avg_hybrid) / len(data_to_avg_hybrid)

    data_to_avg_merge = []
    for i in range(50):
        data = random.sample(range(1, 100), num)
        start_time = time.time()
        mergeSort(data)
        data_to_avg_merge.append(time.time() - start_time)

    mergesort_avg = sum(data_to_avg_merge) / len(data_to_avg_merge)

    data_to_avg_insert = []
    for i in range(50):
        data = random.sample(range(1, 100), num)
        start_time = time.time()
        insertionSort(data)
        data_to_avg_insert.append(time.time() - start_time)

    insertsort_avg = sum(data_to_avg_insert) / len(data_to_avg_insert)

    x_merge.append(num)
    y_merge.append(mergesort_avg)
    x_insert.append(num)
    y_insert.append(insertsort_avg)
    x_hybrid.append(num)
    y_hybrid.append(hybrid_sort_avg)

plt.plot(x_merge, y_merge, label="merge sort")
plt.plot(x_insert, y_insert, label="insertion sort")
plt.plot(x_hybrid, y_hybrid, label="hybrid sort(k=32)")

plt.title('MergeSort vs. InsertionSort vs. HybridSort')
plt.xlabel('input size')
plt.ylabel('average runtime (seconds)')
plt.tight_layout()
plt.legend()
plt.show()
plt.show()

