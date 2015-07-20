package com.llq.Util;

public class HeapUtil {

	public static void print(int[] arr) {
		int levelCount = Integer.SIZE
				- Integer.numberOfLeadingZeros(arr.length);
		int[] spaces = new int[levelCount];
		for (int i = 0; i < levelCount; i++) {
			spaces[i] = (1 << i) - 1;
		}
		for (int i = 0; i < levelCount; i++) {
			int spaceIdx = levelCount - i - 1;
			for (int j = 0; j < spaces[spaceIdx]; j++) {
				System.out.print(" ");
			}
			int startIdx = (1 << i) - 1;
			System.out.print(arr[startIdx]);
			for (int k = 1; k < (1 << i); k++) {
				for (int j = 0; j < spaces[spaceIdx + 1]; j++) {
					System.out.print(" ");
				}
				if (startIdx + k < arr.length) {
					System.out.print(arr[startIdx + k]);
				}

			}
			System.out.println();

		}
	}

	public static void main(String[] args) {
		print(IntegerArrayGenerator.randomGenerate(10, 50));
	}

}
