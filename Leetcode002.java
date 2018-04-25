/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode current = head;
        int carry = 0;
        while(l1 != null || l2 != null || carry != 0){
            int v1 = 0;
            int v2 = 0;

            if(l1 == null){
                v1 = 0;
            }else{
                v1 = l1.val;
                l1 = l1.next;
            }

            if(l2 == null){
                v2 = 0;
            }else{
                v2 = l2.val;
                l2 = l2.next;
            }

            int sum = v1 + v2 + carry;
            int val = sum % 10;
            carry = sum / 10;
            ListNode temp = new ListNode(val);
            current.next = temp;
            current = current.next;
        }
        return head.next;

    }
}
