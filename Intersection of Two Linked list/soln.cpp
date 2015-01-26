/**
* Definition for singly-linked list.
* struct ListNode {
*     int val;
*     ListNode *next;
*     ListNode(int x) : val(x), next(NULL) {}
* };
*/
class Solution {
public:
	ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
		ListNode* retPtr = NULL;
		ListNode* A = headA;    //keep our ptr
		ListNode* B = headB;

		int Alen = 0;
		int Blen = 0;

		//measure the length of A and B
		while (A != NULL) {
			Alen++;
			A = A->next;
		}
		while (B != NULL) {
			Blen++;
			B = B->next;
		}
		//restore the ptr
		A = headA;
		B = headB;


		if (Alen > Blen) {
			//skip the extra content
			for (int i = 0; i < (Alen - Blen); i++) {
				A = A->next;
			}
			//do a linear search after content skiped
			for (int i = 0; i < Blen; i++) {
				if (A == B) {
					return A;
				}
				A = A->next;
				B = B->next;
			}
			return NULL;
		}
		else {
			for (int i = 0; i < (Blen - Alen); i++) {
				B = B->next;
			}
			for (int i = 0; i < Alen; i++) {
				if (A == B) {
					return A;
				}
				A = A->next;
				B = B->next;
			}
			return NULL;
		}

		return NULL;
	}
};