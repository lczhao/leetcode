Symmetric Tree
---

[leetcode problem link](https://oj.leetcode.com/problems/symmetric-tree/)

This problem asks us to detect whether or not a tree is symmetric

The strategy I used is to flatten out the tree into a palindrome (along with the level we are) using pre-ordering, that is:

		Left + Current + Right

I'm adding the level to avoid this problem:

		      1
		    2   3
		   3   2
		
		=> 32123 is a palindrome 
		=> [(3,2), (2,1), (1,0), (2,2), (3,3)] is not