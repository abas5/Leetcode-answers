

def find_min(nums):
    result = nums[0]
    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] < nums[right]:
            result = min(result, nums[left])
            break

        middle = (left + right) // 2
        result = min(result, nums[middle])

        if nums[middle] >= nums[left]:
            left = middle + 1
        else:
            right = middle - 1
    
    return result


nums = [3, 4, 5, 1, 2]

ans = find_min(nums)

print(ans)

nums = [3, 4, 5, 1, 2, 2.1, 2.2, 2.3, 2.4]

ans = find_min(nums)

print(ans)