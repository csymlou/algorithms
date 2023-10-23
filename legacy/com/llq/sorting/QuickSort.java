package com.llq.sorting;

import java.util.Arrays;

import com.llq.Util.IntegerArrayGenerator;

public class QuickSort {
	
	/**
	 * 快速排序，递归算法
	 * @param A	排序数组
	 * @param p	开始索引
	 * @param r	结束索引
	 */
	public void quickSort(int[] A, int p, int r) {
		if (p < r) {
			int q = partition(A, p, r);
			quickSort(A, p, q - 1);
			quickSort(A, q + 1, r);
		}
	}
	
	/**
	 * 数组划分，最后一个为主元，pivot element
	 * @param A
	 * @param p
	 * @param r
	 * @return 划分点的索引
	 */
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

	/**
	 *  交换 A[i]与A[j]
	 * @param A
	 * @param i
	 * @param j
	 */
	private void exchange(int[] A, int i, int j) {

		int temp = A[i];
		A[i] = A[j];
		A[j] = temp;
	}
	
	
	/**
	 * 快速排序的随机版本，随机选取主元
	 * @param A
	 * @param p
	 * @param r
	 */
	public void randomQuickSort(int[] A, int p, int r) {
		if (p < r) {
			int q = randomPartition(A, p, r);
			randomQuickSort(A, p, q - 1);
			randomQuickSort(A, q + 1, r);
		}
	}
	
	/**
	 * 随机选择一个数作为主元（与最后一个交换，然后使用partition算法）
	 * @param A
	 * @param p
	 * @param r
	 * @return
	 */
	private int randomPartition(int[] A, int p, int r) {
		
		int i = randomBetween(p, r);
		exchange(A, i, r);
		return partition(A, p, r);
	}
	
	/**
	 * 计算两个数中间的随机值
	 * @param low
	 * @param high
	 * @return
	 */
	private int randomBetween(int low, int high) {
		return (int) (Math.random() * (high - low) + low);
	}

	public static void main(String[] args) {
		
		int[] A = IntegerArrayGenerator.randomGenerate(20, 10);
		System.out.println(Arrays.toString(A));
		new QuickSort().randomQuickSort(A, 0, A.length - 1);
		System.out.println(Arrays.toString(A));
	}
	
}
