def bubble_sort(arr, n):
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i += 1

def wiggle_sort(nums, n):
    bubble_sort(nums, n)
    mid = (n + 1) // 2
    left = [0] * mid
    right = [0] * (n - mid)
    i = 0
    while i < mid:
        left[i] = nums[i]
        i += 1
    j = 0
    while i < n:
        right[j] = nums[i]
        i += 1
        j += 1
    result = [0] * n
    i = 0
    while i < mid:
        result[2 * i] = left[mid - 1 - i]
        i += 1
    i = 0
    while i < n - mid:
        result[2 * i + 1] = right[n - mid - 1 - i]
        i += 1
    return result

size = int(input("Enter the length of the array: "))
nums = [0] * size
i = 0
while i < size:
    nums[i] = int(input(f"Enter element {i + 1}: "))
    i += 1

result = wiggle_sort(nums, size)
i = 0
while i < size:
    print(result[i], end=" ")
    i += 1
