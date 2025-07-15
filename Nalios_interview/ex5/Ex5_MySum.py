# Ex 5: MySum
# - Write a function that takes an array of numbers in parameter (no joke : no None, no
# strings, only real numbers)
# - Output the sum of these number, without using the sum() function.

# Will work with floats and integers (positive and negative).
def MySum(array):
    total = 0  
    for number in array:  
        total += number 
    return total


# Bonus :
# I would need to call the sum fucntion on itself to sum the numbers in the array.
# I cannot really see how i could do it so i'll skip this one. 




# Test cases:
test_array1 = [1, 2, 3, 4, 5]
test_array2 = [10, -2, 3.5, 4.5, 0]
test_array3 = [-1, -2, -3, -4, -5]
test_array4 = [0, 0, 0, 0]     
print(MySum(test_array1))  # Output: 15
print(MySum(test_array2))  # Output: 16.0
print(MySum(test_array3))  # Output: -15
print(MySum(test_array4))  # Output: 0