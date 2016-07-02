/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
package AddTwoNumbers;
public class Solution {
	public ListNode addTwoNumbers(ListNode l1, ListNode l2){
		ListNode dummy = new ListNode(0), cur = dummy;
		int carry = 0, s;
		while (l1 != null || l2 != null || carry != 0){
			s = carry;
			if(l1 != null){
				s += l1.val;
				l1 = l1.next;
			}
			if(l2 != null){
				s += l2.val;
				l2 = l2.next;
			}
			carry = s/10;
			s = s%10;
			cur.next = new ListNode(s);
			cur = cur.next;
		}
		return dummy.next;
	}
}