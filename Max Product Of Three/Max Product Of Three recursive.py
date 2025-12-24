def readInteger(prompt):
    while True:
        print(prompt, end=" ")
        s = input()
        if s == "":
            print("Error: Empty value is not allowed!")
            continue
        try:
            number = int(s)
            return number
        except:
            print("Error: Invalid integer!")

def recursiveScan(A, index, n, max1, max2, max3, min1, min2):
    if index == n:
        return max1, max2, max3, min1, min2
    
    x = A[index]
    
    if x > max1:
        max3 = max2
        max2 = max1
        max1 = x
    elif x > max2:
        max3 = max2
        max2 = x
    elif x > max3:
        max3 = x
        
    if x < min1:
        min2 = min1
        min1 = x
    elif x < min2:
        min2 = x
        
    return recursiveScan(A, index + 1, n, max1, max2, max3, min1, min2)

def maxProductOfThreeRecursive(A, n):
    max1 = float('-inf')
    max2 = float('-inf')
    max3 = float('-inf')
    min1 = float('inf')
    min2 = float('inf')
    
    max1, max2, max3, min1, min2 = recursiveScan(
        A, 0, n, max1, max2, max3, min1, min2
    )
    
    product1 = max1 * max2 * max3
    product2 = max1 * min1 * min2
    
    if product1 > product2:
        return product1
    else:
        return product2


def main():
    while True:
        n = readInteger("Enter array size:")
        if n < 3:
            print("Error: Size must be at least 3!")
        else:
            break
            
    A = [0] * n
    for i in range(n):
        A[i] = readInteger(f"Enter element {i+1}:")
        
    result = maxProductOfThreeRecursive(A, n)
    print("Maximum product of three numbers =", result)

main()