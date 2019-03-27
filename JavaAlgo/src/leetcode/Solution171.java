package leetcode;

/**
 *  Excel Sheet Column Number
 */
public class Solution171 {
    private int trans(char c) {
        return c - 'A' + 1;
    }
    public int titleToNumber(String s) {
        int r = 0;
        for (int i = 0; i < s.length(); i++) {
            r = r * 26 + trans(s.charAt(i));
        }
        return r;
    }

    public static void main(String[] args) {
        System.out.println(new Solution171().titleToNumber("ZY"));
    }
}
