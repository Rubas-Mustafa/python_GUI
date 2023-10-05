def three_sum(nums):
    nums.sort()
    triplets = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates

        left, right = i + 1, len(nums) - 1
        target = -nums[i]

        while left < right:
            if nums[left] + nums[right] == target:
                triplets.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1  # Skip duplicates
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1  # Skip duplicates
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

    return triplets

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
result = three_sum(nums)
print(nums)
print("target = 0")
print(result)
