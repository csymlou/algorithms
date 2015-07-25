package com.llq.sorting;

import java.util.Arrays;

import com.llq.Util.IntegerArrayGenerator;

public class CountingSort {
	
	/**
	 * 计数排序
	 * @param A 原始数组
	 * @param B 排序后数组
	 * @param k 原始数组的范围 [0, k]
	 */
	public void countingSort(int[] A, int[] B, int k) {
		
		int[] C = new int[k];
		// let C[i] be 0
		for (int i = 0; i < C.length; i++) {
			C[i] = 0;
		}
		// count A[i]
		for (int i = 0; i < A.length; i++) {
			C[A[i]]++;
		}
		// accumulate A[i]
		for (int i = 1; i < C.length; i++) {
			C[i] += C[i - 1];
		}
		// sort
		for (int i = A.length - 1; i >= 0; i--) {
			B[C[A[i]] - 1] = A[i];
			C[A[i]] --;
		}
	}

	public static void main(String[] args) {
		// range 0 to k
		int k = 10;
		// length n
		int n = 20;
		int[] A = IntegerArrayGenerator.randomGenerate(k, n);
		int[] B = new int[n];
		new CountingSort().countingSort(A, B, k);
		System.out.println(Arrays.toString(A));
		System.out.println(Arrays.toString(B));
		
	}
}
