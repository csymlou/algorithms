package com.llq.dp;

/**
 * 装载问题 每个物品重量为 w1, w2, ..., wn 能装载的总重为 C 选择物品是装载量最大但不超过 C 动态规划 状态: m(i, t)
 * 表示选择范围是1-i, 能装下的剩余重量是t wi表示第i个物品的重量 若：0 <= t < wi, 不能装下wi，m(i, t) = m(i - 1,
 * t) 若：t >= wi，可以考虑是否装wi 若不装：则 m(i, t) = m(i - 1, t) 若装：则 m(i, t) = m(i - 1, t
 * - wi) + wi 以上二则取最大
 */
public class Loading {

	public static void main(String[] args) {

		// start with 1
		int[] w = { Integer.MIN_VALUE, 2, 50, 13, 8, 4 };
		int C = 50;

		// m[*][0] = m[0][*] = 0
		int[][] m = new int[w.length][C + 1];

		int a = 0; // temp
		int b = 0; // temp

		for (int i = 0; i < w.length; i++) {
			for (int t = 0; t <= C; t++) {
				m[i][t] = 0;
			}
		}

		for (int i = 1; i < w.length; i++) {
			for (int t = 0; t <= C; t++) {
				if (t < w[i]) {
					m[i][t] = m[i - 1][t]; // 不装w[i]
				} else {
					a = m[i - 1][t];
					b = m[i - 1][t - w[i]] + w[i];
					if (a > b) {
						m[i][t] = a; // 不装 w[i]
					} else {
						m[i][t] = b; // 装 w[i]
					}
				}
			}
		}

		// 构造选择
		boolean[] choose = new boolean[w.length - 1];
		int t = m[w.length - 1][C]; // the last one
		for (int i = w.length - 1; i > 0; i--) {
			if (t >= w[i]) {
				a = m[i - 1][t];
				b = m[i - 1][t - w[i]] + w[i];
				if (a > b) {
					choose[i - 1] = false;
				} else {
					choose[i - 1] = true;
					t -= w[i];
				}
			} else {
				choose[i - 1] = false;
			}
		}

		System.out.println("max: " + m[w.length - 1][C]);
		for (int i = 0; i < choose.length; i++) {
			if (choose[i]) {
				System.out.print(w[i + 1] + "  ");
			}
		}

	}
}
