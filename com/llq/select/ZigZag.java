package com.llq.select;

/**
 * 动态规划
 * @author Administrator
 *
 */
public class ZigZag {

	public static void main(String[] args) {
		
		int[] A = { 1, 7, 4, 9, 2, 5, 1, 1, -1};
		// R二维数组
		// 第一行记录从前一个数上升到该位置的最大长度
		// 第一行记录从前一个数下降到该位置的最大长度
		int[][] R = new int[2][A.length];
		R[0][0] = 1;
		R[1][0] = 1;
		// max_asc是记录遍历某个位置之前所有数的最大上升长度
		int max_asc = 1;
		// max_asc是记录遍历某个位置之前所有数的最大下降长度
		int max_des = 1;
		
		for (int i = 0; i < A.length; i++) {
			// 遍历位置i之前的所有数
			for (int j = 0; j < i; j++) {
				// 位置j的数大于位置i的数，到位置i是下降，比较max_des
				if (A[j] > A[i]) {
					// 使用j位置的上升长度
					if (R[0][j] + 1 > max_des) {
						max_des = R[0][j] + 1;
					}
				} 
				// 位置j的数小于位置i的数，到位置i是上升，比较max_asc
				else if (A[j] < A[i]) {
					// 使用j位置的下降长度
					if (R[1][j] + 1 > max_asc) {
						max_asc = R[1][j] + 1;
					}
				}
			}
			// 求得到位置i的最大上升或下降长度
			R[0][i] = max_asc;
			R[1][i] = max_des;
		}
		
		for (int i = 0; i < R.length; i++) {
			for (int j = 0; j < R[0].length; j++) {
				System.out.print(R[i][j] + "  ");
			}
			System.out.println();
		}
	}
	
}
