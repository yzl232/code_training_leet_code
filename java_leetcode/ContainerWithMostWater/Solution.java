package ContainerWithMostWater;

public class Solution {
	public int maxArea(int[] h) {
		int l = 0, r = h.length - 1, ret = 0;
		while (l < r) {
			ret = Math.max(ret, Math.min(h[r], h[l]) * (r - l));
			if (h[r] > h[l]) l++;
			else r--;
		}
		return ret;
	}
}