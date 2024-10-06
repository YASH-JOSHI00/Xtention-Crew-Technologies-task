def find_missing(arr, n):
    # Calculate the expected sum of numbers from 1 to n
    total_sum = n * (n + 1) // 2
    
    # Calculate the sum of numbers in the array
    arr_sum = sum(arr)
    
    # The missing number is the difference between the total sum and the array sum
    missing_number = total_sum - arr_sum
    
    return missing_number

# Example usage:
arr = [1, 2, 4, 5, 6]
n = 6
print("The missing number is:", find_missing(arr, n))
