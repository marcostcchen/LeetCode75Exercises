namespace LeetCode
{
    public static class Palindrome
    {
        public static string longestPalindrome(string s)
        {
            var longest = "";
            for (var i = 0; i < s.Length; i++)
            {
                var palindrome1 = expandFromMiddle(s, i, i);
                var palindrome2 = expandFromMiddle(s, i, i + 1);
                var palindrome = palindrome1.Length > palindrome2.Length ? palindrome1 : palindrome2;
                if (palindrome.Length > longest.Length) longest = palindrome;
            }

            return longest;
        }

        private static string expandFromMiddle(string s, int left, int right)
        {
            var longest = s.Substring(left, 1);
            while (left >= 0 && right <= s.Length - 1 && s[left] == s[right])
            {
                longest = s.Substring(left, right - left + 1);
                left--;
                right++;
            }

            return longest;
        }
    }
}