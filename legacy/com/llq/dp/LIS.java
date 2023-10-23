package com.llq.dp;

import java.util.Arrays;

import com.llq.Util.IntegerArrayGenerator;

public class LIS {

	public static void main(String[] args) {
		
		final int N = 10;
		
		int[] a = IntegerArrayGenerator.randomGenerate(10, N);
		int[] b = new int[a.length];
		int max;
		int allMax = 1;
		
		for (int i = 0; i < a.length; i++) {
			b[i] = 1;
			max = 1;
			for (int j = i - 1; j >= 0; j--) {
				if ((a[j] <= a[i]) && (b[j] + 1 > max)) {
					max = b[j] + 1;
				}
			}
			b[i] = max;
			if (max > allMax) {
				allMax = max;
			}
		}
		
		System.out.println(Arrays.toString(a));
		System.out.println(Arrays.toString(b));
		
		System.out.println(allMax);
		int[] c = new int[allMax];
		int n = allMax;
		
		for (int i = b.length - 1; i >= 0; i--) {
			if (b[i] == n) {
				c[n - 1] = a[i];
				n--;
			}
		}
		System.out.println(Arrays.toString(c));
	}
}
