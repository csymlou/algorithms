package com.llq.sorting;

import java.util.Arrays;

import com.llq.Util.IntegerArrayGenerator;

public class MaxHeap {
	
	private int[] arr;
	private int heapSize;
	
	public MaxHeap() {
		arr = IntegerArrayGenerator.randomGenerate(20, 20);
		heapSize = arr.length;
	}

	
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
			int temp = arr[pos];
			arr[pos] = arr[largestIdx];
			arr[largestIdx] = temp;
			// 递归
			maxHeapify(largestIdx);
		}
		// 最后一定是 largestIdx 等于 pos
	}
	
	public void buildMaxHeap() {
		heapSize = arr.length;
		for (int i = arr.length/2 - 1; i >= 0; i--) {
			maxHeapify(i);
		}
	}
	
	public void heapSort() {
		for (int i = arr.length - 1; i > 0; i--) {
			//每次将堆最后一个值与arr[0]交换
			int temp = arr[0];
			arr[0] = arr[i];
			arr[i] = temp;
			// heapSize为未排序长度
			heapSize--;
			// 从 arr[0]维护堆
			maxHeapify(0);
		}
	}
	
	public void maxHeapInsert(int value) {
		
	}
	
	public int extractMax() {
		
		return 0;
	}
	
	public void increaseKey(int position) {
		
	}
	
	public void print() {
		System.out.println(Arrays.toString(arr));
	}
	
	private int parent(int i) {
		return i / 2;
	}

	private int left(int i) {
		return 2 * i;
	}

	private int right(int i) {
		return 2 * i + 1;
	}
	
	public static void main(String[] args) {
		MaxHeap heap = new MaxHeap();
		heap.print();
		heap.buildMaxHeap();
		heap.print();
		heap.heapSort();
		heap.print();
	}
}
