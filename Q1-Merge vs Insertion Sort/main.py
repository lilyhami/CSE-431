import time
import random
import matplotlib.pyplot as plt


# https://www.geeksforgeeks.org/merge-sort/
# Python program for implementation of MergeSort
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


x_merge = []
y_merge = []
x_insert = []
y_insert = []
special_input_val = []

for num in range(60, 80):
    data_to_avg_merge = []
    for i in range(50):
        data = random.sample(range(1, 1000000), num)
        start_time = time.time()
        mergeSort(data)
        data_to_avg_merge.append(time.time() - start_time)

    mergesort_avg = sum(data_to_avg_merge) / len(data_to_avg_merge)
    # print("MergeSort average runtime for num =", num, ": %s seconds" % mergesort_avg)

    data_to_avg_insert = []
    for i in range(50):
        data = random.sample(range(1, 1000000), num)
        start_time = time.time()
        insertionSort(data)
        data_to_avg_insert.append(time.time() - start_time)

    insertsort_avg = sum(data_to_avg_insert) / len(data_to_avg_insert)
    # print("InsertionSort average runtime for num =", num, ": %s seconds" % insertsort_avg)
    # print("--------------------")

    if mergesort_avg < insertsort_avg:
        x = num
        if len(special_input_val) == 0:
            special_input_val.append(x)
            print(special_input_val)
    else:
        pass

    x_merge.append(num)
    y_merge.append(mergesort_avg)
    x_insert.append(num)
    y_insert.append(insertsort_avg)


plt.plot(x_merge, y_merge, label="merge sort")
plt.plot(x_insert, y_insert, label="insertion sort")
plt.title('MergeSort vs. InsertionSort')
plt.xlabel('input size')
plt.ylabel('average runtime (seconds)')
plt.tight_layout()
plt.legend()
plt.show()
