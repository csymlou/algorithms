package leetcode;

import java.util.Arrays;

/**
 * Add Binary
 */
public class Solution67 {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int carry = 0;
        int i = a.length() - 1, j = b.length() - 1;
        while (i >= 0 || j >= 0) {
            int a1 = 0, b1 = 0;
            if (i >= 0) {
                a1 = a.charAt(i) == '0' ? 0 : 1;
            }
            if (j >= 0) {
                b1 = b.charAt(j) == '0' ? 0 : 1;
            }
            int s = a1 + b1 + carry;
            sb.append((s & 1) == 0 ? '0' : '1');
            carry = s / 2;
            i--;
            j--;
        }
        if (carry == 1) {
            sb.append("1");
        }
        return sb.reverse().toString();
    }

    public static void main(String[] args) {
        String s = new Solution67().addBinary("0", "0");
        System.out.println(s);
    }
}
