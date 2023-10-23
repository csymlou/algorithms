package com.llq.sorting;

import java.util.Arrays;

import com.llq.Util.StringUtil;

public class RadixSort {
	
	/**
	 * 基数排序，将待排序的数组A从第d-1位到第0位依次排序
	 * @param A 待排序数组
	 * @param d 排序进行的位数
	 */
	public void radixSort(String[] A, int d) {
		for (int i = d - 1; i >= 0; i--) {
//			insertSort(A, i);
			countingSort(A, i, 10);
			System.out.println(Arrays.toString(A));
		}
	}

	/**
	 *  使用插入排序，事件复杂度为n^2
	 * @param A
	 * @param rdx
	 */
	@SuppressWarnings("unused")
	private void insertSort(String[] A, int rdx) {
		char key;
		String keyString;
		int i;
		for (int j = 1; j < A.length; j++) {
			key = A[j].charAt(rdx);
			keyString = A[j];
			i = j - 1;
			while (i >= 0 && A[i].charAt(rdx) > key) {
				A[i + 1] = A[i];
				i--;
			}
			A[i + 1] = keyString;
		}
	}
	
	/**
	 * 使用计数排序，线性时间复杂度
	 * @param A 待排序数组
	 * @param rdx 排序的位
	 * @param range 位变化的范围
	 */
	private static void countingSort(String[] A, int rdx, int range) {
		String[] B = new String[A.length];
		int[] C = new int[range];
		for (int i = 0; i < C.length; i++) {
			C[i] = 0;
		}
		for (int i = 0; i < A.length; i++) {
			C[A[i].charAt(rdx) - '0'] ++;
		}
		for (int i = 1; i < C.length; i++) {
			C[i] += C[i - 1];
		}
		for (int i = A.length - 1; i >= 0; i--) {
			int idx = A[i].charAt(rdx) - '0';
			B[C[idx] - 1] = A[i];
			C[idx]--;
		}
		System.arraycopy(B, 0, A, 0, B.length);
	}


	public static void main(String[] args) {
		String[] A = StringUtil.randomIntegerArray(10, 3);
		System.out.println(Arrays.toString(A));
		System.out.println();
		
		new RadixSort().radixSort(A, A[0].length());
		
//		countingSort(A, 0, 10);
		System.out.println();
		System.out.println(Arrays.toString(A));
	}
}
