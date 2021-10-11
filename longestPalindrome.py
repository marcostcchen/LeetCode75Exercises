def longestPalindrome(s: str):
    lgstPalindrome = ""
    for i in range(len(s)):
        palindrome = s[i]
        l = i
        r = i if len(s) % 2 == 1 else i + 1
        while(l >= 0 and r <= len(s) - 1):
            if(s[l] != s[r]):
                break
            palindrome = s[l: r + 1]
            l -= 1
            r += 1

        if(len(palindrome) > len(lgstPalindrome)):
            lgstPalindrome = palindrome
    return lgstPalindrome
