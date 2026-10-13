def largest_sum_after_k_negations(nums, k):
    nums.sort()

    # Change negative numbers to positive
    for i in range(len(nums)):
        if nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            k -= 1

    # If odd flips are still remaining,
    # flip the smallest absolute value
    if k % 2 == 1:
        i = min(range(len(nums)), key=lambda x: abs(nums[x]))
        nums[i] = -nums[i]

    return sum(nums)


n, k = map(int, input().split())
nums = list(map(int, input().split()))

print(largest_sum_after_k_negations(nums, k))