package leetcode;

import java.awt.*;
import java.util.BitSet;

/**
 *  Missing Number
 */
public class Solution268 {
    public int missingNumber(int[] nums) {
        int r = nums.length;
        for (int i = 0; i < nums.length; i++) {
            r = r ^ i ^ nums[i];
        }
        return r;
    }

    public static void main(String[] args) {
        int[] a ={3,0,1};
        System.out.println(new Solution268().missingNumber(a));
    }
}
