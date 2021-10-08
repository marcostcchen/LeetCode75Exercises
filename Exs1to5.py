# Logica de utilizar a sub e comparar com o target
def twoSumsIndex(nums, target: int):
    results = []

    for num in nums:
        sub = target - num
        if(sub in nums):
            results.append(nums.index(num))
    return results


# Logica do window sliding
def longestStringWithoutRepeating(string: str):
    finalArray = []

    array = []
    for r in range(len(string)):

        while(string[r] in array):
            array.pop(0)
        array.append(string[r])

        if(len(finalArray) < len(array)):
            finalArray = array.copy()

    return finalArray




if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(f"TwoSums: {str(twoSumsIndex(nums, target))}")

    string = "pwwkew"
    solutionArray = longestStringWithoutRepeating(string)
    print(
        f"LgstStrNoRepeat: {str(solutionArray)}, Length: {str(len(solutionArray))}")
