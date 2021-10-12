using System;

namespace LeetCode
{
  public static class Program
  {
    private static void Main()
    {
      var str = "bb";
      var palindrome = Palindrome.longestPalindrome(str);
      Console.WriteLine(palindrome);
    }
  }
}