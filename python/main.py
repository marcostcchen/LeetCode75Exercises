from longestPalindrome import longestPalindrome
from twoSums import twoSums
from longestStringWithoutRepeating import longestStringWithoutRepeating

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(f"TwoSums: {str(twoSums(nums, target))}")

    string = "pwwkew"
    solutionArray = longestStringWithoutRepeating(string)
    print(
        f"LgstStrNoRepeat: {str(solutionArray)}, Length: {str(len(solutionArray))}")

    s = "babad"
    lgstpalindrome = longestPalindrome(s)
    print(
        f"LgstPalindrome: {str(lgstpalindrome)}, Length: {str(len(lgstpalindrome))}")
