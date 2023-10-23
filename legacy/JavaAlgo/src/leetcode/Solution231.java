package leetcode;

/**
 *  Excel Sheet Column Number
 */
public class Solution231 {
    public boolean isPowerOfTwo(int n) {
        if (n <= 0) return false;
        return (n & (n - 1)) == 0;
    }

    public static void main(String[] args) {
        System.out.println(new Solution231().isPowerOfTwo(0));
    }
}
