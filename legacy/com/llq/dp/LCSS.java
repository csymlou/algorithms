package com.llq.dp;


/**
 * 最长公共子序列
 * 
 * @author Administrator
 * 
 */
public class LCSS {

	public static void main(String[] args) {

		char[] a = "#hsbafdreghsbacdba".toCharArray();
		char[] b = "#acdbegshbdrabsa".toCharArray();

		int[][] c = new int[a.length + 1][b.length + 1];
		for (int i = 0; i < a.length + 1; i++) {
			for (int j = 0; j < b.length + 1; j++) {
				c[i][j] = 0;
			}
		}

		for (int i = 1; i < a.length; i++) {
			for (int j = 1; j < b.length; j++) {
				if (a[i] == b[j]) {
					c[i][j] = c[i - 1][j - 1] + 1;
				} else {
					if (c[i - 1][j] > c[i][j - 1]) {
						c[i][j] = c[i - 1][j];
					} else {
						c[i][j] = c[i][j - 1];
					}
				}
			}
		}

		for (int j = 1; j < c[0].length - 1; j++) {
			for (int i = 1; i < c.length - 1; i++) {
				System.out.print(c[i][j] + "  ");
			}
			System.out.println();
		}
	}

}
