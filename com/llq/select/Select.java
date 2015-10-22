package com.llq.select;

import java.util.Arrays;

import com.llq.Util.IntegerArrayGenerator;

public class Select {
	
	/**
	 * 同时找出最大值和最小值，时间复杂度为3(n-1)/2
	 * @param A
	 */
	public static void findMinMax(int[] A) {
		int min;
		int max;
		if ((A.length & 1) == 0) {
			// 长度为偶数
			if (A[0] <= A[1]) {
				min = A[0];
				max = A[1];
			} else {
				min = A[1];
				max = A[0];
			}
			for (int i = 2; i < A.length; i=i+2) {
				if (A[i] <= A[i+1]) {
					if (min > A[i]) {
						min = A[i];
					}
					if (max < A[i+1]) {
						max = A[i+1];
					}
				} else {
					if (min > A[i+1]) {
						min = A[i+1];
					}
					if (max < A[i]) {
						max = A[i];
					}
				}
			}
		} else {
			// 长度为奇数
			min = max = A[0];
			for (int i = 1; i < A.length; i = i+2) {
				if (A[i] <= A[i+1]) {
					if (min > A[i]) {
						min = A[i];
					}
					if (max < A[i+1]) {
						max = A[i+1];
					}
				} else {
					if (min > A[i+1]) {
						min = A[i+1];
					}
					if (max < A[i]) {
						max = A[i];
					}
				}
			}
		}
		System.out.println("min = " + min);
		System.out.println("max = " + max);
	}

	/**
	 * 找出数组A中第iMin小的数，时间复杂度为n
	 * @param A 原始数组
	 * @param p
	 * @param r
	 * @param iMin 从1开始数第iMin小的数
	 * @return
	 */
	public int randomSelect(int[] A, int p, int r, int iMin) {
		if (iMin > A.length) {
			throw new RuntimeException("参数错误");
		}
		if (p == r) {
			return A[p];
		}
		int q = randomPartition(A, p, r);
		int k = q - p + 1;
		if (iMin == k) {
			return A[q];
		} else if (iMin < k) {
			return randomSelect(A, p, q - 1, iMin);
		} else {
			return randomSelect(A, q + 1, r, iMin - k);
		}
		
	}
	
	private int randomPartition(int[] A, int p, int r) {
		
		int i = randomBetween(p, r);
		exchange(A, i, r);
		return partition(A, p, r);
	}
	
	private int partition(int[] A, int p, int r) {
		
		int x = A[r];
		int i = p - 1;
		for (int j = p; j < r; j++) {
			if (A[j] <= x) {
				i++;
				exchange(A, i, j);
			}
		}
		exchange(A, i + 1, r);
		return i + 1;
	}
	
	private int randomBetween(int low, int high) {
		return (int) (Math.random() * (high - low) + low);
	}
	
	private void exchange(int[] A, int i, int j) {

		int temp = A[i];
		A[i] = A[j];
		A[j] = temp;
	}
	
	
	
	public static void main(String[] args) {
		int[] A = IntegerArrayGenerator.randomGenerate(20, 50);
		System.out.println(Arrays.toString(A));
		findMinMax(A);
		
		int a = new Select().randomSelect(A, 0, A.length - 1, A.length/2 + 1);
		System.out.println(a);
		
	}
}
