package com.llq.sorting;

import java.util.Arrays;

public class RadixSort {
	
	public void radixSort(String[] A, int d) {
		for (int i = d - 1; i >= 0; i--) {
			quickSort(A, i, 0, A.length - 1);
			System.out.println(Arrays.toString(A));
		}
	}

	
	private void quickSort(String[] A, int idx, int p, int r) {
		
		if (p < r) {
			int q = partition(A, idx, p, r);
			quickSort(A, idx, p, q - 1);
			quickSort(A, idx, q + 1, r);
		}
		
	}


	private int partition(String[] A, int idx, int p, int r) {
		
		char x = A[r].charAt(idx);
		int i = p - 1;
		for (int j = p; j < r; j++) {
			if (A[j].charAt(idx) <= x) {
				i++;
				exchange(A, i, j);
			}
		}
		i++;
		exchange(A, i, r);
		return i;
	}

	private void exchange(String[] A, int i, int j) {

		String temp = A[i];
		A[i] = A[j];
		A[j] = temp;
	}


	public static void main(String[] args) {
		String[] A = {"329", "457", "657", "839", "436", "720", "355"};
		System.out.println(Arrays.toString(A));
		System.out.println();
		new RadixSort().radixSort(A, A[0].length());
	}
}
