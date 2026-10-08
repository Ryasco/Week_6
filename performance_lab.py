# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    most_common = max(counts, key=counts.get)
    return most_common

"""
Time and Space Analysis for problem 1:
- Best-case:O(n)
- Worst-case:O(n)
- Average-case: O(n)
- Space complexity:O(n)
- Why this approach? Only one pass is needed to count frequencies
- Could it be optimized? No.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
  

"""
Time and Space Analysis for problem 2:
- Best-case:O(n)
- Worst-case:O(n)
- Average-case: O(n)
- Space complexity:O(n)
- Why this approach? It uses a set for O(1) lookup time and a list to preserve order.
- Could it be optimized? No.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    pairs = []
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs
   

"""
Time and Space Analysis for problem 3:
- Best-case:O(n)
- Worst-case:O(n)
- Average-case: O(n)
- Space complexity:O(n)
- Why this approach? It uses a set for O(1) lookup time and a list to store pairs.
- Could it be optimized? No.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 4
    size = 0
    arr = [None] * capacity
    for i in range(n):
        if size == capacity:
            print(f"Resizing from {capacity} to {capacity * 2}")
            new_arr = [None] * new_capacity
            for j in range(size):
                new_arr[j] = arr[j]
            arr = new_arr
            capacity = new_capacity
        arr[size] = i
        size += 1
        print(f"Added {i}, size: {size}, capacity: {capacity}")
    return arr[:size] 
   

"""
Time and Space Analysis for problem 4:
- When do resizes happen? When size == capacity. If capacity is 4, resizes happen at 4, 8, 16, etc.
- What is the worst-case for a single append? O(n)
- What is the amortized time per append overall? O(1)
- Space complexity: O(n)
- Why does doubling reduce the cost overall? If you resize by one, each resize requires copying more elements
Doubling reduces the number of resizes needed, thus reducing the total number of copies made.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    current_sum = 0
    for num in nums:
        current_sum += num
        result.append(current_sum)
    return result

"""
Time and Space Analysis for problem 5:
- Best-case:O(n)
- Worst-case:O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? It iterates through the list once and maintains a running sum.
- Could it be optimized? yes
"""

#refactor problem 5

def running_total(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
print(running_total([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]

# Time Complexity: O(n)
# Space Complexity: O(1)
#The original solution allocates a second list to store results, requiring O(n) extra space.
#The refactored solution reduces extra memory usage to O(1).