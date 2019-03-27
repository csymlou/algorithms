package leetcode;

/**
 *  Ugly Number
 */
public class Solution263 {
    public boolean isUgly(int num) {
        int n = num;
        while ((n & 1) == 0) {
            n >>= 1;
        }
        while (n % 3 == 0) {
            n /= 3;
        }
        while (n % 5 == 0) {
            n /= 5;
        }
        return n == 1;
    }

    public static void main(String[] args) {
        System.out.println(new Solution263().isUgly(0));
    }
}
