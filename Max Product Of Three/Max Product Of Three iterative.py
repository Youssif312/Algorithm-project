def maxProductOfThree(A, n):
    max1 = float('-inf')
    max2 = float('-inf')
    max3 = float('-inf')
    
    min1 = float('inf')
    min2 = float('inf')
    
    for x in A:
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
            
    product1 = max1 * max2 * max3
    product2 = max1 * min1 * min2
    
    return product1 if product1 > product2 else product2

def get_valid_input(prompt, min_value=None):
    while True:
        user_input = input(prompt)
        
        is_empty = True
        for char in user_input:
            if char != ' ':
                is_empty = False
                break
        
        if is_empty:
            print("Input cannot be empty. Please enter a number.")
            continue
            
        try:
            val = int(user_input)
            
            if min_value is not None and val < min_value:
                print(f"Value must be at least {min_value}.")
                continue
                
            return val
            
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    n = get_valid_input("Enter array size: ", min_value=3)
    A = [get_valid_input(f"Enter element {i+1}: ") for i in range(n)]
    print("Maximum product of three numbers =", maxProductOfThree(A, n))

main()