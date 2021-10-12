using System;
using System.Collections.Generic;

namespace LeetCode
{
  public static class Program
  {
    private static void Main()
    {
      var Array = new List<int>() { 1,2,3,4,5,6};
      var index = Utils.BinarySearch(Array, 0, Array.Count, 3);
      Console.WriteLine(index);
    }
  }
}