def stats(nums):
    small = nums[0]
    large = nums[0]
    total = 0

    for n in nums:
        if n < small:
            small = n

        if n > large:
            large = n

        total += n

    avg = total / len(nums)

    return (small, large, avg)

a = list(map(int, input().split()))

print(stats(a))