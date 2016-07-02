package StringtoInteger_atoi;

public class Solution {
	public int myAtoi(String ss){
		String s = ss.trim()+"#";
		int sign = 1, i=0;
		long ret=0;
		if(s.charAt(i)=='+') i++;
		else if(s.charAt(i)=='-'){
			i++;
			sign = -1;
		}
		while(s.charAt(i)>='0' && s.charAt(i)<='9'){
			ret = ret*10+s.charAt(i)-'0';
			i++;
			ret = sign*Math.max(Math.min(sign*ret, Integer.MAX_VALUE), Integer.MIN_VALUE);
		}
		return (int) (sign*ret);
	}
}
