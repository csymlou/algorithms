package com.llq.Util;

import java.util.Arrays;
import java.util.Random;

public class StringUtil {
	
	private static final String ALL_NUMBERS = "0123456789";
	private static final String ALL_CHARACTERS = "abcdefghijklmnopqrstuvwxyz";

	public static String[] randomIntegerArray(int length, int width) {
		
		String[] arr = new String[length];
		Random random = new Random();
		for (int i = 0; i < arr.length; i++) {
			StringBuilder sb = new StringBuilder();
			for (int j = 0; j < width; j++) {
				sb.append(ALL_NUMBERS.charAt(random.nextInt(10)));
			}
			arr[i] = sb.toString();
		}
		return arr;
	}
	
	public static String randomString(int length) {
		
		Random random = new Random();
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < length; i++) {
			sb.append(ALL_CHARACTERS.charAt(random.nextInt(ALL_CHARACTERS.length())));
		}
		
		return sb.toString();
	}
	
	public static String[] randomStringArray(int length, int width) {
		String[] arr = new String[length];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = randomString(width);
		}
		return arr;
	}
	
	public static void main(String[] args) {
		
		System.out.println(Arrays.toString(randomStringArray(10, 3)));
	}
}
