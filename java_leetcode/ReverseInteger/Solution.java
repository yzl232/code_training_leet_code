
public class Solution {
	public int reverse(int x) {
		long ret = 0;

		while (x != 0) {
			ret = ret * 10 + x%10;
			x /= 10;
		}
		if (Math.abs(ret) > Integer.MAX_VALUE) return 0;
		else return (int) ret;
	}
}