package com.llq.sorting;

import java.util.Arrays;

import com.llq.Util.HeapUtil;
import com.llq.Util.IntegerArrayGenerator;

public class MaxHeap {
	
	private int[] arr;
	private int heapSize;
	
	public MaxHeap() {
		arr = IntegerArrayGenerator.randomGenerate(10, 10);
//		arr = new int[]{1,2,3,4,5,6};
		heapSize = arr.length;
	}

	/**
	 * 维护最大堆的函数，从pos位置向下维护最大堆
	 * @param pos
	 * 		开始位置
	 */
	public void maxHeapify(int pos) {
		int leftIdx = left(pos);
		int rightIdx = right(pos);
		int largestIdx;
		// 找出最大值
		if (leftIdx < heapSize && arr[leftIdx] > arr[pos]) {
			largestIdx = leftIdx;
		} else {
			largestIdx = pos;
		}
		if (rightIdx < heapSize && arr[rightIdx] > arr[largestIdx]) {
			largestIdx = rightIdx;
		}
		if (largestIdx != pos) {
			// 交换 arr[pos] 和 arr[largestIdx]
			exchange(pos, largestIdx);
			// 递归
			maxHeapify(largestIdx);
		}
		// 最后一定是 largestIdx 等于 pos
	}
	
	/**
	 * 建立最大堆，数组arr从中间元素到首元素遍历建堆
	 */
	public void buildMaxHeap() {
		heapSize = arr.length;
		for (int i = arr.length/2 - 1; i >= 0; i--) {
			maxHeapify(i);
			HeapUtil.print(arr);
			System.out.println("-----------------------------");
		}
	}
	
	/**
	 * 利用已经建好的最大堆，完成堆排序
	 */
	public void heapSort() {
		for (int i = arr.length - 1; i > 0; i--) {
			//每次将堆最后一个值与arr[0]交换
			exchange(0, i);
			// heapSize为未排序长度
			heapSize--;
			// 从 arr[0]维护堆
			maxHeapify(0);
		}
	}
	
	
	public void increaseKey(int pos, int value) {
		if (value < arr[pos]) {
			return;
		}
		arr[pos] = value;
		while (pos > 0 && arr[parent(pos)] < arr[pos]) {
			// exchange arr[pos] with arr[parent(pos)]
			exchange(pos, parent(pos));
			pos = parent(pos);
		}
	}
	
	public void print() {
		System.out.println(Arrays.toString(arr));
	}
	
	// Java start with 0
	private int parent(int i) {
		return (i - 1) / 2;
	}

	private int left(int i) {
		return 2 * i + 1;
	}

	private int right(int i) {
		return 2 * i + 2;
	}
	
	private void exchange(int pos1, int pos2) {
		int temp = arr[pos1];
		arr[pos1] = arr[pos2];
		arr[pos2] = temp;
	}
	
	public static void main(String[] args) {
		MaxHeap heap = new MaxHeap();
		heap.print();
		heap.buildMaxHeap();
		heap.print();
//		heap.heapSort();
		heap.print();
		heap.increaseKey(4, 100);
		heap.print();
	}
}
