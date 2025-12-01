def longest_consecutive(nums):
    num_set = set(nums)  # Convert list to set for O(1) lookups
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # Start of a new sequence
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest

# Example usage:
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4