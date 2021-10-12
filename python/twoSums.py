# Logica de utilizar a sub e comparar com o target
def twoSums(nums, target: int):
    results = []

    for num in nums:
        sub = target - num
        if(sub in nums):
            results.append(nums.index(num))
    return results
