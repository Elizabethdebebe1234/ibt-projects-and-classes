numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] 
print(numbers[1])

# Big-O: O(1)
# Reason: Accessing an item by index takes constant time.

for num in numbers:
    print(num)

# Big-O: O(n)
# Reason: The loop visits every element once.

for i in numbers:
    for j in numbers:
        print(i, j)

# Big-O: O(n²)
# Reason: One loop runs inside another loop.

student = {
    "name": "Almaz"
}

print(student["name"])

# Big-O: O(1)
# Reason: Dictionary lookup is constant time.



target = 14

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        print("Found at index", mid)
        break

    elif numbers[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

# Big-O: O(log n)
# Reason: Each step cuts the search space in half.