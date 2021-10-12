using System.Collections.Generic;

namespace LeetCode
{
    public static class Utils
    {
        public static int BinarySearch(List<int> Array, int left, int right, int value)
        {
            var mid = (left + right) / 2;
            if (Array[mid] == value) return mid;
            if (Array[mid] > value) return BinarySearch(Array, left, right - mid, value);
            if (Array[mid] < value) return BinarySearch(Array, mid + 1, right, value);
            return -1;
        }
    }
}