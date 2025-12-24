def bubble_sort_recursive(arr, n):
    if n <= 1:
        return
    def inner(j):
        if j >= n - 1:
            return
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        inner(j + 1)
    inner(0)
    bubble_sort_recursive(arr, n - 1)

def wiggle_sort_recursive(nums, n):
    bubble_sort_recursive(nums, n)
    mid = (n + 1) // 2
    left = [0] * mid
    right = [0] * (n - mid)
    
    def copy_left(i):
        if i >= mid:
            return
        left[i] = nums[i]
        copy_left(i + 1)
        
    def copy_right(i, j):
        if i >= n:
            return
        right[j] = nums[i]
        copy_right(i + 1, j + 1)
        
    copy_left(0)
    copy_right(mid, 0)
    
    result = [0] * n
    
    def place_left(i):
        if i >= mid:
            return
        result[2 * i] = left[mid - 1 - i]
        place_left(i + 1)
        
    def place_right(i):
        if i >= n - mid:
            return
        result[2 * i + 1] = right[n - mid - 1 - i]
        place_right(i + 1)
        
    place_left(0)
    place_right(0)
    
    return result

size = int(input("Enter the length of the array: "))
nums = [0] * size
i = 0
while i < size:
    nums[i] = int(input(f"Enter element {i + 1}: "))
    i += 1

result = wiggle_sort_recursive(nums, size)
i = 0
while i < size:
    print(result[i], end=" ")
    i += 1
