package com.llq.Util;

import java.util.Arrays;
import java.util.Random;

public class IntegerArrayGenerator {

	public static int[] randomGenerate(int maxValue, int length) {
		
		int[] result = new int[length];
		
		Random random = new Random();
		
		for (int i = 0; i < result.length; i++) {
			result[i] = random.nextInt(maxValue);
		}
		
		return result;
		
	}
	
	public static void main(String[] args) {
		
		int[] arr = IntegerArrayGenerator.randomGenerate(104, 50);
		
		System.out.println(Arrays.toString(arr));
	}
}
