package com.llq.sorting;

import java.util.Arrays;

import com.llq.Util.IntegerArrayGenerator;

public class Sort {
	
	public static void insertSort(int[] arr) {
		int key;
		int i;
		for (int j = 1; j < arr.length; j++) {
			key = arr[j];
			i = j - 1;
			while (i >= 0 && arr[i] > key) {
				arr[i + 1] = arr[i];
				i = i - 1;
				System.out.println("  " + Arrays.toString(arr));
			}
			arr[i + 1] = key;
			System.out.println(Arrays.toString(arr));
		}
	}
	
	public static void main(String[] args) {
		int[] arr = IntegerArrayGenerator.randomGenerate(10, 6);
//		System.out.println(Arrays.toString(arr));
		insertSort(arr);
//		System.out.println(Arrays.toString(arr));
	}
}
