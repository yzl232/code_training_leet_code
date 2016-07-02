public class Solution {
	public int len, left, right;
	public void expand(String s, int l, int r){
		while(l>=0 && r<s.length() && s.charAt(l)==s.charAt(r)){
			l--;
			r++;
			if(r-l-1>len){
				left = l+1;
				right = r-1;
				len = r-l-1;
			}
		}
	
	}
	public String longestPalindrome(String s){
		for(int i=0; i<s.length(); i++){
			expand(s, i, i);
			expand(s, i, i+1);
		}
		return s.substring(left, right+1);
	}
}
