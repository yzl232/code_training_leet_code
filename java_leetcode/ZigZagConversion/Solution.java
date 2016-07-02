package ZigZagConversion;

public class Solution {
	public String convert(String s, int r) {
		if (r <= 1) {
			return s;
		}
		int zigN = r*2-2, n = s.length();
		StringBuilder ret = new StringBuilder();
		for(int i=0; i<r; i++){
			int base = i;
			while(base<n){
				ret.append(s.charAt(base));
				base+=zigN;
				if(i!=0 && i!=r-1 && base-2*i<n ){
					ret.append(s.charAt(base-2*i));
				}
			}
		}
		return ret.toString();
	}
}