package leetcode;

/**
 *  Pow(x, n)
 */
public class Solution50 {
    public double myPow(double x, int n) {

        if (x == 0) return 0.0;
        if (n == 0) return 1.0;
        if (n < 0) {
            x = 1 / x;
            if (n == Integer.MIN_VALUE) {
                return x * myPow(x, Integer.MAX_VALUE);
            }
            n = -n;
        }
        if ((n & 1) == 0) return myPow(x * x, n / 2);
        else return x * myPow(x * x, n / 2);
    }

    public static void main(String[] args) {
        System.out.println(new Solution50().myPow(1.1, Integer.MIN_VALUE));
    }
}
