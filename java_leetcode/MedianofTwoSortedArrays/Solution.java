package MedianofTwoSortedArrays;

import java.util.Arrays;

public class Solution {
	public double findMedianSortedArrays(int A[], int B[]) {
		int m = A.length, n = B.length;
		return (m + n) % 2 == 1 ? findKth(A, B, (m + n) / 2 + 1)
				: 0.5 * (findKth(A, B, (m + n) / 2 + 1) + findKth(A, B, (m + n) / 2));
	}

	public int findKth(int A[], int B[], int k) {
		int m = A.length, n = B.length;
		if (m > n) {
			return findKth(B, A, k);
		}
		if (m == 0) {
			return B[k - 1];
		}
		if (k == 1){
			return Math.min(A[0], B[0]);
		}
		int pa = Math.min(k / 2, m), pb = k - pa;
		return A[pa - 1] <= B[pb - 1] ? findKth(Arrays.copyOfRange(A, pa, m), B, k - pa)
				: findKth(A, Arrays.copyOfRange(B, pb, n), k - pb);
	}
}
