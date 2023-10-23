package leetcode;

/**
 * Sqrt(x)
 */
public class Solution69 {
    public int mySqrt(int x) {
        if (x < 2) return x;
        int r = x / 2;
        while (r > x / r) {
            r = (r + x / r) / 2;
        }
        return r;
    }

    public static void main(String[] args) {
        System.out.println(new Solution69().mySqrt(0));
    }
}
