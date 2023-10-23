package leetcode;

import java.util.Arrays;

/**
 *  Plus One
 */
public class Solution66 {
    public int[] plusOne(int[] digits) {
        int carry = 1;
        for (int i = digits.length - 1; i >= 0 ; i--) {
            int s = digits[i] + carry;
            digits[i] = s % 10;
            carry = s / 10;
            if (carry == 0) break;
        }
        if (carry == 1) {
            int[] arr = new int[digits.length + 1];
            System.arraycopy(digits,0,arr, 1,digits.length);
            arr[0] = 1;
            return arr;
        }
        return digits;
    }

    public static void main(String[] args) {
        int[] a = new int[]{1,0,0};
        int[] b = new Solution66().plusOne(a);
        System.out.println(Arrays.toString(b));
    }
}
