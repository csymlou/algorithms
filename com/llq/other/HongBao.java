package com.llq.other;

public class HongBao {

	public static void main(String[] args) {
		func();
	}

	private static void func1() {
		double totalMoney = 10;
		int totalPeople = 8;

		double min = 0.01;
		double[] arrMoney = new double[totalPeople];

		for (int i = 0; i < totalPeople - 1; i++) {
			int given = i + 1;
			double safeMoney = (totalMoney - (totalPeople - given) * min)
					/ (totalPeople - given);
			double temp = (Math.random() * (safeMoney * 100 - min * 100) + min * 100) / 100;
			totalMoney -= temp;
			arrMoney[i] = temp;
		}
		arrMoney[totalPeople - 1] = totalMoney;

		double count = 0;
		for (int i = 0; i < arrMoney.length; i++) {
			count += arrMoney[i];
			System.out.printf("%.2f", arrMoney[i]);
			System.out.println();
		}

		System.out.println("count: " + count);
	}

	static void func() {
		int total = 1000;
		int low = 30;
		int high = 100;
		int n = 20;

		int min = low;
		int[] arr = new int[n];
		int temp;
		for (int i = 1; i < n; i++) {
			int r = n - i; // remain
			int safeHigh = (total - r * min);
			do {
				temp = (int) (Math.random() * safeHigh );
			} while (temp > high || temp < low);
			arr[i - 1] = temp;
			total -= temp;
		}
		arr[n - 1] = total;

		int count = 0;
		for (int i = 0; i < arr.length; i++) {
			count += arr[i];
			System.out.println(arr[i]);
		}
		System.out.println("count: " + count);
	}

}
